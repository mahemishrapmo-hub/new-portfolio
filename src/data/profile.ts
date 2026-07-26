// ============================================================
// EDIT THIS FILE FIRST.
// Every personal fact on the site is pulled from here.
// Search for "TODO" and replace each one, then commit.
// ============================================================

export const profile = {
  name: 'Mahe Mishra',
  firstName: 'Mahe',

  // Shown in the hero and meta tags
  headline: 'Programme delivery and data, NHS capital projects',
  role: 'Programme Support Officer',
  org: 'North West Anglia NHS Foundation Trust',
  programme: 'Hinchingbrooke Hospital Redevelopment Programme',
  programmeShort: 'HHRP',

  // TODO confirm you want your city public. Region is a safe default.
  location: 'South Yorkshire, UK',

  // TODO confirm Cloudflare Email Routing forwards this address, then keep it.
  email: 'mahe@mahemishra.co.uk',

  github: 'https://github.com/mahemishrapmo-hub',

  // TODO set your real LinkedIn URL
  linkedin: 'https://www.linkedin.com/in/mahe-mishra-31693b267/',

  // Points at public/_redirects. Drop cv.pdf into public/ and
  // uncomment the /cv line there, then this link works.
  cvUrl: 'https://github.com/mahemishrapmo-hub/new-portfolio/blob/bbe352ab8580cdfd62c417be4d7e5ae165a31ce8/public/Mahe%20Mishra%20-%20Resume.pdf',

  // ---- Dates that power the live counters on the site ----
  // TODO replace with your real start dates (YYYY-MM-DD).
  currentRoleStart: '2025-01-01',
  nhsCareerStart: '2024-01-01',
};

export type Profile = typeof profile;
