// Scarica i font Google usati dalle tavole e li incorpora in un CSS locale
// con data URI, così il rendering non dipende dalla rete ed è deterministico.
import { readFileSync, writeFileSync, readdirSync } from 'node:fs'
import { execFileSync } from 'node:child_process'

const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
const hrefs = new Set()
for (const f of readdirSync('.').filter(f => f.endsWith('.dc.html'))) {
  for (const m of readFileSync(f, 'utf8').matchAll(/href="(https:\/\/fonts\.googleapis\.com[^"]+)"/g)) {
    hrefs.add(m[1].replace(/&amp;/g, '&'))
  }
}

let out = ''
for (const href of hrefs) {
  const css = execFileSync('curl', ['-sSL', '-A', UA, href], { encoding: 'utf8', maxBuffer: 1 << 24 })
  let n = 0
  out += css.replace(/url\((https:\/\/fonts\.gstatic\.com[^)]+)\)/g, (_, url) => {
    const b64 = execFileSync('bash', ['-c', `curl -sSL '${url}' | base64 -w0`], { encoding: 'utf8', maxBuffer: 1 << 26 })
    n++
    return `url(data:font/woff2;base64,${b64})`
  })
  console.error(`${href.slice(39, 90)}… → ${n} file`)
}
writeFileSync('export/.tmp/fonts.css', out)
console.error(`fonts.css: ${(out.length / 1024 / 1024).toFixed(1)} MB`)
