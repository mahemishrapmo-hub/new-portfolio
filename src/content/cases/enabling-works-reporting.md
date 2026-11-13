---
ref: CS-04
title: Redesigning project reporting for an NHS enabling works programme
summary: Each enabling works project reported fortnightly on two narrative slides, so nobody could see at a glance whether a project was safe, on budget or on time. A metrics-led template, drafted with the workstream chair, puts health and safety, finance, programme, change control and risk on the page.
order: 4
role: PMO Analyst
period: '2026'
pubDate: 2026-11-13
tags: ['PMO', 'Reporting design', 'Risk management', 'PowerPoint', 'Power BI']
outcomes:
  - value: '11'
    label: live projects covered by one metrics-led template
  - value: '6'
    label: health and safety measures, reported first
  - value: '1'
    label: workstream risk page in place of eleven
  - value: '+1'
    label: slide added to the pack, everything else stays the same size
---

## Context

- **Programme.** Enabling works workstream of a £1bn+ NHS hospital redevelopment programme, 11 live projects.
- **Audience.** Fortnightly workstream delivery group, with a view to programme leadership reporting.
- **Tools.** PowerPoint, Power BI, Excel.
- **Status.** Template drafted and reviewed with the workstream chair. Second iteration in progress ahead of a trial.

All figures shown in this case study are sample data. Project names, people and programme data are left out on purpose.

## The problem

Each enabling works project reported fortnightly on two slides. The format had grown over time and was mostly narrative.

* **Page 1** held an executive summary, deliverables this period and next, information required and decisions required.
* **Page 2** held scope, upcoming meetings, interdependencies, assumptions, project value, a set of governance gate statuses (PID agreed, PEP agreed, justification form agreed), a milestone table and a risk table squeezed in at the bottom.

That created six problems.

1. **Very little could be measured.** There was no committed spend, forecast, contingency or schedule movement. To find out whether a project was on time and on budget you had to read paragraphs.
2. **Static rows repeated every cycle.** Once a PID or PEP is agreed, saying so every fortnight tells the meeting nothing.
3. **No health and safety data** for projects with contractors on site.
4. **Change requests and decisions lived in free text,** so neither could be searched or traced later.
5. **Risk had no workstream view.** Each project's risks sat at the bottom of its own slide, so nobody could see the overall picture.
6. **Meetings ran long** on narrative updates, and attention dropped.

## Requirements

I gathered these with the workstream chair over two working sessions.

* Remove static governance gate rows.
* Add finance, covering approved budget, committed spend, forecast spend and % of contingency used.
* Add programme, covering completion against the agreed baseline and how far it has moved.
* Report health and safety first, for projects on site.
* Capture change requests, both upcoming and approved.
* Record decisions so they can feed a central decision log.
* Summarise risk as identified, significant, closed and transferred to issues, with the meeting focused on emerging and high risks.
* **Constraint.** Improve reporting now without a wholesale change, because longer-term programme reporting was being designed in parallel.

## What I built

A three-part template that matches the existing deck's layout, fonts and RAGB colours, so the slides paste straight into the live pack.

### Page 1. Project health

* **Header.** Project manager, workstream lead, reporting period, previous and current RAGB, and the RAGB key.
* **Health and safety, six measures.** Lost time accident frequency rate (target below 0.3), RIDDOR reportable incidents, lost time incidents, incidents requiring action, near misses, and safety conversations and toolbox talks. Each shows this period with the cumulative figure in brackets.
* **Finance, four measures.** Approved budget, committed spend as a share of budget, forecast outturn, and variance to budget.
* **Programme, four measures.** Baseline completion, last reported date, current forecast, and movement against baseline, with movement since the last report underneath.
* **Contingency health.** A native chart comparing % of contingency used with % of programme time elapsed, plus a flag when drawdown runs ahead of time.
* **Narrative,** cut down to an executive summary and deliverables this period and next.

### Page 2. Delivery and governance

* **Project context.** Scope, interdependencies, assumptions, status of fees, and a one-line count of the project's open and significant risks.
* **Milestones.** SOC baseline, last reported, current forecast and a new movement column.
* **Information required and decisions required,** side by side to save space.
* **Change requests (new).** Reference, description, stage, cost impact, time impact, funding source, approval forum, date and status.
* **Decisions made this period (new).** Each decision carries a decision log reference.

