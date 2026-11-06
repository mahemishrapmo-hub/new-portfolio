import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const link = z.object({ label: z.string(), href: z.string() });

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

// One markdown file per project. Frontmatter feeds the cards and filters,
// the body is the write-up on /projects/<slug>/.
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    ref: z.string(),
    title: z.string(),
    status: z.enum(['live', 'shipped', 'in-progress', 'awaiting-data']),
    order: z.number(),
    featured: z.boolean().default(false),
    summary: z.string(),
    tags: z.array(z.string()),
    stack: z.array(z.string()).default([]),
    // Where the data comes from. Honest provenance, shown on every project.
    data: z.string(),
    updated: z.coerce.date(),
    links: z.array(link).default([]),
    // Any iframe-able report, e.g. a Power BI publish-to-web URL.
    embed: z.object({ src: z.string().url(), title: z.string() }).optional(),
    caseStudy: z.string().optional(),
    // Render the live synthetic snapshot under the write-up.
    snapshot: z.enum(['portfolio', 'actions']).optional(),
  }),
});

// Case studies are the story with a measurable outcome. Projects are the build.
const cases = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/cases' }),
  schema: z.object({
    ref: z.string(),
    title: z.string(),
    summary: z.string(),
    order: z.number(),
    role: z.string(),
    period: z.string(),
    pubDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    outcomes: z.array(z.object({ value: z.string(), label: z.string() })).min(1).max(4),
    project: z.string().optional(),
  }),
});

export const collections = { blog, projects, cases };
