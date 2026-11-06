import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { profile } from '../data/profile';
import { getCases, getPosts } from '../lib/content';

export async function GET(context: APIContext) {
  const [posts, cases] = await Promise.all([getPosts(), getCases()]);
  const items = [
    ...posts.map((p) => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: p.data.pubDate,
      link: `/writing/${p.id}/`,
      categories: ['Writing', ...p.data.tags],
    })),
    ...cases.map((c) => ({
      title: `${c.data.ref}: ${c.data.title}`,
      description: c.data.summary,
      pubDate: c.data.pubDate,
      link: `/cases/${c.id}/`,
      categories: ['Case study', ...c.data.tags],
    })),
  ].sort((a, b) => b.pubDate.valueOf() - a.pubDate.valueOf());

  return rss({
    title: `${profile.name}, ${profile.role}`,
    description: 'Writing and case studies on PMO practice, reporting and data.',
    site: context.site!,
    items,
    customData: '<language>en-gb</language>',
  });
}
