from pptx_build import *

# ---------------------------------------------------------------- 1080x1350
post = deck(1080, 1350)

def eyebrow(s, x, y, text, color, size=16, w=700, align="l"):
    txt(s, x, y, w, 30, text.upper(), size, SANS, color, align, spacing=size * 0.3)

# --- Main: Direzione A --------------------------------------------------
s = page(post, INK)
lockup(s, 72, 66, 112, 27, 11, PAPER, "A2968A")
txt(s, 600, 76, 408, 70, ["DIREZIONE A", "NOTTE DI DICEMBRE"], 16, SANS, "8E8378", "r",
    spacing=3.5, leading=1.9)
eyebrow(s, 72, 362, "Calendario dell'Avvento", ORANGE, 17)
txt(s, 72, 398, 950, 240,
    ["Ventiquattro sere.",
     [("Ventiquattro", {"italic": True, "color": YELLOW}), (" vini.", {})]],
    100, SERIF, PAPER, leading=0.98)
rule(s, 72, 650, 96, RED, 2)
txt(s, 72, 692, 730, 160,
    "Dal 1° al 24 dicembre apri una bottiglia mignon diversa: un assaggio serio, "
    "nel formato giusto per una sera qualunque.", 30, SANS, SOFT_D, leading=1.5)
for i, (num, cap, col) in enumerate([
        ("24", ["mignon,", "una per sera"], RED),
        ("[N]", ["cantine", "italiane"], ORANGE),
        ("[ML]", ["il formato", "di ogni mignon"], PURPLE),
        ("[€]", ["prezzo", "del cofanetto"], YELLOW)]):
    x = 72 + i * 240
    rule(s, x, 968, 216, "3A322C")
    txt(s, x, 988, 216, 60, num, 46, SERIF, col, leading=1.0)
    txt(s, x, 1052, 216, 70, cap, 19, SANS, "A2968A", leading=1.4)
txt(s, 72, 1258, 500, 30, "MIGNONEXPERIENCE.COM", 18, SANS, MUTED_D, spacing=2.5)
txt(s, 508, 1258, 500, 30, "1 — 24 DICEMBRE", 18, SANS, MUTED_D, "r", spacing=2.5)

# --- Direzione B --------------------------------------------------------
s = page(post, CREAM)
lockup(s, 56, 50, 88, 21, 9, "4A4A52", "8A8A92")
txt(s, 600, 60, 424, 70, ["DIREZIONE B", "CARTA & COLORE"], 15, GROTESK, "8A8177", "r",
    bold=True, spacing=3, leading=1.8)
txt(s, 56, 176, 900, 320,
    ["APRINE",
     [("UNA", {"color": RED}), (" ", {}), ("AL", {"color": ORANGE})],
     [("GIORNO", {"color": PURPLE})]],
    116, BLACK, "221E1B", leading=0.86)
txt(s, 56, 590, 640, 90,
    "Il calendario dell'Avvento di Mignon Experience: 24 caselle, 24 bottiglie mignon, "
    "zero cioccolatini.", 27, GROTESK, "4A443E", leading=1.45)
CELL, GAP, GY = 151, 12, 706
FILLED = {1: (RED, CREAM), 4: (ORANGE, CREAM), 8: (PURPLE, CREAM), 12: (YELLOW, "221E1B")}
for n in range(1, 13):
    r, c = divmod(n - 1, 6)
    x, y = 56 + c * (CELL + GAP), GY + r * (CELL + GAP)
    fill, fg = FILLED.get(n, ("EDE5D6", "7F7466"))
    box(s, x, y, CELL, CELL, fill=fill)
    txt(s, x, y + CELL / 2 - 28, CELL, 56, str(n), 40 if n < 10 else 36, BLACK, fg, "c",
        anchor="m")
txt(s, 56, 1042, 700, 34, "… e altre dodici, fino al 24.", 21, GROTESK, "6E6459")
rule(s, 56, 1240, 968, "221E1B", 3)
txt(s, 56, 1262, 600, 30, "DAL 1° AL 24 DICEMBRE", 17, GROTESK, "221E1B", bold=True, spacing=1.7)
txt(s, 500, 1262, 524, 30, "MIGNONEXPERIENCE.COM", 17, GROTESK, "8A8177", "r", bold=True,
    spacing=1.7)

