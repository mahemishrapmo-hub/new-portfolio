---
ref: PRJ-01
title: RAID dashboard in Power BI
status: shipped
order: 1
featured: true
summary: Interactive risk and issue reporting for a £1B+ NHS redevelopment programme, replacing static spreadsheet tracking. Version 3 is built, three pages around the RAID review.
tags: ['Power BI', 'DAX', 'PMO']
stack: ['Power BI', 'DAX', 'Power Query', 'Excel']
data: Built inside the programme. Shown here as method only. No programme data leaves the Trust.
updated: 2026-11-13
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

## Version 3, built

Version 2 was specified as five pages reading the log live from SharePoint, with bookmark-driven board views and a full meeting brief generator. The build that came out of that spec, version 3, is three pages. The live SharePoint connection moved to phase 2 and the brief generator tab was dropped. Each page now carries a one-line takeaway written in DAX instead.

- **Current Position.** Cards for open risks, risks scoring 12 and above, risks at or above the board threshold of 15, red risks and overdue actions. A likelihood by impact heat map on current scores. Open risks by workstream and by RAG, and a register filtered by workstream, owner and Datix status.
- **RAID Meeting.** Built for the RAID review. Proposed risks and risks proposed for closure, impact 5 risks, open risks by escalation level and by trend, actions with owners and due dates, and the number of days until each risk reaches its exposure date.
- **Issues.** Open, significant and red issues, with the register and the latest review on each.
- **A takeaway line on every page.** One measure writes the headline sentence from the live counts, so the sentence at the top of the page can never disagree with the cards beneath it.
- **Source fixed in Power Query, not patched in DAX.** Due dates parsed out of free text, "N/A" exposure dates set to null, escalation routes collapsed into five levels from not escalated up to Trust Board, and line breaks stripped from long text so tables wrap cleanly.
- **Programme theme.** A custom report theme so a colour means the same thing on every visual, with page navigation built into the header.

For now the risks and issues are re-exported from the master RAID log each cycle and swapped in. Reading the log live from its SharePoint library is the next phase.

## What stays private

Any report built inside NHS employment belongs to the Trust, and that includes the files. Everything public on this site is rebuilt from scratch on personal hardware against synthetic or openly licensed data. The open rebuild of this pattern lives in [PRJ-02, the PMO central portfolio dashboard](/projects/portfolio-dashboard/).
