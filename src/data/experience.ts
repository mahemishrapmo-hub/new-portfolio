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
    title: 'PMO Analyst',
    org: 'North West Anglia NHS Foundation Trust',
    period: 'July 2026 to present',
    current: true,
    points: [
      'Designed, built and own the HHRP portfolio RAID dashboard in Power BI with 19 custom DAX and Power Query KPIs, consolidating 230+ risks, issues and dependencies across 8+ workstreams, replacing manual Excel consolidation and cutting the PMO reporting cycle from 2 to 3 days to under 30 minutes.',
      'Own the fortnightly PMO reporting cycle feeding the Deputy Programme Director and external governance chairs, producing the portfolio pack covering milestone slippage, benefits realisation, interdependencies and critical path variance across 30+ active programme activities on a £1B+ capital programme.',
      'Redesigned enabling works project reporting with the workstream chair, replacing narrative two-slide updates across 11 projects with a metrics-led template covering health and safety, finance, contingency, programme movement, change control and decision logging, plus a risk page per project.',
      'Lead PMO support for the Enabling Works Development Group (EWDG), owning fortnightly action tracker production, external chair review cycles and senior stakeholder circulation across the Trust and external partners.',
      'Operate PMO financial controls across 150+ purchase orders ranging £1k to £4.2m in Oracle Cloud ERP, tracking cost variance, flagging anomalies and producing forecast exposure reporting that surfaced reforecast risk to Finance ahead of month-end.',
      'Shape PMO reporting standards and data governance across the programme, consolidating 5+ workstream data sources into a single reporting layer, removing 10+ hours of manual reconciliation per cycle and improving portfolio data quality for Programme Board decision-making.',
      'Act as PMO point of contact for assurance queries from workstream leads, external chairs and Finance, translating programme data into decision-ready insight for senior stakeholders.',
    ],
  },
  {
    ref: 'EXP-02',
    title: 'PMO Coordinator',
    org: 'North West Anglia NHS Foundation Trust',
    period: 'Jan 2024 to July 2026',
    current: false,
    points: [
      'PMO point of contact for the New Main Theatres project at Hinchingbrooke Hospital, coordinating reporting, RAID and actions across 5+ workstream leads for the Senior Responsible Officer and Project Director.',
      'Produced the monthly Project Board and Project Team packs, consolidating workstream lead reports, and owned the project action tracker of 20+ actions.',
      'Delivered £280k of workforce savings across a 200 to 250 staff service, feeding evidence directly into the Trust’s Cost Improvement Programme (CIP) governance cycle.',
      'Developed 10+ KPI dashboards and management information reports for service leads and senior management, translating rostering and workforce data into evidence-based recommendations tracked through programme governance.',
      'Built Python automation (Pandas, NumPy) across 4 HealthRoster reporting workflows, driving 25 to 30 per cent efficiency gains and strengthening data quality for Trust-wide reporting.',
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
    detail: '',
    state: 'in-progress',
  },
  {
    ref: 'CRT-03',
    title: 'DP-600 Fabric Analytics Engineer Associate',
    org: 'Microsoft',
    detail: '',
    state: 'in-progress',
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
