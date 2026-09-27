from html.parser import HTMLParser
from pathlib import Path

root = Path(__file__).parent / "dist"
pages = list(root.rglob("index.html"))
routes = {"/" if p.parent == root else "/" + p.parent.relative_to(root).as_posix() + "/" for p in pages}
errors = []

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs.get("src", ""))

for page in pages:
    parser = Parser()
    parser.feed(page.read_text(encoding="utf-8"))
    for href in parser.links:
        if href.startswith("/") and href.split("#")[0] not in routes:
            errors.append(f"{page}: broken link {href}")
    for src in parser.images:
        if src.startswith("/") and not (root / src.lstrip("/")).exists():
            errors.append(f"{page}: missing image {src}")

print(f"Checked {len(pages)} pages and {len(routes)} routes")
if errors:
    raise SystemExit("\n".join(errors))
