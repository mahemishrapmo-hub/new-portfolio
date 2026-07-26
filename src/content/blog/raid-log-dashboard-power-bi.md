---
title: 'Building a RAID log dashboard in Power BI for a £1B NHS programme'
description: 'Why static RAID spreadsheets fail on large programmes, and how I prototyped an interactive alternative on synthetic data.'
pubDate: 2026-07-26
tags: ['Power BI', 'PMO', 'DAX']
draft: false
---

Every large programme has a RAID log. Most of them live in a spreadsheet, and most of those spreadsheets fail at the one thing a RAID log exists to do, which is tell decision makers what needs their attention right now.

I support the Hinchingbrooke Hospital Redevelopment Programme, a £1B+ NEC scheme, and I built a Power BI prototype to replace static RAID tracking. This post covers the reasoning and the build, not the programme's actual risk data. Everything shown was built on a synthetic dataset created for exactly that purpose.

## The problem with the spreadsheet

A RAID spreadsheet is a flat list. It answers "what risks do we have" but struggles with the questions a Programme Board actually asks.

- What changed since last month?
- Which risks are trending the wrong way despite mitigation?
- Where is ownership concentrated, and is anyone overloaded?
- What is the aggregate exposure by workstream?

Answering those from a flat list means someone manually building a summary every reporting cycle. That summary is stale the moment it is pasted into a slide deck.

## Designing on synthetic data

Prototyping on live programme data was never an option, so the first task was building a dataset that behaved like a real RAID log without containing anything real. I generated a themed synthetic dataset with realistic distributions, risks skewed towards a handful of workstreams, a plausible mix of severities, and mitigation histories that moved over time. A prototype you can demo to anyone without a single redaction is a prototype that actually gets seen.

## Two pages, two questions

The report deliberately has only two pages, because a dashboard with ten pages is a spreadsheet with extra steps.

**Current Position** answers "where are we today". Open items by severity and workstream, ownership distribution, and the items that have breached or are approaching review dates.

**Mitigation Journey** answers "is our management working". Movement of risk scores over time, items whose scores have not moved despite active mitigation, and the gap between inherent and residual exposure.

The split matters. Boards need the first page for triage and the second to judge whether the programme's risk management is real or theatre.

## The DAX layer

The measures behind the report follow a few patterns that generalise to any RAID build.

- Base measures for counts and scores, filtered by status, so every visual inherits consistent logic
- Time intelligence over snapshot dates to show score movement between reporting periods
- Measures comparing inherent and residual scores to expose where mitigation exists on paper but not in the numbers

Keeping all logic in measures rather than calculated columns kept the model small and made every figure on the page traceable to one definition.

## What happened next

The prototype was received well internally and referred up the PMO chain. The wider lesson is transferable, and it is not about Power BI. Reporting earns trust when the person reading it can get from a headline number to the underlying item in two clicks, and no static document can offer that.

