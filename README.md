# mahemishra.co.uk

Personal site of Mahe Mishra, Programme Support Officer on the Hinchingbrooke Hospital Redevelopment Programme.
Astro, hand-written CSS, deployed on Cloudflare Pages.

Live at [www.mahemishra.co.uk](https://www.mahemishra.co.uk).

## Structure

```
src/data/        all personal data, edit here first for any factual change
src/content/     blog posts as markdown
src/pages/       routes
src/components/  header, footer, cards, status row
src/styles/      one global stylesheet
public/          static files, redirects, robots, favicon
```

## How to update

**Change a fact about the current role or dates.**
Edit `src/data/profile.ts`. Fields include role title, org, current role start date, and NHS career start date. The two date fields power the live counters shown in the hero status row.

**Add or amend a job.**
Edit `src/data/experience.ts`. Each entry has a ref, title, org, period, current flag, and a bulleted list of points. New role goes at the top of the array.

**Add or amend a project.**
Edit `src/data/projects.ts`. Status can be `live`, `shipped`, or `in-progress`, and tags feed the filter chips on the projects page automatically.

**Publish a new blog post.**
Create a new `.md` file in `src/content/blog/` with this frontmatter.

```yaml
---
title: 'Post title'
description: 'One sentence summary.'
pubDate: 2026-08-01
tags: ['Power BI']
draft: false
---
```

Post appears at `/writing/<filename>/` on the next deploy. `draft: true` hides it while you work on it.

**Add a shortlink.**
Edit `public/_redirects`. Format is `/path https://target 301` (permanent) or `302` (temporary). CV lives at `/cv`, LinkedIn at `/linkedin`.

## Local development

```bash
npm install
npm run dev
```

Site runs at `localhost:4321`. Production build with `npm run build`, output in `dist/`.

## Deployment

Pushing to `main` triggers a Cloudflare Pages build automatically. Build takes about 90 seconds. Any other branch builds too, and gets its own preview URL like `<hash>.mahemishra.pages.dev`, useful for reviewing drafts before merging.

Build command `npm run build`, output directory `dist`, Node 22 (pinned in `.node-version`).

## Design

Register-document aesthetic borrowed from programme documentation. Reference numbers on every section, RAG dots reserved for actual status, live counters computed in the browser rather than hardcoded. Dark mode toggles via the button in the header and respects system preference on first load.

Typography, Archivo display and Source Serif 4 body from Google Fonts, IBM Plex Mono for utility.
