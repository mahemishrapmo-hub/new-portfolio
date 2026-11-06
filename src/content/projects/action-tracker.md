---
ref: PRJ-03
title: Governance action tracker and dashboard
status: live
order: 3
featured: true
summary: The fortnightly action tracker for an enabling works governance group, built so every row carries its own audit trail and the chair sees what lands before the next meeting.
tags: ['Excel', 'Power Query', 'Power BI', 'PMO']
stack: ['Excel', 'Power Query', 'Power BI', 'SharePoint']
data: The live tracker runs inside the programme. The public version runs on the synthetic actions table.
updated: 2026-11-02
caseStudy: action-tracker
snapshot: actions
links:
  - label: Download the synthetic actions CSV
    href: /data/actions.csv
---

## What it does

The enabling works governance group on the programme meets every fortnight. After each meeting I turn the record of the discussion into updates on the master action tracker, and the chair reviews it before it goes any wider.

The value is not the spreadsheet. It is the set of rules that make the spreadsheet trustworthy when twenty people are reading it.

## The rules

- **One row per action**, sequential IDs, never reused.
- **Updates newest first.** Each line is dated and initialled, so the cell is its own audit trail and nobody has to ask what happened last time.
- **Status lives in its own column** with a fixed colour for each state. It is never written into the narrative.
- **Dates live in their own column too.** A due date turns red when it falls after this meeting but before the next one, so the chair sees what will land before the group meets again.
- **A new action needs one owner and one deliverable.** Escalations, chases and clarifications fold into the existing action as an update rather than spawning a new row.
- **Ownership follows the work.** If the meeting shows someone else driving an action, the owner column changes, whatever the original description says.
- **Short updates.** Ten to twenty words, the fact and the next physical step, nothing else.

## The dashboard layer

The tracker answers "what is the status of A042". The dashboard answers the questions the chair actually asks across the whole list. Which owners are carrying the most open actions, which actions have been rolled forward meeting after meeting, and what is overdue. The public version below runs on the synthetic actions table, which follows the same rules.
