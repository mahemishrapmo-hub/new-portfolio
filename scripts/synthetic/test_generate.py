"""Run with: python -m unittest discover -s scripts/synthetic -p 'test_*.py'"""

import csv
import datetime as dt
import io
import tempfile
import unittest
from pathlib import Path

import generate as g

WEEK = dt.date(2026, 11, 2)


class EngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prog = g.build(WEEK)
        cls.tables = g.tables(cls.prog)

    def test_deterministic(self):
        again = g.tables(g.build(WEEK))
        for name, rows in self.tables.items():
            self.assertEqual(g.to_csv(rows), g.to_csv(again[name]), name)

    def test_snaps_to_monday(self):
        self.assertEqual(g.build(dt.date(2026, 11, 4)).as_of, WEEK)

    def test_forward_only(self):
        """Next week's file is this week's history plus one row, never a rewrite."""
        nxt = g.build(WEEK + dt.timedelta(days=7)).history
        self.assertEqual(nxt[:-1], self.prog.history[-(len(nxt) - 1):])

    def test_ids_unique(self):
        for name, key in (("raid_log", "raid_id"), ("actions", "action_id"), ("portfolio", "project_id")):
            ids = [r[key] for r in self.tables[name]]
            self.assertEqual(len(ids), len(set(ids)), name)

    def test_scores_in_range(self):
        for r in self.tables["raid_log"]:
            for k in ("inherent_likelihood", "inherent_impact", "residual_likelihood", "residual_impact"):
                self.assertTrue(1 <= int(r[k]) <= 5, (r["raid_id"], k))
            self.assertEqual(int(r["residual_score"]), int(r["residual_likelihood"]) * int(r["residual_impact"]))

    def test_closed_items_have_dates(self):
        for r in self.tables["raid_log"] + self.tables["actions"]:
            self.assertEqual(r["status"] == "Closed", bool(r["closed"]), r)

    def test_no_duplicate_open_titles(self):
        titles = [r["title"] for r in self.tables["raid_log"] if r["status"] == "Open"]
        self.assertEqual(len(titles), len(set(titles)))

    def test_no_duplicate_live_actions(self):
        live = [a.description for a in self.prog.actions if a.status != "Closed"]
        self.assertEqual(len(live), len(set(live)))

    def test_nothing_dated_after_as_of(self):
        for a in self.prog.actions:
            for line in a.updates:
                day = dt.datetime.strptime(line[:10], "%d.%m.%Y").date()
                self.assertLessEqual(day, self.prog.as_of, line)

    def test_updates_newest_first(self):
        for a in self.prog.actions:
            days = [dt.datetime.strptime(u[:10], "%d.%m.%Y").date() for u in a.updates]
            self.assertEqual(days, sorted(days, reverse=True), a.action_id)

    def test_csv_round_trips(self):
        for name, rows in self.tables.items():
            parsed = list(csv.DictReader(io.StringIO(g.to_csv(rows))))
            self.assertEqual(len(parsed), len(rows), name)

    def test_write_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = g.write_outputs(self.prog, Path(tmp))
            second = g.write_outputs(self.prog, Path(tmp))
            self.assertEqual(len(first), 5)
            self.assertEqual(second, [])


if __name__ == "__main__":
    unittest.main()