# --- Direzione C --------------------------------------------------------
s = page(post, "E9E3D9")
lockup(s, 540, 96, 150, 36, 15, "4A4A52", "8A8A92", "c")
txt(s, 96, 380, 888, 260,
    ["Dicembre,", [("un sorso alla volta", {"italic": True})]],
    104, SERIF_C, "2E2A26", "c", leading=1.06)
box(s, 539, 664, 1, 72, fill="B7AFA2")
txt(s, 220, 774, 640, 160,
    "Ventiquattro bottiglie mignon, una per ogni sera dell'Avvento. Nessuna fretta, "
    "nessun rumore: solo il tempo di versare.", 25, SANS_M, "5C554C", "c", leading=1.7)
txt(s, 96, 1140, 888, 50, "1 — 24 DICEMBRE", 30, SERIF_C, PURPLE, "c", spacing=12)
txt(s, 96, 1214, 888, 30, "MIGNONEXPERIENCE.COM", 16, SANS_M, "6F6659", "c", spacing=3.8)

# --- Composizione -------------------------------------------------------
TYPE = {"b": YELLOW, "r": RED, "s": ORANGE, "d": PURPLE}
SEQ = "brsrdbrsbrdsbrsdrbsrdbr" + "b"
s = page(post, INK)
eyebrow(s, 64, 64, "1 · Da cosa è composto", ORANGE)
txt(s, 64, 100, 900, 100, "Cosa c'è dentro", 78, SERIF, PAPER, leading=1.0)
txt(s, 64, 208, 780, 80,
    "Ventiquattro caselle numerate, ventiquattro etichette diverse. Il colore della "
    "casella dice che cosa stai per versare.", 24, SANS, "B7AB9E", leading=1.5)
CELL, GAP, GY = 147, 14, 330
BOT = {YELLOW: "bottiglia-gialla.png", RED: "bottiglia-rossa.png",
       ORANGE: "bottiglia-arancio.png", PURPLE: "bottiglia-viola.png"}
for n in range(1, 25):
    r, c = divmod(n - 1, 6)
    x, y = 64 + c * (CELL + GAP), GY + r * (CELL + GAP)
    col = TYPE[SEQ[n - 1]]
    last = n == 24
    box(s, x, y, CELL, CELL, fill=YELLOW if last else None, line=None if last else col)
    pic(s, BOT[RED if last else col], x + CELL / 2 - 5, y + 30, 46)
    txt(s, x, y + 88, CELL, 40, str(n), 22, SERIF, INK if last else col, "c")
LEG = [("Bianchi", YELLOW), ("Rossi", RED), ("Bollicine", ORANGE), ("Dolci & passiti", PURPLE)]
rule(s, 64, 1000, 952, "3A322C")
for i, (lab, col) in enumerate(LEG):
    x = 64 + i * 240
    box(s, x, 1032, 14, 14, fill=col)
    txt(s, x + 26, 1026, 200, 30, lab, 20, SANS, SOFT_D)
txt(s, 64, 1258, 952, 30,
    "Ripartizione da confermare con la selezione definitiva — "
    "[N bianchi / N rossi / N bollicine / N dolci-passiti]", 19, SANS, MUTED_D)

# --- Composizione: dentro una casella -----------------------------------
s = page(post, INK2)
eyebrow(s, 64, 64, "1 · Da cosa è composto", ORANGE)
txt(s, 64, 100, 900, 100, "Dentro una casella", 76, SERIF, PAPER, leading=1.0)
pic(s, "bottiglia-rossa.png", 138, 300, 300)
box(s, 119, 640, 190, 118, line="4C423A")
txt(s, 137, 664, 160, 40, "Giorno 7", 26, SERIF, PAPER)
txt(s, 137, 702, 160, 60, ["[Cantina]", "[Etichetta · annata]"], 15, SANS, "9C9084", leading=1.4)
box(s, 177, 790, 74, 74, line="4C423A")
txt(s, 177, 814, 74, 30, "QR", 20, SANS, "9C9084", "c")
for i, (n, t, b) in enumerate([
        ("01", "La mignon", "Un'etichetta reale, imbottigliata nel formato mignon da [ML]: la stessa "
         "qualità della bottiglia intera, la quantità giusta per una persona."),
        ("02", "La scheda del giorno", "Cantina, territorio, vitigno, temperatura di servizio e una "
         "nota di degustazione in tre righe. Da leggere mentre il vino si apre."),
        ("03", "Il QR", "Porta alla voce del produttore — e alla bottiglia intera in enoteca, "
         "se la sera è andata bene.")]):
    y = 300 + i * 210
    txt(s, 420, y, 60, 50, n, 34, SERIF, [RED, ORANGE, PURPLE][i], leading=1.0)
    txt(s, 488, y - 4, 528, 44, t, 32, SANS, PAPER)
    txt(s, 488, y + 44, 528, 140, b, 22, SANS, DIM_D, leading=1.55)