### Workstream risk page

* **Six summary measures.** Open risks, significant risks, new this period, closed since last update, transferred to issues, and open issues.
* **Open risks by project,** as a stacked bar chart splitting significant from other risks.
* **Emerging risks, high risk updates and issues,** each with a project column. High risk updates show pre-mitigation score, progress this period, current score and trend.

### Build standards

* Same 16:9 size, typeface and colour palette as the existing pack.
* Native PowerPoint charts that update through Edit Data, not pasted images.
* Every shape named, so values can later be filled automatically.
* Speaker notes on each slide summarising what changed and why.

## Key design decisions

**Health and safety goes first.** On a live construction site, safety outranks cost and time, and the order of the page should say so. The row only applies to projects with contractors on site.

**Contingency is compared with time, not just budget.** A project can sit comfortably within budget while burning through its contingency far too early. Putting % of contingency used next to % of programme time elapsed shows that months before it turns into an overspend.

**Two kinds of schedule movement.** Movement against baseline shows how far a project has drifted in total. Movement since the last report shows whether it is still getting worse. A project that slipped 13 weeks some time ago and has since held steady needs a different conversation from one that slipped 9 weeks in the last fortnight.

**Decisions get a log reference.** The slide becomes a view of the decision log rather than the record itself, so every decision can be traced by meeting, date and approver when assurance asks.

**One risk page, not eleven.** A risk page per project would have added 11 slides and more work for every project manager each cycle. A single workstream page adds one slide, and PMO fills it from the RAID dashboard. The project section stays at 22 slides.

**Each period's pack is frozen.** A pack is a governance record of what the meeting saw on that date. Live links get refreshed at the reporting cut-off, then broken, and the pack goes out as a PDF, so past packs never change when the source data does.

## Data and automation design

This part is designed and agreed in principle, but not yet built.

* Source the risk measures from the RAID log through Power BI, or through Excel Power Query where Power BI isn't available.
* Calculate period measures against a reporting cut-off date rather than today's date, so any past period can be reproduced exactly.
* Make sure the RAID log captures date raised, date closed, status change date, score, project and latest update. Without those fields, measures such as "closed since last update" can't be automated.
* Use a scheduled flow to add each period's values to a history table at the cut-off. That freezes every period in the data and builds trend reporting at no extra cost.

## Before and after

|Area|Before|After|
|-|-|-|
|Finance|Project value only|Budget, committed, forecast, variance and contingency used|
|Schedule|Milestone dates|Baseline, last reported, forecast, and movement both ways|
|Health and safety|Not reported|Six measures, first on the page|
|Governance gates|PID, PEP and justification status every cycle|Removed|
|Change control|Free text|Dedicated table with cost, time and funding|
|Decisions|Free text|Logged with references|
|Risk|A table at the bottom of each project|Workstream risk page plus a per-project count|
|Pack size|2 slides per project|2 slides per project, plus 1 risk page|

## Feedback and iteration

The workstream chair reviewed the draft and asked for the following in the second iteration.

* **Commercial block.** Contract award status, number of compensation events and number of early warning notices.
* **Deliverables moved** to free up space for measures.
* **Stakeholder engagement RAG** in place of upcoming meetings and assumptions. Assumptions move to the RAID log, where they belong.
* **Risk split by level.** A summary strip on each project's pages. The workstream view moves to an enabling works front page with an overall RAG health check across scope, risk, schedule and spend.
* **Trend arrows** inside the score cell, coloured by direction, replacing trend words.

## Status and next steps

The second iteration is in progress. Next, the template is trialled at an internal workstream meeting and submitted as a shadow update to programme leadership for feedback, subject to PMO sign-off.

## What I learned

* **Executive reporting is about what's stopping a project getting to green,** not a list of activity. Every element earns its place by answering that.
* **Design the data before the dashboard.** Automation depends entirely on what the source log records.
* **A report pack is a governance record.** Live data is useful for building it but dangerous for circulating it.
