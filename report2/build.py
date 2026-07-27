"""Assemble report2/index.html + artifact.html from template.html + p1/out figures.
Refuses to build while any PENDING-LIT slot remains."""
import base64
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
FIG_DIR = HERE.parent / "p1" / "out"
FIGS = ["p1_e1_closure", "p1_e2_dft", "p1_e3_extensivity", "p1_e4_quantum"]

tpl = (HERE / "template.html").read_text()
if "PENDING-LIT" in tpl:
    sys.exit("refusing to build: PENDING-LIT slots remain in template.html")

for name in FIGS:
    imgs = []
    for mode in ("light", "dark"):
        b64 = base64.b64encode((FIG_DIR / f"{name}_{mode}.svg").read_bytes()).decode()
        imgs.append(f'<img class="fig fig-{mode}" alt="" src="data:image/svg+xml;base64,{b64}">')
    tpl = tpl.replace("{{FIG:" + name + "}}", "\n".join(imgs))

leftover = re.findall(r"\{\{[^}]+\}\}", tpl)
if leftover:
    sys.exit(f"refusing to build: unexpanded tokens {leftover}")

(HERE / "artifact.html").write_text(tpl)
standalone = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
    "</head>\n<body>\n" + tpl + "\n</body>\n</html>\n"
)
(HERE / "index.html").write_text(standalone)
print("wrote index.html + artifact.html", f"({len(tpl) / 1024:.0f} KB content)")
