---
ref: CS-01
title: Replacing a static RAID spreadsheet with a dashboard a board can interrogate
summary: A £1B+ redevelopment programme's RAID log could list risks but could not say what had changed. A Power BI prototype on dummy data was endorsed, taken forward, and earned named ownership of RAID reporting.
order: 1
role: PMO and Data Analyst
period: '2025 to 2026'
pubDate: 2026-11-04
tags: ['Power BI', 'DAX', 'PMO']
project: raid-dashboard
outcomes:
  - value: '£1B+'
    label: programme covered by the reporting
  - value: '2 clicks'
    label: from a headline number to the underlying item
  - value: 'Named'
    label: ownership of RAID reporting in the PMO operating model
---

## Context

The Hinchingbrooke Hospital Redevelopment Programme is a £1B+ scheme delivered under an NEC contract. Like most programmes its RAID log lived in a spreadsheet, maintained by several people, read by many more.

## Problem

A flat list answers "what risks do we have". A Programme Board asks different questions. What changed since last month. Which risks are getting worse despite mitigation. Where ownership is concentrated. What the aggregate exposure is by workstream. Answering those from a spreadsheet meant someone rebuilding a summary by hand every cycle, and the summary was stale the moment it was pasted into a pack.

## Approach

- **Prototype on dummy data first.** Building on live programme data was never an option for a demo, so the first job was a dataset that behaved like a real RAID log without containing anything real. It meant the prototype could be shown to anyone without a single redaction.
- **Two pages, two questions.** Current Position for triage today. Mitigation Journey to judge whether risk management is real or theatre.
- **All logic in measures.** Base measures for counts and scores, time intelligence over snapshot dates, and inherent against residual comparisons. Every figure on the page traces back to one definition.

## Outcome

The Deputy Head of PMO endorsed the prototype and it was taken forward, with named ownership of RAID reporting written into the PMO operating model. Version 2 is now in build, reading the RAID log live from SharePoint, adding board-safe views and a meeting brief written by DAX from the live numbers.

## Lesson

Reporting earns trust when the reader can get from a headline number to the item behind it in two clicks. No static document can offer that, however well it is formatted.
