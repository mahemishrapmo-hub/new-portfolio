---
ref: PRJ-08
title: This site
status: live
order: 8
featured: false
summary: A controlled-document take on a personal site. Astro, hand-written CSS, self-hosted fonts and a synthetic programme that updates itself every Monday.
tags: ['Astro', 'Cloudflare', 'Web']
stack: ['Astro', 'TypeScript', 'CSS', 'Cloudflare Pages', 'GitHub Actions']
data: Public. The source is on GitHub.
updated: 2026-11-04
links:
  - label: View source
    href: https://github.com/mahemishrapmo-hub/new-portfolio
---

## Design

No template. The layout borrows from programme documentation. Every section has a reference number, every project has a status, and the RAG colours are only used where a real status exists. Live counters are computed in the visitor's browser rather than typed in, so they are never wrong.

## Under the bonnet

- **Static Astro build** deployed on Cloudflare Pages. Every push to main builds and ships in about 90 seconds.
- **Content as markdown.** Projects, case studies and writing are content collections with typed frontmatter, so a missing field fails the build instead of shipping a broken page.
- **Fonts served from this domain.** No calls to a third-party font service, so nothing about a visitor is shared to load a typeface.
- **Social cards generated at build time.** Every page gets its own preview image, drawn from its title and status.
- **RSS** for writing and case studies.
- **A synthetic programme** that moves forward every Monday through a [GitHub Action](/projects/synthetic-data-engine/), feeding the live snapshot on the index.
- **Build check on every pull request**, with the data engine's tests run first.
