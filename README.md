# mahemishra.co.uk

Personal site of Mahe Mishra, PMO and Data Analyst on the Hinchingbrooke Hospital Redevelopment Programme.
Astro, hand-written CSS, deployed on Cloudflare Pages. A synthetic hospital programme moves forward every Monday and feeds the live snapshot on the index.

Live at [www.mahemishra.co.uk](https://www.mahemishra.co.uk).

## Structure

```
src/data/            personal data, edit here first for any factual change
src/content/blog/    writing, one markdown file per post
src/content/projects one markdown file per project, frontmatter drives cards and filters
src/content/cases/   case studies, outcome first
src/pages/           routes, including rss.xml and og/ social cards
src/components/      header, footer, cards, status row, snapshot/
src/lib/             collection helpers, structured data, social card list
src/styles/          one global stylesheet
scripts/synthetic/   the synthetic programme engine and its tests (Python, standard library)
public/data/         CSVs written by the engine, served at /data/
public/              redirects, headers, robots, favicon
.github/workflows/   weekly data refresh and pull request build check
```

## How to update

**Change a fact about the current role or dates.**
Edit `src/data/profile.ts`. The title, one-line headline, CV link and the two dates that drive the live counters all live there.

**Add or amend a job, a credential or the stack.**
Edit `src/data/experience.ts`. Credentials have a `state` of `done`, `in-progress` or `planned`, which drives the dots on Experience and the roadmap on About.

**Add a project.**
Create `src/content/projects/<slug>.md`. Page appears at `/projects/<slug>/`, with its own social card.

```yaml
---
ref: 'PRJ-10'
title: 'Project title'
status: 'in-progress'    # live | shipped | in-progress | awaiting-data
order: 10                # position on the projects page
featured: false          # true puts it on the index, first six by order
summary: 'One or two sentences for the card.'
tags: ['Power BI']       # feeds the filter chips automatically
stack: ['Power BI', 'DAX']
data: 'Where the data comes from. Required, shown on every project.'
updated: 2026-11-04
caseStudy: 'slug'        # optional, links a case study
snapshot: 'portfolio'    # optional, portfolio | actions, renders the live synthetic snapshot
links:
  - label: 'View source'
    href: 'https://github.com/...'
embed:                   # optional, any iframe-able report
  src: 'https://...'
  title: 'Report title'
---
```

**Add a case study.**
Create `src/content/cases/<slug>.md` with `ref`, `title`, `summary`, `order`, `role`, `period` (quote it if it is a bare year), `pubDate`, `tags`, one to four `outcomes` as `value` and `label`, and an optional `project` slug. The first outcome is the headline figure on the card.

**Publish a post.**
Create `src/content/blog/<slug>.md` with `title`, `description`, `pubDate`, `tags` and `draft`. `draft: true` hides it while you work on it. Posts and case studies both go out on `/rss.xml`.

**Update the now page.**
Edit `src/data/now.ts` and change `reviewed` to today. The page turns amber by itself after 45 days.

**Add a shortlink.**
Edit `public/_redirects`. `/cv`, `/linkedin`, `/github`, `/source` and `/rss` are set. If the CV moves, change `cvUrl` in `profile.ts` and `/cv` in `_redirects` together.

## The synthetic programme

`scripts/synthetic/generate.py` replays the fictional Halden Vale Health Campus Programme from its start date to the current Monday and writes four CSVs to `public/data/` plus `src/data/synthetic/snapshot.json` for the site. It is deterministic, so the same week always gives identical files, and forward only, so published history never changes. Owners are role codes, never people.

```bash
npm run data           # generate the current week
npm run data:test      # run the engine's tests
python3 scripts/synthetic/generate.py --as-of 2026-09-07   # rebuild any past week
```

`.github/workflows/weekly-synthetic-refresh.yml` runs every Monday at 06:30 UTC, tests the engine, generates the week and commits as `github-actions[bot]`. The commit triggers a Cloudflare build. To run it by hand, open the Actions tab and use **Run workflow**. The repository needs **Settings, Actions, General, Workflow permissions** set to read and write.

Power BI can read the CSVs straight from `https://www.mahemishra.co.uk/data/<file>.csv` with the Web connector.

## Local development

```bash
npm install
npm run dev
```

Site runs at `localhost:4321`. Production build with `npm run build`, output in `dist/`.

## Deployment

Pushing to `main` triggers a Cloudflare Pages build automatically. Any other branch gets its own preview URL. Pull requests also run `.github/workflows/ci.yml`, which tests the data engine and builds the site.

Build command `npm run build`, output directory `dist`, Node 22 (pinned in `.node-version`).

### Optional analytics

Cloudflare Web Analytics can be switched on from the Pages project with no code. For self-hosted Umami instead, set `PUBLIC_UMAMI_SRC` and `PUBLIC_UMAMI_WEBSITE_ID` as environment variables in Cloudflare Pages. Leave them unset and nothing loads.

## Design

Register-document aesthetic borrowed from programme documentation. Reference numbers on every section, RAG dots reserved for actual status, live counters and freshness computed in the browser rather than hardcoded. Dark mode toggles from the header, follows the system until a choice is made.

Typography, Archivo display and Source Serif 4 body, IBM Plex Mono for utility. All three are self-hosted through Fontsource, so there are no calls to a third-party font service. Social cards are drawn at build time with Satori and resvg in the same type and palette.

## What stays off this repository

Anything built inside NHS employment belongs to the Trust, including `.pbix` files and screenshots of real data. Everything here is either written from scratch on personal hardware or runs on synthetic or openly licensed data.
