"""Converte i PDF vettoriali delle tavole in SVG: testo e forme restano
vettoriali, quindi apribili e modificabili in Figma, Illustrator, Affinity."""
import fitz, pathlib, json

canvas = json.loads(pathlib.Path("canvas.json").read_text())
out = pathlib.Path("export/svg"); out.mkdir(parents=True, exist_ok=True)
for a in canvas["artboards"]:
    stem = a["file"].replace(".dc.html", "")
    doc = fitz.open(f"export/{stem}.pdf")
    svg = doc[0].get_svg_image(text_as_path=False)
    p = out / f"{stem}.svg"
    p.write_text(svg)
    print(f"{stem}.svg  {len(svg)//1024} KB")
