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
  location: 'Yorkshire, UK',

  // TODO confirm Cloudflare Email Routing forwards this address, then keep it.
  email: 'mahe@mahemishra.co.uk',

  github: 'https://github.com/mahemishrapmo-hub',

  // TODO set your real LinkedIn URL
  linkedin: 'https://www.linkedin.com/in/YOUR-SLUG',

  // Points at public/_redirects. Drop cv.pdf into public/ and
  // uncomment the /cv line there, then this link works.
  cvUrl: '/cv',

  // ---- Dates that power the live counters on the site ----
  // TODO replace with your real start dates (YYYY-MM-DD).
  currentRoleStart: '2025-10-01',
  nhsCareerStart: '2024-06-01',
};

export type Profile = typeof profile;
