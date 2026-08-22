// Converte le tavole .dc.html in HTML autonomo e le renderizza con Chromium
// in PNG (bitmap alla dimensione reale) e PDF (testo vettoriale).
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { execFileSync } from 'node:child_process'
import { join, resolve } from 'node:path'

const CHROME = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'
const OUT = resolve('export')
const TMP = resolve('export/.tmp')
mkdirSync(OUT, { recursive: true })
mkdirSync(TMP, { recursive: true })

const canvas = JSON.parse(readFileSync('canvas.json', 'utf8'))
const FONTS = readFileSync(join(TMP, 'fonts.css'), 'utf8')

function standalone(file) {
  const src = readFileSync(file, 'utf8')
  const helmet = (src.match(/<helmet>([\s\S]*?)<\/helmet>/) || [, ''])[1]
    // il <link> a Google Fonts diventa il CSS incorporato: niente rete, resa deterministica
    .replace(/<link[^>]+fonts\.googleapis\.com[^>]*>/g, `<style>${FONTS}</style>`)
  const body = (src.match(/<x-dc>([\s\S]*?)<\/x-dc>/) || [, ''])[1]
    .replace(/<helmet>[\s\S]*?<\/helmet>/, '')
  return `<!doctype html><html><head><meta charset="utf-8">${helmet}
<style>html,body{margin:0;padding:0;background:transparent}
@page{margin:0}</style></head><body>${body}</body></html>`
}

for (const a of canvas.artboards) {
  const stem = a.file.replace(/\.dc\.html$/, '')
  const tmp = join(TMP, `${stem}.html`)
  writeFileSync(tmp, standalone(a.file))
  const common = [
    '--headless', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
    '--force-color-profile=srgb', '--font-render-hinting=none',
    '--virtual-time-budget=4000',
  ]
  execFileSync(CHROME, [...common,
    `--window-size=${a.w},${a.h}`,
    `--screenshot=${join(OUT, stem + '.png')}`,
    `file://${tmp}`], { stdio: 'pipe' })
  execFileSync(CHROME, [...common,
    '--no-pdf-header-footer',
    `--print-to-pdf=${join(OUT, stem + '.pdf')}`,
    `file://${tmp}`], { stdio: 'pipe' })
  console.log(`${stem}  ${a.w}x${a.h}`)
}
