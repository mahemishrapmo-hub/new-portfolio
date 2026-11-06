import { getCollection, type CollectionEntry } from 'astro:content';

export type ProjectEntry = CollectionEntry<'projects'>;
export type CaseEntry = CollectionEntry<'cases'>;
export type Status = ProjectEntry['data']['status'];

export const statusLabel: Record<Status, string> = {
  live: 'Live',
  shipped: 'Shipped',
  'in-progress': 'In progress',
  'awaiting-data': 'Awaiting data',
};

// RAG is reserved for real status. Green means it exists and works,
// amber means it is being built, a hollow amber ring means it is waiting on someone else.
export const statusDot: Record<Status, string> = {
  live: 'green',
  shipped: 'green',
  'in-progress': 'amber',
  'awaiting-data': 'amber hollow',
};

export async function getProjects() {
  return (await getCollection('projects')).sort((a, b) => a.data.order - b.data.order);
}

export async function getCases() {
  return (await getCollection('cases')).sort((a, b) => a.data.order - b.data.order);
}

export async function getPosts() {
  return (await getCollection('blog', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
  );
}

export function tagCounts(projects: ProjectEntry[]) {
  const counts = new Map<string, number>();
  for (const p of projects) for (const t of p.data.tags) counts.set(t, (counts.get(t) ?? 0) + 1);
  return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}

export const fmtDate = (d: Date, month: 'short' | 'long' = 'short') =>
  d.toLocaleDateString('en-GB', { year: 'numeric', month, day: '2-digit', timeZone: 'UTC' });
