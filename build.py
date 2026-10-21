#!/usr/bin/env python3
"""Static build: data/countries/*.yaml -> country pages, data/guides/*.md -> guides."""
import shutil, datetime, pathlib, yaml, markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
R = pathlib.Path(__file__).parent; OUT = R / "dist"
site = yaml.safe_load((R/"site.yaml").read_text())
env = Environment(loader=FileSystemLoader(R/"templates"), autoescape=select_autoescape())
md = lambda t: markdown.markdown(t or "", extensions=["tables"])
env.filters["md"] = md
from urllib.parse import urlparse
env.globals["root"] = urlparse(site["base_url"]).path.rstrip("/")
shutil.rmtree(OUT, ignore_errors=True); (OUT/"static").mkdir(parents=True)
for f in (R/"static").iterdir(): shutil.copy(f, OUT/"static"/f.name)
urls = ["/"]
def write(path, tpl, **ctx):
    p = OUT/path.strip("/")/"index.html" if path != "/" else OUT/"index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(env.get_template(tpl).render(site=site, path=path, **ctx), encoding="utf-8")
countries = []
for f in sorted((R/"data/countries").glob("*.yaml")):
    c = yaml.safe_load(f.read_text()); c["slug"] = f.stem; c["url"] = f"/esim/{f.stem}/"
    countries.append(c); write(c["url"], "country.html", c=c, page_title=c["title"], page_desc=c["description"]); urls.append(c["url"])
guides = []
for f in sorted((R/"data/guides").glob("*.md")):
    _, fm, body = f.read_text().split("---", 2); g = yaml.safe_load(fm)
    g["slug"] = f.stem; g["url"] = f"/guide/{f.stem}/"; g["html"] = md(body)
    guides.append(g); write(g["url"], "guide.html", g=g, page_title=g["title"], page_desc=g["description"]); urls.append(g["url"])
write("/", "index.html", countries=countries, guides=guides, page_title=site["title"], page_desc=site["description"])
write("/disclosure/", "disclosure.html", page_title="제휴 링크 고지", page_desc="이 사이트의 제휴 링크와 수익 구조 안내"); urls.append("/disclosure/")
today = datetime.date.today().isoformat()
sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{site['base_url'].rstrip('/')}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
(OUT/"sitemap.xml").write_text("\n".join(sm+["</urlset>"])+"\n")
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {site['base_url'].rstrip('/')}/sitemap.xml\n")
print(f"built {len(urls)} pages -> {OUT}")
