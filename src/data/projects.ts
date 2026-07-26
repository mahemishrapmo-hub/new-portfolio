export type Project = {
  ref: string;
  title: string;
  status: 'live' | 'shipped' | 'in-progress';
  summary: string;
  detail: string;
  tags: string[];
  link?: { label: string; href: string };
};

export const projects: Project[] = [
  {
    ref: 'PRJ-01',
    title: 'RAID log dashboard in Power BI',
    status: 'shipped',
    summary:
      'Interactive risk, assumption, issue and dependency reporting for a £1B+ NHS redevelopment programme, replacing static spreadsheet tracking.',
    detail:
      'Built end to end on a synthetic dataset so the prototype could be shared safely. Two report pages, Current Position for the live risk picture and Mitigation Journey for movement over time, backed by a full DAX measure layer. Presented internally and taken forward with the PMO.',
    tags: ['Power BI', 'DAX', 'PMO'],
  },
  {
    ref: 'PRJ-02',
    title: 'Workforce data automation in Python',
    status: 'shipped',
    summary:
      'Automated recurring HealthRoster workforce data workflows and management information reporting for an NHS trust.',
    detail:
      'Replaced manual extract and reshape steps with Python, cutting 25 to 30 percent of the time spent on routine reporting tasks and reducing rekeying errors in the process.',
    tags: ['Python', 'Automation', 'NHS'],
  },
  {
    ref: 'PRJ-03',
    title: 'This site',
    status: 'live',
    summary:
      'A controlled-document take on a personal site. Astro, hand-written CSS, deployed on Cloudflare Pages with automatic builds on every push.',
    detail:
      'No template. Register-style layout borrowed from programme documentation, live counters computed in the browser, content managed as markdown. The source is public.',
    tags: ['Astro', 'Cloudflare', 'Web'],
    link: { label: 'View source', href: 'https://github.com/mahemishrapmo-hub/new-portfolio' },
  },
];

export const allTags = [...new Set(projects.flatMap((p) => p.tags))];
