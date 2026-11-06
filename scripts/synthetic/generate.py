#!/usr/bin/env python3
"""
Synthetic programme data engine.

Generates a fictional capital programme (the Halden Vale Health Campus
Programme) as a set of CSV files a PMO would recognise: a portfolio register,
a RAID log, a fortnightly action tracker and a weekly history table. Nothing
here is real. Every name, figure and owner is invented.

The output for any week is a pure function of (SEED, as-of Monday). The script
replays the programme from GENESIS one week at a time, using a random generator
seeded by the week, so:

  * running it twice for the same week gives byte-identical files
  * the weekly GitHub Action only ever moves the programme forward
  * anyone can rebuild any past week with --as-of

Standard library only. Python 3.10+.

Usage
  python scripts/synthetic/generate.py                 # current week
  python scripts/synthetic/generate.py --as-of 2026-09-07
  python scripts/synthetic/generate.py --out /tmp/x    # write somewhere else
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import random
from dataclasses import dataclass, field
from pathlib import Path

SEED = "halden-vale"
GENESIS = dt.date(2026, 5, 4)  # a Monday
PROGRAMME = "Halden Vale Health Campus Programme"
HISTORY_WEEKS = 104
HIGH_EXPOSURE = 15  # residual score at or above this is high exposure
MEDIUM_EXPOSURE = 8

ROOT = Path(__file__).resolve().parents[2]

# --------------------------------------------------------------------------
# Reference data. All fictional.
# --------------------------------------------------------------------------

WORKSTREAMS = {
    "EW": "Enabling Works",
    "MB": "Main Build",
    "DI": "Digital and IT",
    "CM": "Clinical Mobilisation",
    "EF": "Estates and Facilities",
    "FC": "Finance and Commercial",
    "CE": "Communications and Engagement",
}

# Owners are role codes, never people.
OWNERS = {
    "PD": "Programme Director",
    "PMO": "PMO Lead",
    "EWL": "Enabling Works Lead",
    "CPM": "Construction Project Manager",
    "DGL": "Digital Lead",
    "CTL": "Clinical Transition Lead",
    "ESL": "Estates Lead",
    "CML": "Commercial Lead",
    "FNL": "Finance Lead",
    "CEL": "Communications Lead",
}

WORKSTREAM_OWNERS = {
    "EW": ["EWL", "CPM"],
    "MB": ["CPM", "PD"],
    "DI": ["DGL"],
    "CM": ["CTL"],
    "EF": ["ESL"],
    "FC": ["CML", "FNL"],
    "CE": ["CEL"],
}

# (id, name, workstream, budget £m, start, baseline finish)
PROJECTS = [
    ("P01", "Site enabling and demolition", "EW", 18.4, "2025-09-01", "2027-01-29"),
    ("P02", "Utilities diversion and substation", "EW", 9.2, "2025-11-03", "2027-03-26"),
    ("P03", "Main hospital block", "MB", 412.0, "2026-03-02", "2030-06-28"),
    ("P04", "Multi-storey car park", "MB", 24.5, "2026-06-01", "2028-02-25"),
    ("P05", "Electronic patient record integration", "DI", 14.8, "2026-01-05", "2029-09-28"),
    ("P06", "Network and infrastructure fit-out", "DI", 6.3, "2027-04-05", "2030-03-29"),
    ("P07", "Clinical service transition planning", "CM", 3.1, "2026-02-02", "2030-09-27"),
    ("P08", "Soft FM procurement", "EF", 1.2, "2026-04-06", "2027-10-29"),
    ("P09", "Stakeholder engagement programme", "CE", 0.6, "2025-10-06", "2030-12-20"),
]

RISK_BANK = {
    "EW": [
        "Ground conditions differ from the site investigation",
        "Asbestos found in buildings due for demolition",
        "Network operator approval for utility diversion delayed",
        "Ecology survey window missed, delaying site clearance",
        "Highways licence for site access not granted in time",
        "Unrecorded services found during excavation",
        "Archaeological finds pause groundworks",
        "Decant accommodation not ready before demolition",
    ],
    "MB": [
        "Long-lead plant procurement exceeds programme float",
        "Inflation on mechanical and electrical packages exceeds allowance",
        "Main contractor resource shortfall on site",
        "Design freeze slips due to late clinical change requests",
        "Tier 2 subcontractor insolvency",
        "Fire strategy sign-off delayed by building control",
        "Weather delays to the frame programme",
        "Modern methods of construction supplier capacity constrained",
        "Commissioning resource not secured for handover",
    ],
    "DI": [
        "EPR integration testing window compressed",
        "Cyber assurance sign-off delayed",
        "Data migration quality below acceptance threshold",
        "Network hardware lead times extend",
        "Legacy system decommissioning dependencies not mapped",
        "Digital clinical safety case not approved in time",
    ],
    "CM": [
        "Clinical engagement capacity constrained by winter pressures",
        "Recruitment for new service models behind plan",
        "Patient flow model assumptions not validated",
        "Training plan for new building not resourced",
        "Service change consultation extends timeline",
    ],
    "EF": [
        "Soft FM market interest lower than expected",
        "Maintenance regime not agreed before handover",
        "Energy performance targets not met in design",
        "Waste management route not agreed with contractor",
    ],
    "FC": [
        "Funding drawdown profile misaligned with spend",
        "Optimism bias allowance insufficient",
        "Compensation event volume exceeds forecast",
        "VAT recovery position challenged",
        "Contingency drawdown ahead of plan",
    ],
    "CE": [
        "Local objections to car park design",
        "Negative press coverage on programme delays",
        "Staff engagement drops during construction disruption",
        "Stakeholder fatigue with consultation events",
    ],
}

ISSUE_BANK = {
    "EW": ["Contaminated soil found in north compound", "Diversion works paused pending permit"],
    "MB": ["Steel delivery delayed by four weeks", "Clash found in level 2 services coordination"],
    "DI": ["Interface specification rejected by supplier", "Test environment unavailable"],
    "CM": ["Clinical lead post vacant", "Workshop attendance below quorum"],
    "EF": ["Tender returns over budget", "Lift maintenance contract lapsed"],
    "FC": ["Invoice backlog on enabling works", "Cost report issued late"],
    "CE": ["Complaint received on construction noise", "Website content out of date"],
}

ASSUMPTION_BANK = [
    ("FC", "Capital funding profile confirmed at current envelope"),
    ("MB", "Planning consent conditions dischargeable within eight weeks"),
    ("DI", "Existing EPR contract extendable to 2030"),
    ("CM", "Bed modelling based on current length of stay holds"),
    ("EW", "Network operator capacity available for new substation"),
    ("EF", "Current FM provider supports transition period"),
    ("CE", "Public consultation not required for car park"),
    ("FC", "Inflation indices track central forecast"),
    ("MB", "Site available for continuous working hours"),
    ("DI", "National integration standards stable during build"),
]

DEPENDENCY_BANK = [
    ("EW", "Utility diversion complete before main build piling"),
    ("MB", "Design freeze before contractor price"),
    ("DI", "Network fit-out before EPR go-live"),
    ("CM", "Workforce plan approved before service transition"),
    ("FC", "Full business case approval before main contract award"),
    ("EF", "FM contract live before building handover"),
    ("MB", "Car park complete before old car park demolition"),
    ("DI", "Cyber assurance before clinical system migration"),
    ("CE", "Comms plan agreed before site hoarding goes up"),
    ("EW", "Decant complete before demolition of old blocks"),
]

# Appended when a title is already open, so two live items never read the same.
QUALIFIERS = ["phase 2", "Block B", "level 3", "north site", "south site", "package 4", "temporary works", "fit-out"]

MITIGATIONS = [
    "Early engagement with approving body, fortnightly check-in",
    "Additional survey commissioned",
    "Programme float protected and reported weekly",
    "Alternative supplier identified and pre-qualified",
    "Escalated to programme board for decision",
    "Contingency allocated against this item",
    "Design team workshop scheduled",
    "Weekly tracking at workstream meeting",
    "Commercial review of contract position",
    "Joint plan agreed with contractor",
]

ACTION_CATEGORIES = {
    "EW": ["Site Prep", "Utilities", "Demolition"],
    "MB": ["Design", "Construction", "Commissioning"],
    "DI": ["Digital", "Cyber"],
    "CM": ["Mobilisation", "Workforce"],
    "EF": ["FM", "Sustainability"],
    "FC": ["Commercial", "Finance"],
    "CE": ["Comms"],
}

ACTION_BANK = {
    "EW": [
        "Confirm survey scope and issue instruction to consultant",
        "Agree access arrangements with site neighbours",
        "Confirm licence application status with highways",
        "Confirm network operator connection date",
        "Validate asbestos register against demolition plan",
    ],
    "MB": [
        "Provide updated cost estimate for revised layout",
        "Circulate draft method statement for review",
        "Issue revised programme showing critical path",
        "Close out design comments on level 3 layouts",
        "Agree waste management route with contractor",
    ],
    "DI": [
        "Provide data migration test results",
        "Confirm cyber assurance timeline with supplier",
        "Share interface specification with EPR supplier",
    ],
    "CM": [
        "Arrange workshop with clinical leads on room layouts",
        "Draft training needs analysis for new building",
        "Confirm workforce model for new outpatient service",
    ],
    "EF": [
        "Share commissioning plan with estates team",
        "Confirm soft FM tender evaluation panel",
        "Agree planned maintenance schedule for handover",
    ],
    "FC": [
        "Review compensation event register with commercial lead",
        "Confirm drawdown profile with finance",
        "Produce options paper for board on car park phasing",
    ],
    "CE": [
        "Update stakeholder map and engagement plan",
        "Prepare briefing note for local councillors",
        "Draft site hoarding messages for review",
    ],
}

UPDATE_BANK = [
    "Survey booked, results to come back to the next meeting.",
    "Draft circulated for comment, responses due end of week.",
    "Awaiting supplier response, chased by email.",
    "Meeting held with contractor, next steps agreed.",
    "Revised programme received and under review.",
    "Cost estimate requested from the quantity surveyor.",
    "Paper submitted to programme board for approval.",
    "Scope confirmed, pricing expected within two weeks.",
    "Workshop held, comments being consolidated.",
    "Application submitted, decision expected next month.",
    "Information shared with estates, feedback pending.",
    "Options narrowed to two, recommendation being drafted.",
]

CLOSE_UPDATES = [
    "Complete, evidence saved to the programme library.",
    "Delivered and confirmed by the chair.",
    "Superseded by board decision, no further work needed.",
]

HOLD_UPDATES = [
    "Paused pending funding decision.",
    "Paused until design freeze is confirmed.",
]

# --------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------


@dataclass
class Project:
    project_id: str
    name: str
    workstream: str
    budget: float
    start: dt.date
    baseline_finish: dt.date
    forecast: float
    forecast_finish: dt.date
    spend: float = 0.0

    def rag(self) -> str:
        cost_var = (self.forecast - self.budget) / self.budget
        slip = (self.forecast_finish - self.baseline_finish).days
        if cost_var > 0.05 or slip > 90:
            return "Red"
        if cost_var > 0.02 or slip > 30:
            return "Amber"
        return "Green"

    def percent_complete(self, as_of: dt.date) -> float:
        if as_of <= self.start:
            return 0.0
        total = (self.forecast_finish - self.start).days
        done = (as_of - self.start).days
        return round(min(1.0, done / total) * 100, 1)


@dataclass
class RaidItem:
    raid_id: str
    type: str  # Risk, Issue, Assumption, Dependency
    workstream: str
    title: str
    owner: str
    raised: dt.date
    inherent_l: int
    inherent_i: int
    residual_l: int
    residual_i: int
    mitigation: str
    last_reviewed: dt.date
    next_review: dt.date
    status: str = "Open"
    closed: dt.date | None = None
    previous_score: int | None = None

    @property
    def inherent_score(self) -> int:
        return self.inherent_l * self.inherent_i

    @property
    def residual_score(self) -> int:
        return self.residual_l * self.residual_i

    def trend(self) -> str:
        if self.previous_score is None or self.previous_score == self.residual_score:
            return "Flat"
        return "Up" if self.residual_score > self.previous_score else "Down"


@dataclass
class Action:
    action_id: str
    workstream: str
    category: str
    raised: dt.date
    description: str
    owner: str
    due: dt.date
    status: str = "New"
    updates: list[str] = field(default_factory=list)
    closed: dt.date | None = None


@dataclass
class Programme:
    as_of: dt.date
    projects: list[Project]
    raid: list[RaidItem]
    actions: list[Action]
    history: list[dict]
    counters: dict[str, int]
    week_events: dict[str, int] = field(default_factory=dict)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def monday_of(day: dt.date) -> dt.date:
    return day - dt.timedelta(days=day.weekday())


FIRST_MEETING = GENESIS + dt.timedelta(days=3)  # governance group meets every other Thursday


def last_meeting(as_of: dt.date) -> dt.date:
    """Most recent meeting strictly before the as-of Monday."""
    fortnights = ((as_of - FIRST_MEETING).days) // 14
    return FIRST_MEETING + dt.timedelta(days=14 * fortnights)


def fmt_update(day: dt.date, owner: str, text: str) -> str:
    return f"{day.strftime('%d.%m.%Y')} - {owner} - {text}"


def next_id(prog: Programme, prefix: str, width: int = 3) -> str:
    prog.counters[prefix] = prog.counters.get(prefix, 0) + 1
    sep = "" if prefix == "A" else "-"
    return f"{prefix}{sep}{prog.counters[prefix]:0{width}d}"


RAID_PREFIX = {"Risk": "R", "Issue": "I", "Assumption": "AS", "Dependency": "D"}


def new_raid(prog: Programme, rng: random.Random, kind: str, raised: dt.date) -> RaidItem:
    open_titles = {r.title for r in prog.raid if r.status == "Open"}
    if kind == "Risk":
        pool = [(ws, t) for ws, ts in RISK_BANK.items() for t in ts if t not in open_titles]
    elif kind == "Issue":
        pool = [(ws, t) for ws, ts in ISSUE_BANK.items() for t in ts if t not in open_titles]
    elif kind == "Assumption":
        pool = [p for p in ASSUMPTION_BANK if p[1] not in open_titles]
    else:
        pool = [p for p in DEPENDENCY_BANK if p[1] not in open_titles]
    if pool:
        ws, title = rng.choice(pool)
    else:  # every base title is live, so raise a variant against a named area
        ws, base = rng.choice([(r.workstream, r.title) for r in prog.raid if r.type == kind and "(" not in r.title])
        variants = [f"{base} ({q})" for q in QUALIFIERS if f"{base} ({q})" not in open_titles]
        title = rng.choice(variants) if variants else f"{base} ({prog.counters.get(RAID_PREFIX[kind], 0) + 1})"
    if kind == "Issue":
        l = 5
        i = rng.choice([2, 3, 3, 4, 4, 5])
    elif kind == "Risk":
        l = rng.choice([2, 3, 3, 4, 4, 5])
        i = rng.choice([2, 3, 4, 4, 5])
    else:
        l = rng.choice([2, 3])
        i = rng.choice([2, 3, 4])
    rl = max(1, l - rng.choice([0, 0, 1]))
    item = RaidItem(
        raid_id=next_id(prog, RAID_PREFIX[kind]),
        type=kind,
        workstream=ws,
        title=title,
        owner=rng.choice(WORKSTREAM_OWNERS[ws]),
        raised=raised,
        inherent_l=l,
        inherent_i=i,
        residual_l=rl,
        residual_i=i,
        mitigation=rng.choice(MITIGATIONS),
        last_reviewed=raised,
        next_review=raised + dt.timedelta(days=14 if rl * i >= HIGH_EXPOSURE else 28),
    )
    prog.raid.append(item)
    return item


def new_action(prog: Programme, rng: random.Random, raised: dt.date) -> Action:
    open_desc = {a.description for a in prog.actions if a.status not in ("Closed",)}
    ws = rng.choice(list(WORKSTREAMS))
    pool = [d for d in ACTION_BANK[ws] if d not in open_desc]
    if not pool:  # this workstream's list is all live, raise against another one
        spare = [(w, d) for w in WORKSTREAMS for d in ACTION_BANK[w] if d not in open_desc]
        if spare:
            ws = rng.choice(spare)[0]
            pool = [d for d in ACTION_BANK[ws] if d not in open_desc]
        else:
            pool = [f"{d} (follow-up)" for d in ACTION_BANK[ws]]
    action = Action(
        action_id=next_id(prog, "A"),
        workstream=ws,
        category=rng.choice(ACTION_CATEGORIES[ws]),
        raised=raised,
        description=rng.choice(pool),
        owner=rng.choice(WORKSTREAM_OWNERS[ws]),
        # Default due date is the next meeting; some owners commit to an earlier or later date.
        due=raised + dt.timedelta(days=rng.choice([7, 10, 14, 14, 14, 14, 21, 28])),
    )
    prog.actions.append(action)
    return action


# --------------------------------------------------------------------------
# Genesis and weekly step
# --------------------------------------------------------------------------


def genesis() -> Programme:
    rng = random.Random(f"{SEED}:genesis")
    projects = []
    for pid, name, ws, budget, start, finish in PROJECTS:
        s = dt.date.fromisoformat(start)
        f = dt.date.fromisoformat(finish)
        p = Project(pid, name, ws, budget, s, f, forecast=budget, forecast_finish=f)
        if GENESIS > s:
            elapsed = (GENESIS - s).days / max(1, (f - s).days)
            p.spend = round(budget * elapsed * rng.uniform(0.85, 1.05), 2)
        projects.append(p)

    prog = Programme(GENESIS, projects, [], [], [], {})
    for kind, count in (("Risk", 32), ("Issue", 4), ("Assumption", 7), ("Dependency", 7)):
        for _ in range(count):
            raised = GENESIS - dt.timedelta(days=rng.randint(7, 180))
            item = new_raid(prog, rng, kind, raised)
            item.last_reviewed = GENESIS - dt.timedelta(days=rng.randint(0, 30))
            item.next_review = item.last_reviewed + dt.timedelta(days=28)
    for _ in range(14):
        raised = last_meeting(GENESIS) - dt.timedelta(days=14 * rng.randint(1, 4))
        a = new_action(prog, rng, raised)
        a.status = "In progress"
        a.due = raised + dt.timedelta(days=14 * rng.randint(1, 3))
        a.updates.insert(0, fmt_update(raised + dt.timedelta(days=14), a.owner, rng.choice(UPDATE_BANK)))
    record_history(prog, new_items=0, closed_items=0)
    return prog


def step(prog: Programme) -> None:
    """Advance the programme by one week."""
    as_of = prog.as_of + dt.timedelta(days=7)
    prog.as_of = as_of
    rng = random.Random(f"{SEED}:{as_of.isoformat()}")
    new_items = closed_items = 0

    # Portfolio. Spend burns, forecasts drift upwards more often than down.
    for p in prog.projects:
        if as_of < p.start:
            continue
        weeks_total = max(1, (p.forecast_finish - p.start).days / 7)
        burn = p.forecast / weeks_total * rng.uniform(0.7, 1.3)
        p.spend = round(min(p.forecast * 0.995, p.spend + burn), 2)
        if rng.random() < 0.08:
            p.forecast = round(p.forecast * (1 + rng.choice([-1, 1, 1, 1]) * rng.uniform(0.002, 0.02)), 2)
        if rng.random() < 0.05:
            p.forecast_finish += dt.timedelta(days=7 * rng.randint(1, 4))

    # RAID.
    for r in prog.raid:
        if r.status != "Open":
            continue
        r.previous_score = r.residual_score
        due = r.next_review <= as_of
        if (due and rng.random() < 0.65) or (not due and rng.random() < 0.12):
            roll = rng.random()
            if roll < 0.34:
                r.residual_l = max(1, r.residual_l - 1)
            elif roll < 0.46:
                r.residual_l = min(5, r.residual_l + 1)
            if rng.random() < 0.05:
                r.residual_i = max(1, min(5, r.residual_i + rng.choice([-1, 1])))
            r.last_reviewed = as_of
            r.next_review = as_of + dt.timedelta(days=14 if r.residual_score >= HIGH_EXPOSURE else 28)
        close_p = {
            "Risk": 0.05 if r.residual_score <= 6 else 0.012,
            "Issue": 0.08,
            "Assumption": 0.03,
            "Dependency": 0.04,
        }[r.type]
        if rng.random() < close_p:
            r.status, r.closed = "Closed", as_of
            closed_items += 1
        elif r.type == "Risk" and r.residual_score >= HIGH_EXPOSURE and rng.random() < 0.03:
            r.status, r.closed = "Closed", as_of
            r.mitigation = "Materialised, now tracked as an issue"
            closed_items += 1
            issue = new_raid(prog, rng, "Issue", as_of)
            issue.workstream, issue.owner = r.workstream, r.owner
            new_items += 1

    for _ in range(rng.choice([0, 1, 1, 1, 2, 2])):
        new_raid(prog, rng, "Risk", as_of)
        new_items += 1
    for kind, p in (("Issue", 0.2), ("Assumption", 0.08), ("Dependency", 0.08)):
        if rng.random() < p:
            new_raid(prog, rng, kind, as_of)
            new_items += 1

    # Actions. The governance group meets fortnightly; most movement happens then.
    mdate = last_meeting(as_of)
    meeting = mdate >= as_of - dt.timedelta(days=7)
    for a in prog.actions:
        if a.status == "Closed":
            continue
        if not meeting:
            if rng.random() < 0.08 and a.status != "On hold":
                a.updates.insert(0, fmt_update(as_of - dt.timedelta(days=rng.randint(1, 4)), a.owner, rng.choice(UPDATE_BANK)))
                a.status = "In progress"
            continue
        roll = rng.random()
        if a.status == "On hold":
            if roll < 0.35:
                a.status = "In progress"
                a.updates.insert(0, fmt_update(mdate, a.owner, "Restarted following board decision."))
        elif a.status == "In progress" and roll < 0.3:
            a.status, a.closed = "Closed", mdate
            a.updates.insert(0, fmt_update(mdate, a.owner, rng.choice(CLOSE_UPDATES)))
        elif 0.3 <= roll < 0.32:
            a.status = "On hold"
            a.updates.insert(0, fmt_update(mdate, a.owner, rng.choice(HOLD_UPDATES)))
        elif roll < 0.85:
            a.status = "In progress"
            a.updates.insert(0, fmt_update(mdate, a.owner, rng.choice(UPDATE_BANK)))
            if a.due <= mdate and rng.random() < 0.75:
                a.due = mdate + dt.timedelta(days=14)
    if meeting:
        for _ in range(rng.randint(2, 5)):
            new_action(prog, rng, mdate)

    record_history(prog, new_items, closed_items)


def record_history(prog: Programme, new_items: int, closed_items: int) -> None:
    open_raid = [r for r in prog.raid if r.status == "Open"]
    risks = [r for r in open_raid if r.type == "Risk"]
    live_actions = [a for a in prog.actions if a.status not in ("Closed",)]
    prog.week_events = {"new": new_items, "closed": closed_items}
    prog.history.append(
        {
            "as_of": prog.as_of.isoformat(),
            "open_risks": len(risks),
            "open_issues": sum(1 for r in open_raid if r.type == "Issue"),
            "high_exposure_risks": sum(1 for r in risks if r.residual_score >= HIGH_EXPOSURE),
            "avg_residual_score": round(sum(r.residual_score for r in risks) / max(1, len(risks)), 2),
            "raid_raised": new_items,
            "raid_closed": closed_items,
            "open_actions": len(live_actions),
            "overdue_actions": sum(1 for a in live_actions if a.due < prog.as_of and a.status != "On hold"),
            "budget_gbp_m": round(sum(p.budget for p in prog.projects), 2),
            "forecast_gbp_m": round(sum(p.forecast for p in prog.projects), 2),
        }
    )
    del prog.history[:-HISTORY_WEEKS]


def build(as_of: dt.date) -> Programme:
    as_of = monday_of(as_of)
    if as_of < GENESIS:
        raise SystemExit(f"as-of {as_of} is before genesis {GENESIS}")
    prog = genesis()
    while prog.as_of < as_of:
        step(prog)
    return prog


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------


def d(day: dt.date | None) -> str:
    return day.isoformat() if day else ""


def band(score: int) -> str:
    if score >= HIGH_EXPOSURE:
        return "High"
    if score >= MEDIUM_EXPOSURE:
        return "Medium"
    return "Low"


def to_csv(rows: list[dict]) -> str:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def tables(prog: Programme) -> dict[str, list[dict]]:
    as_of = prog.as_of
    mdate = last_meeting(as_of)
    next_meeting = mdate + dt.timedelta(days=14)

    portfolio = [
        {
            "as_of": d(as_of),
            "project_id": p.project_id,
            "project": p.name,
            "workstream": WORKSTREAMS[p.workstream],
            "budget_gbp_m": f"{p.budget:.2f}",
            "forecast_gbp_m": f"{p.forecast:.2f}",
            "spend_to_date_gbp_m": f"{p.spend:.2f}",
            "variance_gbp_m": f"{p.forecast - p.budget:.2f}",
            "start": d(p.start),
            "baseline_finish": d(p.baseline_finish),
            "forecast_finish": d(p.forecast_finish),
            "slip_days": (p.forecast_finish - p.baseline_finish).days,
            "percent_complete": f"{p.percent_complete(as_of):.1f}",
            "rag": p.rag() if as_of >= p.start else "Not started",
        }
        for p in prog.projects
    ]

    raid = [
        {
            "as_of": d(as_of),
            "raid_id": r.raid_id,
            "type": r.type,
            "workstream": WORKSTREAMS[r.workstream],
            "title": r.title,
            "owner_role": OWNERS[r.owner],
            "raised": d(r.raised),
            "inherent_likelihood": r.inherent_l,
            "inherent_impact": r.inherent_i,
            "inherent_score": r.inherent_score,
            "residual_likelihood": r.residual_l,
            "residual_impact": r.residual_i,
            "residual_score": r.residual_score,
            "exposure_band": band(r.residual_score),
            "trend": r.trend() if r.status == "Open" else "",
            "mitigation": r.mitigation,
            "last_reviewed": d(r.last_reviewed),
            "next_review": d(r.next_review),
            "review_overdue": "Yes" if r.status == "Open" and r.next_review < as_of else "No",
            "status": r.status,
            "closed": d(r.closed),
        }
        for r in prog.raid
    ]

    actions = []
    for a in prog.actions:
        live = a.status != "Closed"
        actions.append(
            {
                "as_of": d(as_of),
                "action_id": a.action_id,
                "workstream": WORKSTREAMS[a.workstream],
                "category": a.category,
                "raised": d(a.raised),
                "description": a.description,
                "updates": "\n".join(a.updates),
                "owner": a.owner,
                "owner_role": OWNERS[a.owner],
                "due": d(a.due),
                "status": a.status,
                "overdue": "Yes" if live and a.status != "On hold" and a.due < as_of else "No",
                "due_before_next_meeting": "Yes" if live and mdate < a.due < next_meeting else "No",
                "closed": d(a.closed),
            }
        )

    return {
        "portfolio": portfolio,
        "raid_log": raid,
        "actions": actions,
        "weekly_history": prog.history,
    }


def snapshot(prog: Programme) -> dict:
    as_of = prog.as_of
    open_raid = [r for r in prog.raid if r.status == "Open"]
    risks = [r for r in open_raid if r.type == "Risk"]
    live = [a for a in prog.actions if a.status != "Closed"]
    hist = prog.history[-12:]
    prev = prog.history[-2] if len(prog.history) > 1 else prog.history[-1]
    now = prog.history[-1]
    top = sorted(risks, key=lambda r: (-r.residual_score, r.raid_id))[:5]
    budget = sum(p.budget for p in prog.projects)
    forecast = sum(p.forecast for p in prog.projects)
    return {
        "programme": PROGRAMME,
        "as_of": as_of.isoformat(),
        "iso_week": as_of.isocalendar().week,
        "weeks_running": (as_of - GENESIS).days // 7,
        "last_meeting": last_meeting(as_of).isoformat(),
        "next_meeting": (last_meeting(as_of) + dt.timedelta(days=14)).isoformat(),
        "portfolio": {
            "projects": len(prog.projects),
            "budget_gbp_m": round(budget, 1),
            "forecast_gbp_m": round(forecast, 1),
            "variance_gbp_m": round(forecast - budget, 1),
            "variance_pct": round((forecast - budget) / budget * 100, 2),
            "rag": {k: sum(1 for p in prog.projects if as_of >= p.start and p.rag() == k) for k in ("Green", "Amber", "Red")},
            "not_started": sum(1 for p in prog.projects if as_of < p.start),
        },
        "raid": {
            "open_by_type": {k: sum(1 for r in open_raid if r.type == k) for k in ("Risk", "Issue", "Assumption", "Dependency")},
            "risk_bands": {k: sum(1 for r in risks if band(r.residual_score) == k) for k in ("High", "Medium", "Low")},
            "reviews_overdue": sum(1 for r in open_raid if r.next_review < as_of),
            "raised_this_week": now["raid_raised"],
            "closed_this_week": now["raid_closed"],
            "open_risks_delta": now["open_risks"] - prev["open_risks"],
            "high_exposure_delta": now["high_exposure_risks"] - prev["high_exposure_risks"],
            "top_risks": [
                {
                    "id": r.raid_id,
                    "workstream": WORKSTREAMS[r.workstream],
                    "title": r.title,
                    "score": r.residual_score,
                    "trend": r.trend(),
                    "owner_role": OWNERS[r.owner],
                }
                for r in top
            ],
        },
        "actions": {
            "open": sum(1 for a in live if a.status in ("New", "In progress")),
            "on_hold": sum(1 for a in live if a.status == "On hold"),
            "overdue": now["overdue_actions"],
            "overdue_delta": now["overdue_actions"] - prev["overdue_actions"],
            "closed_total": sum(1 for a in prog.actions if a.status == "Closed"),
            "due_before_next_meeting": sum(1 for a in live if last_meeting(as_of) < a.due < last_meeting(as_of) + dt.timedelta(days=14)),
            "attention": [
                {
                    "id": a.action_id,
                    "workstream": WORKSTREAMS[a.workstream],
                    "description": a.description,
                    "owner_role": OWNERS[a.owner],
                    "due": a.due.isoformat(),
                    "status": a.status,
                    "flag": "Overdue" if a.due < as_of else "Due before next meeting",
                    "latest": a.updates[0] if a.updates else "",
                }
                for a in sorted(
                    (a for a in live if a.status != "On hold" and (a.due < as_of or a.due < last_meeting(as_of) + dt.timedelta(days=14))),
                    key=lambda a: (a.due, a.action_id),
                )[:6]
            ],
        },
        "history": [
            {"as_of": h["as_of"], "open_risks": h["open_risks"], "high_exposure_risks": h["high_exposure_risks"], "overdue_actions": h["overdue_actions"]}
            for h in hist
        ],
        "files": ["portfolio.csv", "raid_log.csv", "actions.csv", "weekly_history.csv"],
    }


def write_if_changed(path: Path, text: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def write_outputs(prog: Programme, root: Path) -> list[Path]:
    changed = []
    data_dir = root / "public" / "data"
    for name, rows in tables(prog).items():
        p = data_dir / f"{name}.csv"
        if write_if_changed(p, to_csv(rows)):
            changed.append(p)
    snap = root / "src" / "data" / "synthetic" / "snapshot.json"
    if write_if_changed(snap, json.dumps(snapshot(prog), indent=2) + "\n"):
        changed.append(snap)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.datetime.now(dt.timezone.utc).date())
    parser.add_argument("--out", type=Path, default=ROOT, help="repo root to write into")
    args = parser.parse_args()
    prog = build(args.as_of)
    changed = write_outputs(prog, args.out)
    snap = snapshot(prog)
    print(f"{PROGRAMME}, as at {prog.as_of} (week {snap['weeks_running']})")
    print(f"  open risks {snap['raid']['open_by_type']['Risk']}, high exposure {snap['raid']['risk_bands']['High']}, "
          f"overdue actions {snap['actions']['overdue']}, forecast variance £{snap['portfolio']['variance_gbp_m']}m")
    print(f"  {len(changed)} file(s) changed" + "".join(f"\n    {c.relative_to(args.out)}" for c in changed))


if __name__ == "__main__":
    main()
