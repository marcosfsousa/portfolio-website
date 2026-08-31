# PROTOTYPE — throwaway. Anchors the measure claim on issue #4 change 4.
# Two independent mechanisms (fontTools hmtx tables, PIL rasterizer) must agree
# before any chars-per-line number is reported.
from fontTools.ttLib import TTFont
from PIL import ImageFont

PARA = ("An MCP server over a mock purchase-to-pay ERP. Two callers ask the same endpoint "
        "the same question and get different answers. A tool a caller may not reach is absent "
        "rather than refused. docs/walkthrough.md follows one from the login screen onward, "
        "every wire exchange copied from a capture a test checks it against.")
SIZE = 18.5
faces = {
    "Sitka Text (what Win11 renders)": (r"C:\Windows\Fonts\SitkaVF.ttf", 0),
    "Cambria (next fallback)":         (r"C:\Windows\Fonts\cambria.ttc", 0),
    "Georgia (last named fallback)":   (r"C:\Windows\Fonts\georgia.ttf", 0),
}

print(f"{'face':34} {'avg px/char':>11} {'rem@65ch':>9} {'rem@75ch':>9}")
rows = []
for name, (p, n) in faces.items():
    f = TTFont(p, fontNumber=n)
    upem, cmap, hmtx = f['head'].unitsPerEm, f.getBestCmap(), f['hmtx']
    avg = sum(hmtx[cmap[ord(c)]][0] for c in PARA if ord(c) in cmap) / len(PARA) / upem * SIZE
    pil = ImageFont.truetype(p, int(round(SIZE))).getlength(PARA) / len(PARA)
    assert abs(avg - pil) / avg < 0.06, (name, avg, pil)   # the two mechanisms must agree
    rows.append((name, avg))
    print(f"{name:34} {avg:11.2f} {65*avg/16:9.1f} {75*avg/16:9.1f}")

print()
for w in (33, 36, 37, 38, 39, 40):
    span = ", ".join(f"{n.split(' (')[0]}: {w*16/a:.0f}" for n, a in rows)
    ok = all(65 <= w * 16 / a <= 75 for _, a in rows)
    print(f"max-width {w}rem -> {span}" + ("   <-- all inside 65-75" if ok else ""))
