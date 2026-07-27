"""Assemble report/index.html from template.html + toys/out figures.

Refuses to build while any PENDING-LIT literature slot remains unfilled,
so an unfinished report can't ship by accident.
"""
import base64
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT_FIGS = HERE.parent / "toys" / "out"
FIGS = ["tm1_loopmap", "tm2_roots", "tm3_qubit", "tm4_horizon", "tm6_winding"]

tpl = (HERE / "template.html").read_text()

if "PENDING-LIT" in tpl:
    sys.exit("refusing to build: PENDING-LIT slots remain in template.html")

for name in FIGS:
    imgs = []
    for mode in ("light", "dark"):
        svg = (OUT_FIGS / f"{name}_{mode}.svg").read_bytes()
        b64 = base64.b64encode(svg).decode()
        imgs.append(
            f'<img class="fig fig-{mode}" alt="" '
            f'src="data:image/svg+xml;base64,{b64}">'
        )
    tpl = tpl.replace("{{FIG:" + name + "}}", "\n".join(imgs))

leftover = re.findall(r"\{\{[^}]+\}\}", tpl)
if leftover:
    sys.exit(f"refusing to build: unexpanded tokens {leftover}")

# artifact.html: bare content (the Artifact publisher supplies the document skeleton)
(HERE / "artifact.html").write_text(tpl)

# index.html: standalone copy for direct viewing from the repo
standalone = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
    "</head>\n<body>\n" + tpl + "\n</body>\n</html>\n"
)
(HERE / "index.html").write_text(standalone)
print("wrote index.html + artifact.html", f"({len(tpl) / 1024:.0f} KB content)")
