// schema.org structured data. Helps search engines treat the site as one
// defined person rather than a loose set of pages.
import { profile } from '../data/profile';

const site = 'https://www.mahemishra.co.uk';

export const personSchema = {
  '@type': 'Person',
  '@id': `${site}/#person`,
  name: profile.name,
  alternateName: profile.fullName,
  jobTitle: profile.role,
  url: `${site}/`,
  email: `mailto:${profile.email}`,
  image: `${site}/og/index.png`,
  worksFor: { '@type': 'Organization', name: profile.org },
  alumniOf: { '@type': 'CollegeOrUniversity', name: profile.alumniOf },
  address: { '@type': 'PostalAddress', addressRegion: 'South Yorkshire', addressCountry: 'GB' },
  knowsAbout: profile.knowsAbout,
  sameAs: [profile.linkedin, profile.github],
};

export const websiteSchema = {
  '@type': 'WebSite',
  '@id': `${site}/#website`,
  url: `${site}/`,
  name: profile.name,
  inLanguage: 'en-GB',
  publisher: { '@id': `${site}/#person` },
};

export const articleSchema = (o: { title: string; description: string; url: string; published: Date; modified?: Date }) => ({
  '@type': 'BlogPosting',
  headline: o.title,
  description: o.description,
  url: o.url,
  datePublished: o.published.toISOString(),
  dateModified: (o.modified ?? o.published).toISOString(),
  inLanguage: 'en-GB',
  author: { '@id': `${site}/#person`, '@type': 'Person', name: profile.name, url: `${site}/` },
  image: o.url.replace(site, `${site}/og`).replace(/\/$/, '.png'),
});
