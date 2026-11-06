export const profile = {
  name: 'Mahe Mishra',
  firstName: 'Mahe',
  fullName: 'Mahaswar Mishra',

  // The title used everywhere: hero, meta tags, structured data, experience.
  role: 'PMO and Data Analyst',
  // One line under the hero. This is the line that gets screenshotted into recruiter messages.
  headline: 'Power BI, DAX, Python and SQL, running the reporting on a £1B+ NHS capital programme',
  org: 'North West Anglia NHS Foundation Trust',
  programme: 'Hinchingbrooke Hospital Redevelopment Programme',
  programmeShort: 'HHRP',

  location: 'South Yorkshire, UK',

  email: 'mahe@mahemishra.co.uk',

  github: 'https://github.com/mahemishrapmo-hub',
  repo: 'https://github.com/mahemishrapmo-hub/new-portfolio',

  linkedin: 'https://www.linkedin.com/in/mahe-mishra-31693b267/',

  // The CV button points here. /cv on the live site redirects to the same place,
  // set in public/_redirects. Change both together.
  cvUrl: '/mahe-mishra-cv.pdf',

  // These power the live counters in the hero status row.
  currentRoleStart: '2025-01-01',
  nhsCareerStart: '2024-01-01',

  // Fed into structured data so search engines can describe the person behind the site.
  knowsAbout: [
    'Power BI',
    'DAX',
    'Power Query',
    'Python',
    'SQL',
    'R',
    'Excel',
    'PMO reporting',
    'RAID management',
    'Programme governance',
    'NHS capital programmes',
  ],
  alumniOf: 'University of Sheffield',
};

export type Profile = typeof profile;