rule(s, 64, 1240, 952, "3A322C")
txt(s, 64, 1264, 500, 30, "MIGNON EXPERIENCE", 18, SANS, MUTED_D, spacing=2.5)
txt(s, 516, 1264, 500, 30, "FORMATO E CONTENUTI DA CONFERMARE", 18, SANS, MUTED_D, "r", spacing=2.5)

# --- Packaging ----------------------------------------------------------
s = page(post, PAPER)
eyebrow(s, 64, 64, "2 · Arrivo a casa", RED)
txt(s, 64, 100, 900, 90, "Tre gesti, poi è dicembre", 68, SERIF, INK2, leading=1.0)
txt(s, 64, 196, 790, 80,
    "Il packaging è la prima degustazione: quello che si vede, si sente e si tiene in "
    "mano prima ancora di stappare.", 23, SANS, MUTED_L, leading=1.5)
STEPS = [("01", RED, "La scatola da spedizione", "E4DACB",
          "Cartone grezzo, nastro con il marchio, nessuna scritta che riveli il contenuto. "
          "Regge il corriere e protegge 24 vetri."),
         ("02", ORANGE, "Il cofanetto", INK2,
          "Coperchio scorrevole, interno scuro, il marchio in rilievo. Si apre una volta sola: "
          "da lì in poi resta sul tavolo per 24 giorni."),
         ("03", PURPLE, "Le 24 caselle", "E4DACB",
          "Alveoli in cartone riciclato, ogni bottiglia in piedi e numerata. Vuoto significa "
          "una sera passata: il cofanetto si svuota a vista.")]
BOTS = ["bottiglia-rossa.png", "bottiglia-arancio.png", "bottiglia-viola.png", "bottiglia-gialla.png"]
for i, (n, col, title, bg, body) in enumerate(STEPS):
    x = 64 + i * 318
    box(s, x, 330, 296, 300, fill=bg)
    for j in range(3 if i else 0):
        pic(s, BOTS[(i * 3 + j) % 4], x + 108 + j * 40, 420, 120)
    txt(s, x, 664, 296, 44, n, 30, SERIF, col, leading=1.0)
    txt(s, x, 712, 296, 74, title, 27, SANS, INK2, leading=1.2)
    txt(s, x, 796, 296, 200, body, 20, SANS, MUTED_L, leading=1.5)
rule(s, 64, 1246, 952, "D3C7B6")
txt(s, 64, 1268, 620, 30, "MOCKUP INDICATIVI — MATERIALI E FINITURE DA DEFINIRE", 18, SANS,
    MUTED_L, spacing=2.2)
txt(s, 700, 1268, 316, 30, "MIGNONEXPERIENCE.COM", 18, SANS, MUTED_L, "r", spacing=2.2)

# --- Relax --------------------------------------------------------------
s = page(post, INK)
eyebrow(s, 64, 64, "3 · Situazioni di consumo", PURPLE)
txt(s, 64, 100, 900, 100,
    [[("Una sera, ", {}), ("una sola", {"italic": True, "color": YELLOW})]],
    76, SERIF, PAPER, leading=1.0)
txt(s, 64, 208, 810, 80,
    "Il mignon toglie l'alibi della bottiglia aperta: si versa quando ne hai voglia, "
    "anche da soli, anche di martedì.", 23, SANS, DIM_D, leading=1.5)
TILES = [("Le 21:30", RED, "Cena finita, luci basse, un solo calice. Non è una degustazione: è la "
          "parte migliore della giornata."),
         ("Il libro lungo", ORANGE, "Due capitoli e mezzo bicchiere. La quantità giusta per finire "
          "il capitolo e non il libro."),
         ("L'ultima puntata", PURPLE, "Divano, coperta, la serie che stai finendo. Il vino della "
          "sera arriva già scelto: una decisione in meno."),
         ("A distanza", YELLOW, "Due calendari, due case, la stessa casella aperta alla stessa "
          "ora. Il brindisi arriva per telefono.")]
