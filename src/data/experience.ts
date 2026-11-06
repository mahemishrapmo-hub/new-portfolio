export type Role = {
  ref: string;
  title: string;
  org: string;
  period: string;
  current: boolean;
  points: string[];
};

export const roles: Role[] = [
  {
    ref: 'EXP-01',
    title: 'PMO and Data Analyst',
    org: 'North West Anglia NHS Foundation Trust',
    period: '2025 to present',
    current: true,
    points: [
      'Reporting and analysis for the £1B+ Hinchingbrooke Hospital Redevelopment Programme, an NEC contract delivered with Kier Construction.',
      'Built the programme’s Power BI RAID dashboard, with DAX measures for risk exposure, mitigation trajectories and workstream views. Endorsed by the Deputy Head of PMO and now owned by me in the PMO operating model. Version 2, reading the RAID log live from SharePoint, is in build.',
      'Run the fortnightly action tracker for the enabling works governance group, turning each meeting into chair-ready updates with a dated audit trail on every action.',
      'Portfolio KPI reporting across workstreams, tracking milestones, dependencies and critical path items, and escalating variance to Programme Managers and the Deputy Programme Director.',
      'Expenditure of £1,000 to £350,000 per transaction through NHS SBS on Oracle Cloud ERP, with variance analysis against budget lines and anomalies escalated to Finance.',
      'Programme Board coordination, and data flow between Finance, Communications, Design and Construction, Mobilisation and the principal contractor.',
    ],
  },
  {
    ref: 'EXP-02',
    title: 'Workforce Consultant',
    org: 'North West Anglia NHS Foundation Trust',
    period: '2024 to 2025',
    current: false,
    points: [
      'HealthRoster workforce data for 200 to 250 staff, analysing rostering, capacity and leave patterns to inform workforce planning.',
      'Built Python automation across HealthRoster data operations, delivering a 25 to 30 percent workflow efficiency gain and removing manual processing errors.',
      'Workforce data analysis for the Trust’s Cost Improvement Programme, delivering £280k of validated savings.',
      'KPI dashboards and management information reports for service leads and senior management.',
    ],
  },
];

export type Credential = {
  ref: string;
  title: string;
  org: string;
  detail: string;
  // Drives the dot on the credentials roadmap. Done is green, in progress amber, planned hollow.
  state: 'done' | 'in-progress' | 'planned';
};

export const credentials: Credential[] = [
  {
    ref: 'EDU-01',
    title: 'BA (Dual Hons) Business Management and Economics, 2:1',
    org: 'University of Sheffield',
    detail: 'Graduated 2026.',
    state: 'done',
  },
  {
    ref: 'EDU-02',
    title: 'A-levels, 94.6%',
    org: 'Kendriya Vidyalaya',
    detail: '',
    state: 'done',
  },
  {
    ref: 'CRT-01',
    title: 'APM Project Management Qualification',
    org: 'Association for Project Management',
    detail: 'Online exam route.',
    state: 'in-progress',
  },
  {
    ref: 'CRT-02',
    title: 'PL-300 Power BI Data Analyst Associate',
    org: 'Microsoft',
    detail: 'Next, after the PMQ.',
    state: 'planned',
  },
  {
    ref: 'CRT-03',
    title: 'DP-600 Fabric Analytics Engineer Associate',
    org: 'Microsoft',
    detail: 'Planned, after PL-300.',
    state: 'planned',
  },
  {
    ref: 'CRT-04',
    title: 'MicroMasters in Statistics and Data Science',
    org: 'MIT',
    detail: 'Planned, from 2027.',
    state: 'planned',
  },
];

export const stack = [
  { group: 'Analysis', items: ['Python (Pandas, NumPy, Scikit-learn)', 'SQL', 'R'] },
  { group: 'Reporting', items: ['Power BI with DAX and Power Query', 'Excel', 'SharePoint'] },
  { group: 'PMO', items: ['RAID and risk management', 'Programme governance and action tracking', 'NEC contract environment', 'NHS SBS on Oracle Cloud ERP'] },
  { group: 'Build', items: ['Astro and TypeScript', 'GitHub Actions', 'Cloudflare Pages', 'TrueNAS'] },
];
