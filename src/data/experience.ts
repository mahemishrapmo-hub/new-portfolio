export type Role = {
  ref: string;
  title: string;
  org: string;
  // TODO replace period strings with your real dates
  period: string;
  current: boolean;
  points: string[];
};

export const roles: Role[] = [
  {
    ref: 'EXP-01',
    title: 'Programme Support Officer',
    org: 'North West Anglia NHS Foundation Trust',
    period: '2025 to present', 
    current: true,
    points: [
      'Supporting the £1B+ Hinchingbrooke Hospital Redevelopment Programme, an NEC contract delivered with Kier Construction.',
      'Programme Board coordination and minute taking for senior governance meetings.',
      'Invoice management through NHS Shared Business Services across programme workstreams.',
      'Risk and RAID tracking, including building the Power BI reporting prototype now with the PMO.',
      'Cross-functional liaison across Finance, Communications, Design and Construction, and Mobilisation teams.',
    ],
  },
  {
    ref: 'EXP-02',
    title: 'Workforce Information Officer',
    org: 'North West Anglia NHS Foundation Trust',
    period: '2024 to 2025', // TODO real dates
    current: false,
    points: [
      'Workforce data management in HealthRoster for clinical and non-clinical staff groups.',
      'Built Python automation for recurring data workflows, delivering a 25 to 30 percent efficiency gain on routine reporting.',
      'Produced management information reporting for operational teams.',
    ],
  },
];

export type Credential = {
  ref: string;
  title: string;
  org: string;
  detail: string;
};

export const credentials: Credential[] = [
  {
    ref: 'EDU-01',
    title: 'BA (Dual Hons) Business Management and Economics, 2:1',
    org: 'University of Sheffield',
    detail: 'Graduated 2026.',
  },
  {
    ref: 'EDU-02',
    title: 'A-levels, 94.6%',
    org: 'Kendriya Vidyalaya',
    detail: '',
  },
  {
    ref: 'CRT-01',
    title: 'APM Project Management Qualification',
    org: 'Association for Project Management',
    detail: 'In progress.',
  },
];

export const stack = [
  { group: 'Analysis', items: ['Python (Pandas, NumPy, Scikit-learn)', 'R', 'SQL'] },
  { group: 'Reporting', items: ['Power BI with DAX', 'Excel'] },
  { group: 'Delivery', items: ['NEC contract environment', 'RAID and risk management', 'Programme governance', 'NHS SBS invoicing'] },
];
