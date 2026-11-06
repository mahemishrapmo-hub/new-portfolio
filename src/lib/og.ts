import { profile } from '../data/profile';
import { getCases, getPosts, getProjects, statusLabel, type Status } from './content';

export type OgCard = {
  route: string; // e.g. 'index', 'projects/raid-dashboard'
  ref: string;
  title: string;
  subtitle: string;
  status?: Status;
};

/** Page path to its social card. '/' -> '/og/index.png', '/projects/x/' -> '/og/projects/x.png'. */
export function ogPathFor(pathname: string) {
  const clean = pathname.replace(/^\/+|\/+$/g, '').replace(/\.html$/, '');
  return `/og/${clean || 'index'}.png`;
}

const pages: OgCard[] = [
  { route: 'index', ref: 'Register', title: `${profile.role}.`, subtitle: profile.headline },
  { route: 'projects', ref: 'PRJ', title: 'Projects', subtitle: 'Dashboards, trackers and automation, shown through synthetic data or method only.' },
  { route: 'cases', ref: 'CS', title: 'Case studies', subtitle: 'The story behind the work, with the outcome measured.' },
  { route: 'experience', ref: 'EXP', title: 'Experience', subtitle: `${profile.role}, ${profile.org}.` },
  { route: 'writing', ref: 'WRT', title: 'Writing', subtitle: 'Notes on PMO practice, reporting and data.' },
  { route: 'now', ref: 'NOW', title: 'Now', subtitle: 'What I am working on, building and studying this month.' },
  { route: 'uses', ref: 'USE', title: 'Uses', subtitle: 'The software and kit behind the work.' },
  { route: 'about', ref: 'ABT', title: 'About', subtitle: `${profile.name}, ${profile.role}.` },
  { route: '404', ref: 'Ref not found', title: '404', subtitle: 'This entry does not exist in the register.' },
];

export async function ogCards(): Promise<OgCard[]> {
  const [projects, cases, posts] = await Promise.all([getProjects(), getCases(), getPosts()]);
  return [
    ...pages,
    ...projects.map((p) => ({
      route: `projects/${p.id}`,
      ref: `${p.data.ref} · ${statusLabel[p.data.status]}`,
      title: p.data.title,
      subtitle: p.data.summary,
      status: p.data.status,
    })),
    ...cases.map((c) => ({
      route: `cases/${c.id}`,
      ref: `${c.data.ref} · ${c.data.outcomes[0].value} ${c.data.outcomes[0].label}`,
      title: c.data.title,
      subtitle: c.data.summary,
    })),
    ...posts.map((p) => ({
      route: `writing/${p.id}`,
      ref: `Writing · ${p.data.pubDate.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' })}`,
      title: p.data.title,
      subtitle: p.data.description,
    })),
  ];
}
