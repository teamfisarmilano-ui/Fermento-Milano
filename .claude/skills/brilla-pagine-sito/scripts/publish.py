#!/usr/bin/env python3
"""Crea (o aggiorna) una pagina WordPress da un file di markup a blocchi.

Uso:
  WP_URL=https://ilbrilla.com WP_USER=utente WP_APP_PASSWORD='xxxx xxxx ...' \
  python3 publish.py --file home.html --title Home --slug home [--id 123] [--status draft]

Default: bozza. Rifiuta di pubblicare se restano {{SEGNAPOSTO}}.
"""
import argparse, base64, json, os, re, sys, urllib.request

p = argparse.ArgumentParser()
p.add_argument("--file", required=True)
p.add_argument("--title", required=True)
p.add_argument("--slug")
p.add_argument("--id", type=int, help="ID pagina esistente da aggiornare")
p.add_argument("--status", default="draft", choices=["draft", "pending", "private", "publish"])
a = p.parse_args()

content = open(a.file, encoding="utf-8").read()
left = sorted(set(re.findall(r"\{\{[^}]+\}\}", content)))
if left and a.status != "draft":
    sys.exit("Segnaposto rimasti, pubblico solo come bozza:\n  " + "\n  ".join(left))
if left:
    print("Attenzione, segnaposto ancora presenti:", *left, sep="\n  ")

base = os.environ["WP_URL"].rstrip("/")
auth = base64.b64encode(f'{os.environ["WP_USER"]}:{os.environ["WP_APP_PASSWORD"]}'.encode()).decode()
body = {"title": a.title, "content": content, "status": a.status}
if a.slug:
    body["slug"] = a.slug
url = f"{base}/wp-json/wp/v2/pages" + (f"/{a.id}" if a.id else "")
req = urllib.request.Request(url, json.dumps(body).encode(), method="POST",
                             headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
with urllib.request.urlopen(req) as r:
    d = json.load(r)
print(d["id"], d["status"], d["link"])
