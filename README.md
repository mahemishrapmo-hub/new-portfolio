# mahemishra.co.uk

Personal site of Mahe Mishra. Astro, hand-written CSS, deployed on Cloudflare Pages.

## Before this goes live, edit these

Everything personal lives in three data files. Search each for `TODO`.

1. `src/data/profile.ts`. Start dates (they power the live counters), LinkedIn URL, location, email.
2. `src/data/experience.ts`. Replace the placeholder period strings with real dates.
3. `public/_redirects`. Drop `cv.pdf` into `public/`, then uncomment the `/cv` line. Set the LinkedIn shortlink.
4. `src/content/blog/raid-log-dashboard-power-bi.md`. Read the post, edit anything that does not sound like you, add screenshots, then set `draft: false`.

## Local development

```bash
npm install
npm run dev
```

Site runs at `localhost:4321`. Production build with `npm run build`, output in `dist/`.

## Deployment

Pushing to `main` triggers a Cloudflare Pages build automatically.
Build command `npm run build`, output directory `dist`, Node 22 (pinned in `.node-version`).

## Adding a blog post

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

The post appears at `/writing/<filename>/` on the next deploy.

## Structure

```
src/data/        all personal data, edit here
src/content/     blog posts as markdown
src/pages/       routes
src/components/  header, footer, cards, status row
src/styles/      one global stylesheet
public/          static files, redirects, robots, favicon
```
