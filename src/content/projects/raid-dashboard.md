---
ref: PRJ-01
title: RAID dashboard in Power BI
status: shipped
order: 1
featured: true
summary: Interactive risk, assumption, issue and dependency reporting for a £1B+ NHS redevelopment programme, replacing static spreadsheet tracking.
tags: ['Power BI', 'DAX', 'PMO']
stack: ['Power BI', 'DAX', 'Power Query', 'SharePoint']
data: Built inside the programme. Shown here as method only. No programme data leaves the Trust.
updated: 2026-11-02
caseStudy: raid-dashboard
links:
  - label: Read the build write-up
    href: /writing/raid-log-dashboard-power-bi/
  - label: See the open rebuild, PRJ-02
    href: /projects/portfolio-dashboard/
---

## What it is

The RAID log for the Hinchingbrooke Hospital Redevelopment Programme used to be a flat spreadsheet. It could tell you what risks existed. It could not tell a Programme Board what had changed, which risks were getting worse despite mitigation, or where ownership was piling up.

Version 1 answered those questions in two pages. **Current Position** is the live picture, open items by severity and workstream, ownership spread and anything past its review date. **Mitigation Journey** is the trend, score movement over time and the gap between inherent and residual exposure. Every figure comes from a single DAX measure layer, so a number on the page always traces back to one definition.

It was built end to end on a dummy dataset so it could be demonstrated without a single redaction. The Deputy Head of PMO endorsed it, and I now hold named ownership of RAID reporting in the PMO operating model.

## Version 2, in build

- **Live source.** Power BI reads the programme's RAID log directly from its SharePoint library, so the dashboard is never a copy of a copy.
- **Five report pages**, with the source reshaped in Power Query rather than patched in DAX.
- **Board-safe views.** Bookmarks switch the same report between the working view and a board view that suppresses sensitive columns, so one model serves both audiences.
- **Meeting brief generator.** A DAX layer that writes the headline narrative for each review from the live numbers, so the summary in the pack matches the dashboard by construction.

## What stays private

Any report built inside NHS employment belongs to the Trust, and that includes the files. Everything public on this site is rebuilt from scratch on personal hardware against synthetic or openly licensed data. The open rebuild of this pattern lives in [PRJ-02, the PMO central portfolio dashboard](/projects/portfolio-dashboard/).
