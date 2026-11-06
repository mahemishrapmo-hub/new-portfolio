---
ref: PRJ-06
title: Synthetic programme data engine
status: live
order: 6
featured: true
summary: A Python engine that runs a fictional £490m hospital programme forward one week every Monday, so every dashboard on this site has moving data and none of it is real.
tags: ['Python', 'Automation', 'GitHub Actions']
stack: ['Python standard library', 'GitHub Actions', 'CSV']
data: Entirely synthetic. Every project, risk, owner and figure is invented.
updated: 2026-11-02
links:
  - label: View the source
    href: https://github.com/mahemishrapmo-hub/new-portfolio/tree/main/scripts/synthetic
  - label: Weekly history CSV
    href: /data/weekly_history.csv
---

## Why it exists

Anything I build at work stays at work. That leaves a portfolio with two bad options, screenshots with everything blurred, or a static dummy dataset that never changes and fools nobody. A real PMO dataset moves. Risks get reviewed or go stale, actions roll forward, forecasts creep. So I built a programme that moves.

## How it works

The Halden Vale Health Campus Programme is nine projects across seven workstreams with a £490m budget. Its fictional start date is 4 May 2026. Every Monday at 06:30 a GitHub Action replays it from that date to the current week and commits the result. Cloudflare picks up the commit and rebuilds this site, so the [live snapshot](/projects/portfolio-dashboard/) and the CSVs move on their own.

- **Deterministic.** Each week's random generator is seeded by the date. The same week always produces byte-identical files, so anyone can rebuild any past week and get what was published.
- **Forward only.** Next week's history is this week's history plus one row. Nothing published is ever rewritten.
- **Behaves like a real log.** Risks due for review usually get reviewed, and sometimes do not, which is how overdue reviews appear. Mitigation tends to pull likelihood down. A high-exposure risk can materialise and close into a new issue. Forecasts drift upwards more often than down.
- **Follows a real governance rhythm.** The action tracker moves on a fortnightly meeting cycle, with dated and initialled updates newest first, and a due date flagged when it lands before the next meeting.
- **Owners are roles, never people.**

## What it publishes

| File | One row per | Used for |
| --- | --- | --- |
| [portfolio.csv](/data/portfolio.csv) | Project | Budget, forecast, spend, schedule slip, RAG |
| [raid_log.csv](/data/raid_log.csv) | RAID item | Inherent and residual scores, trend, review status |
| [actions.csv](/data/actions.csv) | Action | Owner, due date, status, full update history |
| [weekly_history.csv](/data/weekly_history.csv) | Week | Trend lines without snapshot tables |

## Tested

Eleven unit tests run before every weekly commit and on every pull request. They check determinism, that history only ever grows, that IDs are unique, that scores stay on the five by five grid, that no update is dated after the as-at date, and that updates stay newest first. If a test fails the commit never happens.
