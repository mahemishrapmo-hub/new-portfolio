---
ref: PRJ-02
title: PMO central portfolio dashboard
status: in-progress
order: 2
featured: true
summary: One view of every project, risk, action and pound across a PMO. Built in the open on a synthetic programme that moves forward every Monday.
tags: ['Power BI', 'DAX', 'PMO', 'Python']
stack: ['Power BI', 'DAX', 'Power Query', 'Python', 'GitHub Actions']
data: Synthetic programme regenerated every Monday. The benchmark layer uses public NISTA major projects data, published under the Open Government Licence v3.0.
updated: 2026-11-02
snapshot: portfolio
links:
  - label: Download the RAID log CSV
    href: /data/raid_log.csv
  - label: How the data is generated, PRJ-06
    href: /projects/synthetic-data-engine/
---

## The problem it solves

A PMO usually reports from four places at once. The portfolio register says what each project costs and when it finishes. The RAID log says what might go wrong. The action tracker says who promised what. The finance report says where the money went. Each is maintained separately, so the board pack is stitched together by hand every cycle and is out of date by the time it is read.

The central dashboard puts all four into one model with shared dimensions, so a question like "which workstream has the most high-exposure risks, the most overdue actions and the biggest forecast overspend" is one click, not an afternoon.

## How it is built

1. **Data.** The [synthetic programme engine](/projects/synthetic-data-engine/) runs a fictional £490m hospital programme forward one week every Monday and publishes four CSVs to [/data/](/data/raid_log.csv) on this site.
2. **Ingest.** Power BI reads those files straight from the web, so a scheduled refresh picks up the new week without a gateway or a manual upload.
3. **Model.** A star schema with four fact tables (portfolio, RAID log, actions, weekly history) sharing workstream, owner role and date dimensions.
4. **Pages.** Portfolio overview, RAID exposure, mitigation journey, action ageing, and budget against forecast.
5. **Benchmark.** NISTA publishes a Red, Amber or Green delivery confidence rating for every project on the Government Major Projects Portfolio each year. The overview sets the synthetic portfolio's mix against the published one, so the numbers have a real-world reference point.

## Status

The data engine is live and the snapshot below is rebuilt from it on every deploy. The Power BI report pages are in build on personal hardware. The `.pbix` and a walkthrough of the model and measures will be published here when they are ready.
