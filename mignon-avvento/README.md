# Calendario dell'Avvento — Mignon Experience

Proposte grafiche di presentazione, sorgenti del canvas pubblicato.

Ogni file `.dc.html` è una tavola (artboard); `canvas.json` definisce pagine,
posizioni e note. Per rigenerare il canvas si ri-seeda con l'helper della skill
`design` e si ripubblica sullo stesso URL.

## Struttura

| Pagina | Tavole |
|---|---|
| Direzioni | `Main.dc.html` (A — Notte di dicembre), `DirezioneB.dc.html` (B — Carta & colore), `DirezioneC.dc.html` (C — Slow December) |
| 1 · Composizione | `Composizione.dc.html`, `ComposizioneDettaglio.dc.html` |
| 2 · Arrivo a casa | `Packaging.dc.html`, `PackagingStory.dc.html` |
| 3 · Relax | `Relax.dc.html`, `RelaxStory.dc.html` |
| 4 · Idee | `Idee.dc.html`, `IdeaCasellaDelGiorno.dc.html` |

Le sezioni 1–4 sono sviluppate nella Direzione A.

## Palette

Ricavata dal marchio Mignon Experience:

| | |
|---|---|
| Rosso | `#E42313` |
| Arancio | `#F08019` |
| Viola | `#7A2E8E` |
| Giallo | `#F6D01A` |
| Fondo scuro | `#14100E` |
| Carta | `#F3ECE2` |

Font: Bodoni Moda + Jost (dir. A), Archivo Black + Archivo (dir. B),
Cormorant Garamond + Mulish (dir. C).

## Dati da confermare

Nel copy sono lasciati fra parentesi quadre: numero di cantine, formato in ml
delle mignon, prezzo del cofanetto, data limite ordine, ripartizione per
tipologia di vino, nomi delle etichette.

## Asset del marchio

| File | Uso |
|---|---|
| `bottiglie.png` | le quattro bottiglie del marchio, distanze e sfalsamento originali |
| `bottiglia-rossa/arancio/viola/gialla.png` | le stesse, isolate, per le caselle del calendario |
| `logo-src/image1.png` | file di partenza, intatto |

Il marchio nelle tavole è **ricostruito**: le bottiglie sono l'immagine
originale, "Mignon Experience" e "le più piccole" sono testo vivo in
Montserrat (700 e 300). I due file Google Slides forniti contengono la stessa
immagine (`md5` identico) e portano il vecchio logotipo Mignon.Wine, quindi il
logotipo attuale non era disponibile. `mignonexperience.com` e il dominio di
download di Canva sono bloccati dalla policy di rete della sessione. Con il
file ufficiale, la sostituzione è immediata.

## Esportazioni

`render.mjs` renderizza le tavole con Chromium incorporando i font
(`fonts.mjs` li scarica una volta sola). `pptx_slides.py` ricostruisce le
tavole come PPTX nativi, `svg_build.py` converte i PDF in SVG vettoriali.

| Formato | Cartella | Testo modificabile |
|---|---|---|
| PNG alla misura reale | `export/` | no |
| PDF vettoriale | `export/` | sì |
| SVG | `export/svg/` | sì |
| PPTX (3 file, uno per formato) | `export/` | sì |

## Versioni Canva

Rigenerate su Canva il 22/08/2026 con il generatore AI. Non sono conversioni
delle tavole: Canva rigenera da un brief testuale, quindi impaginazione e resa
differiscono. Esito verificato tavola per tavola.

| Tavola | Canva | Esito |
|---|---|---|
| Direzione A | [modifica](https://www.canva.com/d/E3x6KDkFCoEYeuS) | usabile |
| Direzione A (1º tentativo) | [modifica](https://www.canva.com/d/9t0z4WX80BUq-os) | da eliminare |
| Direzione B | [modifica](https://www.canva.com/d/FJZZACNF8mE9aMp) | da eliminare |
| Direzione B (1º tentativo) | [modifica](https://www.canva.com/d/K3WXE5XYt3qjsHA) | da eliminare — testimonianza inventata |
| Direzione C | [modifica](https://www.canva.com/d/tULfrlU6R2ig6_o) | debole |
| Composizione | [modifica](https://www.canva.com/d/E_MJkK6xuTYZ1di) | da sistemare |
| Dentro una casella | [modifica](https://www.canva.com/d/oqmdbMJrQkmNTlM) | da eliminare |
| Packaging | [modifica](https://www.canva.com/d/gcT5WgoseP4XA_o) | da eliminare |
| Story arrivo a casa | [modifica](https://www.canva.com/d/ZyCXU7i3V5OhK8H) | buona |
| Situazioni di consumo | [modifica](https://www.canva.com/d/xfPgyKv0SyeV682) | da eliminare |
| Story rituale | [modifica](https://www.canva.com/d/h2FUrOYAbZrsyOa) | parziale |
| Sei piste (presentazione) | [modifica](https://www.canva.com/d/TRFZorOxh028ksQ) | buona |
| Template post quotidiano | [modifica](https://www.canva.com/d/qWfGRIBYduj5bGY) | da eliminare |
