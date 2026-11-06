// The /uses page. Personal kit only. Nothing issued by an employer.
export const uses = [
  {
    ref: 'USE-01',
    group: 'Analysis and reporting',
    items: [
      { name: 'Power BI Desktop', note: 'Dashboards, DAX measures and Power Query.' },
      { name: 'Excel', note: 'Trackers, registers and Power Query.' },
      { name: 'Python', note: 'Pandas, NumPy and Scikit-learn for analysis. The synthetic data engine is standard library only.' },
      { name: 'SQL and R', note: 'Querying and statistics.' },
    ],
  },
  {
    ref: 'USE-02',
    group: 'Building',
    items: [
      { name: 'Astro', note: 'This site. Static output, typed content, no client framework.' },
      { name: 'GitHub Actions', note: 'Runs the synthetic programme every Monday and checks every pull request.' },
      { name: 'Cloudflare Pages', note: 'Hosting, redirects and a preview build for every branch.' },
    ],
  },
  {
    ref: 'USE-03',
    group: 'Desk',
    items: [
      { name: 'Desktop', note: 'Ryzen 7 7800X3D, RTX 5070 Ti, 32GB DDR5.' },
      { name: 'Monitors', note: 'Two LG 27GN800 at 1440p and a BenQ 27-inch.' },
      { name: 'Keyboard', note: 'Aula F99 Pro.' },
      { name: 'Headphones', note: 'Sennheiser Momentum 4.' },
      { name: 'Laptop', note: 'HP Envy x360.' },
    ],
  },
  {
    ref: 'USE-04',
    group: 'Home lab',
    items: [
      { name: 'NAS', note: 'HP 290 G1 tower on TrueNAS Community Edition. Write-up in PRJ-07.', href: '/projects/home-lab/' },
    ],
  },
];
