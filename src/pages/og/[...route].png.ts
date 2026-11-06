// Social preview cards, one per page, drawn at build time with Satori and
// rasterised with resvg. Same palette and type as the site, dark register.
import type { APIRoute, GetStaticPaths } from 'astro';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { ogCards, type OgCard } from '../../lib/og';
import { statusDot } from '../../lib/content';

const require = createRequire(import.meta.url);
const font = (pkg: string, file: string) => readFileSync(require.resolve(`${pkg}/files/${file}`));

const fonts = [
  { name: 'Archivo', data: font('@fontsource/archivo', 'archivo-latin-800-normal.woff'), weight: 800, style: 'normal' },
  { name: 'Archivo', data: font('@fontsource/archivo', 'archivo-latin-700-normal.woff'), weight: 700, style: 'normal' },
  { name: 'Serif', data: font('@fontsource/source-serif-4', 'source-serif-4-latin-400-normal.woff'), weight: 400, style: 'normal' },
  { name: 'Mono', data: font('@fontsource/ibm-plex-mono', 'ibm-plex-mono-latin-400-normal.woff'), weight: 400, style: 'normal' },
  { name: 'Mono', data: font('@fontsource/ibm-plex-mono', 'ibm-plex-mono-latin-500-normal.woff'), weight: 500, style: 'normal' },
] as const;

const c = {
  paper: '#10161d',
  raised: '#161e27',
  ink: '#e8ecef',
  muted: '#93a0ab',
  line: '#263039',
  accent: '#6c96ff',
  green: '#2e9e6b',
  amber: '#e39a2d',
};

type Node = { type: string; props: Record<string, unknown> };
const h = (type: string, style: Record<string, unknown>, ...children: unknown[]): Node => ({
  type,
  props: { style: { display: 'flex', ...style }, children: children.length === 1 ? children[0] : children },
});

const clamp = (s: string, n: number) =>
  s.length > n ? `${s.slice(0, s.lastIndexOf(' ', n - 1)).replace(/[,.;]$/, '')}…` : s;

function card(o: OgCard): Node {
  const titleSize = o.title.length > 60 ? 58 : o.title.length > 34 ? 68 : 92;
  const dot = o.status ? statusDot[o.status] : undefined;
  const dotColour = dot?.startsWith('green') ? c.green : c.amber;
  const hollow = dot?.includes('hollow');

  // Yoga sizes boxes without padding, so the frame is explicit: 1200 x 630 less the margins.
  return h(
    'div',
    { width: 1200, height: 630, background: c.paper, alignItems: 'center', justifyContent: 'center' },
    h(
    'div',
    { width: 1072, height: 534, flexDirection: 'column', color: c.ink, fontFamily: 'Serif' },
    h(
      'div',
      { alignItems: 'center', justifyContent: 'space-between', paddingBottom: 28, borderBottom: `1px solid ${c.line}` },
      h(
        'div',
        { alignItems: 'center', gap: 18 },
        h('div', { background: c.ink, color: c.paper, fontFamily: 'Archivo', fontWeight: 800, fontSize: 30, padding: '4px 12px' }, 'MM'),
        h('div', { fontFamily: 'Mono', fontSize: 22, letterSpacing: 3, color: c.muted }, 'PORTFOLIO / REV 2026')
      ),
      h('div', { fontFamily: 'Mono', fontSize: 22, letterSpacing: 3, color: c.muted }, 'MAHEMISHRA.CO.UK')
    ),
    h(
      'div',
      { flexDirection: 'column', flexGrow: 1, justifyContent: 'center', gap: 26 },
      h(
        'div',
        { alignItems: 'center', gap: 14, fontFamily: 'Mono', fontWeight: 500, fontSize: 24, letterSpacing: 2.5, color: c.accent },
        ...(dot
          ? [h('div', { width: 18, height: 18, borderRadius: 9999, background: hollow ? 'transparent' : dotColour, border: `3px solid ${dotColour}` })]
          : []),
        clamp(o.ref.toUpperCase(), 70)
      ),
      h('div', { fontFamily: 'Archivo', fontWeight: 800, fontSize: titleSize, lineHeight: 1.04, letterSpacing: -1.5, maxWidth: 1060 }, clamp(o.title, 90)),
      h('div', { fontSize: 30, lineHeight: 1.4, color: c.muted, maxWidth: 1000 }, clamp(o.subtitle, 150))
    ),
    h(
      'div',
      { alignItems: 'center', gap: 16, borderLeft: `4px solid ${c.green}`, background: c.raised, padding: '16px 22px', fontFamily: 'Mono', fontSize: 22, letterSpacing: 2 },
      h('div', { width: 14, height: 14, borderRadius: 9999, background: c.green }),
      h('div', { color: c.muted }, 'MAHE MISHRA'),
      h('div', { color: c.ink }, 'PMO AND DATA ANALYST')
    )
    )
  );
}

export const getStaticPaths = (async () => {
  const cards = await ogCards();
  return cards.map((o) => ({ params: { route: o.route }, props: { o } }));
}) satisfies GetStaticPaths;

export const GET: APIRoute = async ({ props }) => {
  const svg = await satori(card((props as { o: OgCard }).o) as unknown as Parameters<typeof satori>[0], {
    width: 1200,
    height: 630,
    fonts: fonts as unknown as Parameters<typeof satori>[1]['fonts'],
  });
  const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
};