for i, (title, col, body) in enumerate(TILES):
    r, c = divmod(i, 2)
    x, y = 64 + c * 488, 340 + r * 424
    box(s, x, y, 464, 400, fill=INK3)
    box(s, x + 38, y + 38, 56, 56, line=col, lw=1.5)
    txt(s, x + 38, y + 208, 388, 60, title, 40, SERIF, PAPER, leading=1.0)
    txt(s, x + 38, y + 272, 388, 110, body, 21, SANS, "9C9084", leading=1.55)
rule(s, 64, 1240, 952, "3A322C")
txt(s, 64, 1264, 952, 30,
    "Da girare come serie foto/reel — stessa luce, stessa inquadratura, quattro sere diverse",
    19, SANS, MUTED_D)

# --- Template post quotidiano ------------------------------------------
s = page(post, INK)
eyebrow(s, 64, 64, "4 · Idee", ORANGE)
txt(s, 600, 64, 416, 30, "TEMPLATE POST QUOTIDIANO", 16, SANS, MUTED_D, "r", spacing=3.2)
txt(s, 64, 130, 260, 200, "7", 190, SERIF, YELLOW, "c", leading=0.8)
pic(s, "bottiglia-rossa.png", 155, 360, 330)
txt(s, 368, 140, 648, 30, "[REGIONE · DENOMINAZIONE]", 18, SANS, "8E8378", spacing=4.3)
txt(s, 368, 180, 648, 80, "[Nome etichetta]", 60, SERIF, PAPER, leading=1.06)
txt(s, 368, 268, 648, 40, "[Cantina] · [Annata]", 26, SANS, DIM_D)
for i, (k, v) in enumerate([("VITIGNO", "[Vitigno]"), ("SERVIZIO", "[XX]°C"),
                            ("AL NASO", "[Tre descrittori]"),
                            ("STASERA CON", "[Abbinamento in tre parole]")]):
    y = 360 + i * 76
    txt(s, 368, y + 4, 200, 30, k, 17, SANS, MUTED_D, spacing=2.7)
    txt(s, 568, y, 448, 36, v, 24, SANS, PAPER)
    rule(s, 368, y + 58, 648, "2E2721")
txt(s, 368, 700, 648, 120, "“[Una riga del produttore su questo vino.]”", 34, SERIF, YELLOW,
    italic=True, leading=1.4)
rule(s, 64, 1216, 952, "3A322C")
lockup(s, 64, 1216, 60, 17, 8, PAPER, "A2968A")
txt(s, 500, 1264, 516, 30, "LA BOTTIGLIA INTERA → IN ENOTECA", 18, SANS, MUTED_D, "r", spacing=2.9)

post.save("export/tavole-post-1080x1350.pptx")
print("tavole-post-1080x1350.pptx —", len(post.slides.__iter__.__self__._sldIdLst), "slide")

# ---------------------------------------------------------------- 1080x1920
story = deck(1080, 1920)

# --- Arrivo a casa ------------------------------------------------------
s = page(story, INK)
txt(s, 80, 150, 920, 40, "2 · ARRIVO A CASA", 20, SANS, ORANGE, "c", spacing=4.8)
txt(s, 80, 216, 920, 220, ["Ha suonato", "il corriere"], 96, SERIF, PAPER, "c", leading=1.04)
box(s, 230, 620, 620, 440, line="4C423A", lw=1.5)
for i in range(10):
    pic(s, BOTS[i % 4], 268 + i * 56, 700, 280)
txt(s, 150, 1180, 780, 130,
    "Dentro: 24 mignon in piedi, numerate, ognuna con la sua scheda. Nient'altro da fare "
    "fino al 1° dicembre.", 34, SANS, SOFT_D, "c", leading=1.5)
b = box(s, 320, 1420, 440, 100, line=YELLOW, lw=1.5)
txt(s, 320, 1450, 440, 40, "ORDINA ENTRO IL [DATA]", 28, SANS, YELLOW, "c", spacing=5.6)
txt(s, 80, 1600, 920, 40, "MIGNONEXPERIENCE.COM", 22, SANS, MUTED_D, "c", spacing=4.4)

