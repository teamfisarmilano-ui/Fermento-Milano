---
name: brilla-pagine-sito
description: Crea e pubblica le pagine del sito ilbrilla.com (WordPress + WooCommerce + tema Neve) come markup a blocchi Gutenberg importabile. Usare quando si chiede di creare, rifare o aggiornare una pagina del sito Brilla (home, landing stagionali, pagine collezione, pagine categoria), di "importare HTML in WordPress" o di preparare hero, caroselli prodotto e sezioni collezioni per Brilla.
---

# Brilla — creazione pagine sito

Sito: **ilbrilla.com** · WordPress + WooCommerce + tema **Neve**.
Prodotti: collanine. Best seller fissi: **Champagne, Spritz, Barolo**.
Linee stagionali/speciali: categoria *speciali/stagionali* (es. Halloween, 10 versioni).

## Regola di base: mai HTML libero, sempre blocchi

L'editor di WordPress (Gutenberg) accetta il codice solo in due modi utili:

1. **Markup a blocchi** (`<!-- wp:group --> ... <!-- /wp:group -->`): incollato nell'*Editor del codice* (Ctrl+Maiusc+Alt+M) o inviato via REST API diventa blocchi normali, modificabili con l'editor visuale. È il formato di questa skill.
2. **HTML grezzo** in un blocco "HTML personalizzato": funziona, ma resta una scatola opaca (niente modifica visuale, niente stili Neve, niente immagini dalla libreria). Usarlo solo per snippet piccoli, mai per una pagina.

Una pagina HTML intera (`<html><head>…`) incollata nell'editor perde `<head>`, CSS e script. Non generarla.

## Flusso di lavoro

1. Chiarire con l'utente: pagina, obiettivo, ID prodotti / slug categorie, immagini già caricate in libreria media (URL o ID). Non inventare ID, prezzi, nomi collezione: lasciarli come `{{SEGNAPOSTO}}` e dirlo.
2. Partire da `templates/home.blocks.html` (home) e adattarlo. Una sezione = un `wp:group` con `align="full"`, così Neve non la restringe.
3. Prodotti: usare lo shortcode WooCommerce in un blocco `wp:shortcode` (`[products ids="…"]`, `[products category="slug"]`). È stabile tra versioni di WooCommerce, i blocchi prodotto no.
4. Caroselli: CSS scroll-snap senza JS e senza plugin → `templates/brilla-carousel.css` (da incollare in Aspetto → Personalizza → CSS aggiuntivo, una sola volta). Le sezioni carosello portano la classe `brilla-carousel`.
5. Salvare il risultato in un file `.html` e fornirlo all'utente, oppure pubblicarlo come **bozza** con `scripts/publish.py` (mai `publish` senza richiesta esplicita).
6. Controllo finale: vedi checklist.

## Importare in WordPress

| Metodo | Quando | Come |
|---|---|---|
| Editor del codice | Una pagina, a mano | Nuova pagina → ⋮ → *Editor del codice* → incolla il file `.blocks.html` → torna a *Editor visuale* |
| REST API | Automatico, ripetibile | `python3 scripts/publish.py --file pagina.html --title "Home" --slug home` con `WP_URL`, `WP_USER`, `WP_APP_PASSWORD` (Utenti → Profilo → Password applicazione) |
| Pattern sincronizzato | Sezioni riusabili (es. banner stagionale) | Incollare la sezione, ⋮ → *Crea pattern* |

Le immagini: il markup deve puntare a file **già in libreria media** (URL `/wp-content/uploads/...`). L'import non carica file. Caricarle prima (Media → Aggiungi, oppure `POST /wp-json/wp/v2/media`), in WebP, e usare quegli URL.

## Struttura Home (decisa con l'utente)

1. **Hero** — `wp:cover`, immagine scenario con 3 collanine (generata con Nano Banana a partire dalle foto reali), titolo, sottotitolo, 1 pulsante → shop.
2. **Shop** — titolo + riga fissa con **Champagne, Spritz, Barolo** in primo piano (`[products ids="…" columns="3"]`), sotto/seguito dal carosello WooCommerce del resto del catalogo.
3. **Speciali / stagionali** — carosello immagini dalla **categoria**, non da immagini incollate a mano (`[products category="speciali" limit="12"]`): a fine stagione si cambia lo slug o si nascondono i prodotti, la pagina non va rifatta. Titolo stagionale in un pattern sincronizzato.
4. **Le tre linee di collezione** — `wp:columns` a 3 colonne: immagine, nome, 1 riga, link alla categoria. Nomi e link: `{{COLLEZIONE_1..3}}` finché l'utente non li fornisce.

## Regole di contenuto e qualità

- **Immagini generate con AI**: devono partire dai prodotti reali e non alterare forma, maglia, ciondolo, colori. Il cliente deve ricevere ciò che vede (Codice del consumo: pratica ingannevole). Nella scheda prodotto restano le foto reali. Controllo umano su ogni immagine hero prima della pubblicazione.
- **Hero e LCP**: una sola immagine hero, WebP, ≤ 200 KB desktop, versione mobile separata (soggetto centrato), mai lazy-load sull'hero. Altre immagini: lazy-load.
- **Mobile first**: Neve ha traffico prevalentemente mobile per l'e-commerce; testare a 390 px. Nel carosello mostrare ~1,5 card per far intuire lo scorrimento.
- **Un solo H1** per pagina (nell'hero). Testo alternativo descrittivo su ogni immagine (es. "Collanina Champagne Brilla indossata"), non "img1".
- **Un obiettivo per sezione**, un solo pulsante principale per sezione. Link a categoria/prodotto, mai a `#`.
- **Tono, palette, font**: `{{DA COMPILARE}}` — non esistono ancora nel repo. Chiederli o leggerli dal sito prima di scrivere copy o colori; usare le variabili colore di Neve (`var(--nv-primary-accent)`) invece di esadecimali fissi, così la pagina segue il tema.
- Lingua del sito: italiano.

## Checklist prima di consegnare

- [ ] Nessun `{{SEGNAPOSTO}}` rimasto, oppure elencati all'utente
- [ ] ID prodotti e slug categoria verificati (WooCommerce → Prodotti)
- [ ] Il file si apre nell'editor visuale senza "Il blocco contiene contenuto imprevisto"
- [ ] Un H1, alt su tutte le immagini, pulsanti con link reale
- [ ] Controllata anteprima mobile e desktop
- [ ] Pagina creata come **bozza**

## Limiti noti

- Template e script **non sono stati provati su ilbrilla.com** (sessione senza accesso al sito): la prima importazione va fatta su una bozza.
- Neve può sovrascrivere larghezze e margini dei blocchi: se la sezione non è a tutta larghezza, impostare *Layout → Contenuto → Larghezza piena* sulla pagina.
