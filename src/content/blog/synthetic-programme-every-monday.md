---
title: 'My portfolio runs on a hospital programme that does not exist'
description: 'Why I built a synthetic £490m programme that moves forward every Monday, and how it keeps every dashboard on this site honest without a single line of real data.'
pubDate: 2026-11-04
tags: ['Python', 'PMO', 'Automation']
draft: false
---

Everything I build at work belongs to the Trust. That is the right rule, and it leaves anyone in a PMO role with a portfolio problem. You can show screenshots with everything blurred, which proves nothing. Or you can build on a dummy dataset, which proves a little more, until someone notices it is the same forty rows every time they look.

Real PMO data has a property that dummy data almost never has. It moves. Risks get reviewed, or do not, and go stale. Actions roll forward from one meeting to the next. Forecasts creep. A dashboard that only ever sees a frozen dataset has never had to deal with any of that.

So I built a programme that moves.

## Halden Vale

The Halden Vale Health Campus Programme is nine projects across seven workstreams with a £490m budget. Its start date, inside the fiction, is 4 May 2026. Every Monday morning a GitHub Action moves it forward one more week and commits the result. Cloudflare sees the commit and rebuilds this site. The [live snapshot](/projects/portfolio-dashboard/) on the index changes without me touching it, and the four CSVs it is built from are published at [/data/](/data/raid_log.csv) for anything else to read, including Power BI.

None of it is real. The owners are roles, not people. The risks are the kind every hospital programme carries, written generically.

## Three rules

**Same week, same answer.** The script does not keep state between runs. It replays the whole programme from 4 May, one week at a time, with each week's random generator seeded by the date. Run it twice for the same Monday and the files are byte-identical. Anyone can rebuild any past week and get exactly what was published.

**Forward only.** Next week's history is this week's history plus one row. Nothing that has been published is ever rewritten, which is the property you want from any reporting dataset and rarely get.

**Behave like a real log.** A risk due for review usually gets reviewed, but not always, which is how overdue reviews appear. Mitigation tends to pull likelihood down. A high-exposure risk can materialise and close into a new issue. Forecasts drift upwards more often than down. Actions move on a fortnightly meeting cycle, with dated and initialled updates newest first, and a due date that lands before the next meeting gets flagged.

## Why it matters for the dashboards

A dashboard built against a frozen dataset has never had to handle a risk that closes, an action that slips twice, or a week where nothing happens. The synthetic programme throws all of that at the [PMO central portfolio dashboard](/projects/portfolio-dashboard/) every week, and the tests in the repository stop a bad week from ever being committed.

The source is in the [site repository](https://github.com/mahemishrapmo-hub/new-portfolio/tree/main/scripts/synthetic). It is standard library Python, so it runs anywhere with nothing to install.