# --- Rituale della sera -------------------------------------------------
s = page(story, INK3)
txt(s, 90, 140, 900, 40, "3 · SITUAZIONI DI CONSUMO", 20, SANS, PURPLE, "c", spacing=4.8)
txt(s, 90, 210, 900, 140, "17", 118, SERIF, YELLOW, "c", leading=1.0)
txt(s, 90, 356, 900, 40, "DICEMBRE", 24, SANS, "8E8378", "c", spacing=5.8)
txt(s, 90, 560, 900, 220,
    ["Stasera non decidi tu.", [("Decide la casella.", {"italic": True})]],
    74, SERIF, PAPER, "c", leading=1.16)
box(s, 539, 830, 1, 90, fill="4C423A")
txt(s, 140, 960, 800, 130,
    "Apri, versi, leggi tre righe sul produttore. Dieci minuti in cui non stai facendo altro.",
    32, SANS, DIM_D, "c", leading=1.6)
for i in range(4):
    pic(s, BOTS[i], 400 + i * 76, 1300, 300)
lockup(s, 540, 1580, 190, 46, 19, PAPER, "A2968A", "c")

story.save("export/tavole-story-1080x1920.pptx")

# ---------------------------------------------------------------- 1440x1080
land = deck(1440, 1080)
s = page(land, PAPER)
eyebrow(s, 64, 56, "4 · Idee", "C4650B")
txt(s, 64, 92, 800, 80, "Sei piste da valutare", 62, SERIF, INK2, leading=1.0)
txt(s, 976, 70, 400, 100,
    "Sei modi di far durare il cofanetto oltre il 24 dicembre: prima di comprarlo, "
    "mentre lo si apre, dopo che è finito.", 19, SANS, DIM_L, "r", leading=1.5)
IDEE = [("01", RED, "Il calendario è un catalogo",
         "Il QR di ogni casella porta alla bottiglia intera, acquistabile subito. Ventiquattro "
         "sere di assaggio diventano ventiquattro occasioni di vendita.", "VENDITA · E-COMMERCE"),
        ("02", ORANGE, "La casella 25",
         "Una casella in più, oltre le 24: non contiene vino ma un invito. Una degustazione "
         "guidata, una visita in cantina, una serata. Il cofanetto finisce, l'esperienza no.",
         "RETENTION · EVENTI"),
        ("03", PURPLE, "Il calendario a due",
         "Due mignon per casella, oppure due cofanetti gemelli a due indirizzi diversi. Stessa "
         "etichetta, stessa sera, due case: il regalo è il brindisi a distanza.",
         "REGALO · SCONTRINO DOPPIO"),
        ("04", YELLOW, "Le 24 carte",
         "Le schede del giorno sono perforate: si staccano e a fine dicembre formano un mazzo "
         "di 24 carte. Il diario della degustazione, e la spesa di gennaio.",
         "PRODOTTO · RICORDO"),
        ("05", RED, "Ventiquattro sere in diretta",
         "Ogni sera un micro-video verticale di un minuto: si apre la casella, il produttore "
         "dice tre cose sul suo vino, fine. Ventiquattro uscite già scritte.",
         "CONTENUTO · 24 USCITE"),
        ("06", PURPLE, "Versione da banco",
         "Lo stesso calendario per enoteche e wine bar: la casella del giorno è il calice del "
         "giorno, esposto al banco con la sua scheda. Contenuto quotidiano pronto.",
         "HO.RE.CA · B2B")]
NUMCOL = {RED: RED, ORANGE: "C4650B", PURPLE: PURPLE, YELLOW: "9A7D08"}
CW, CH = 423, 369
for i, (n, col, title, body, tag) in enumerate(IDEE):
    r, c = divmod(i, 3)
    x, y = 64 + c * (CW + 22), 190 + r * (CH + 22)
    box(s, x, y, CW, CH, fill=WHITE)
    rule(s, x, y, CW, col, 4)
    txt(s, x + 28, y + 28, 100, 44, n, 30, SERIF, NUMCOL[col], leading=1.1)
    txt(s, x + 28, y + 76, CW - 56, 70, title, 27, SANS, INK2, leading=1.2)
    txt(s, x + 28, y + 158, CW - 56, 150, body, 18, SANS, DIM_L, leading=1.55)
    txt(s, x + 28, y + CH - 46, CW - 56, 30, tag, 16, SANS, "6F6859", spacing=2.2)
rule(s, 64, 992, 1312, "D3C7B6")
txt(s, 64, 1014, 1312, 30,
    "Proposte da validare — nessun accordo con cantine, prezzo o disponibilità è stato verificato",
    18, SANS, MUTED_L)
land.save("export/tavole-idee-1440x1080.pptx")
print("PPTX creati")
