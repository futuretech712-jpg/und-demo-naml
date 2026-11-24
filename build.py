#!/usr/bin/env python3
"""Build the NAML 2027 demo site and the WordPress/Elementor HTML blocks.

  python3 build.py

src/pages/*.html  -> ./<page>.html          (demo site with header, menu and footer)
                  -> wordpress/<page>.html  (one self-contained block per page for an
                                             Elementor HTML widget: fonts + CSS + content + JS)
Placeholders in pages: {{base}} asset path, {{link:page}} internal link, {{svg:name}} illustration.
"""
import pathlib, re, hashlib

ROOT = pathlib.Path(__file__).parent
SITE_URL = "https://futuretech712-jpg.github.io/und-demo-naml/"  # used for images in WordPress blocks
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap">'

MENU = [  # (page, label)
    ("index", "Home"),
    ("call-for-participation", "Call for Participation"),
    ("agenda", "Agenda"),
    ("venues", "Venues"),
    ("organizers", "Organizers"),
    ("sponsors", "Sponsors"),
    ("previous-workshops", "Previous Workshops"),
]

def site_link(p): return "index.html" if p == "index" else f"{p}.html"
def wp_link(p): return "/" if p == "index" else f"/{p}/"

def render(body, link, base):
    body = re.sub(r"\{\{part:([\w-]+)\}\}", lambda m: (ROOT / "src/parts" / f"{m[1]}.html").read_text().strip(), body)
    body = re.sub(r"\{\{svg:([\w-]+)\}\}", lambda m: (ROOT / "src/svg" / f"{m[1]}.svg").read_text().strip(), body)
    body = re.sub(r"\{\{link:([\w-]+)\}\}", lambda m: link(m[1]), body)
    return body.replace("{{base}}", base)

def header(active, link=None, base=""):
    """Site header. Desktop nav + a JS-free mobile menu (<details>), so it also works on WordPress plans that strip scripts."""
    link = link or site_link
    def items(cls):
        return "\n".join(
            f'          <a href="{link(p)}"{" aria-current=\"page\"" if p == active else ""}>{label}</a>' for p, label in MENU)
    return f'''<header class="top">
    <div class="wrap">
      <a class="brand" href="{link("index")}" aria-label="NAML 2027 home"><img src="{base}assets/img/naml27-logo-color.webp" alt="NAML, Naval Applications of Machine Learning" width="807" height="425"></a>
      <nav class="menu" aria-label="Main">
{items("d")}
      </nav>
      <a class="btn pri hsub" href="https://go.mil/naml2027sub" target="_blank" rel="noopener">Submit abstract</a>
      <details class="mnav">
        <summary aria-label="Open menu"><span class="bars" aria-hidden="true"><i></i><i></i><i></i></span><span class="lbl"></span></summary>
        <nav aria-label="Main (mobile)">
{items("m")}
          <a class="btn pri" href="https://go.mil/naml2027sub" target="_blank" rel="noopener">Submit abstract</a>
        </nav>
      </details>
    </div>
  </header>'''

FOOTER = '''<footer class="band foot" id="contact">
    <div class="wrap">
      <div>
        <img src="assets/img/naml27-logo-white.webp" alt="NAML" width="807" height="425">
        <p style="margin:0">The 11th Annual Workshop on Naval Applications of Machine Learning<br>April 12-15, 2027, San Diego, California</p>
      </div>
      <div>
        <h3>Workshop</h3>
        <ul>''' + "".join(f'<li><a href="{site_link(p)}">{l}</a></li>' for p, l in MENU[1:]) + '''<li><a href="index.html#faq">FAQ</a></li></ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="mailto:naml@us.navy.mil?subject=NAML%202027%20question">naml@us.navy.mil</a></li>
          <li><a href="https://go.mil/naml" target="_blank" rel="noopener">go.mil/naml</a></li>
          <li>Sponsorship: <a href="mailto:racurato@deloitte.com?subject=NAML%202027%20sponsorship">racurato@deloitte.com</a></li>
          <li>Platform, registration and Underline support: <a href="mailto:naml2027@underline.io?subject=NAML%202027%20registration%20%2F%20platform">naml2027@underline.io</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap fine"><span>NAML 2027. Organized by AFCEA San Diego and NIWC Pacific</span><span>Demo site</span></div>
  </footer>'''

def wp_footer():
    f = FOOTER.replace('href="index.html#faq"', 'href="/#faq"').replace('src="assets/', 'src="' + SITE_URL + 'assets/')
    return re.sub(r'href="([\w-]+)\.html"', lambda m: f'href="{wp_link(m[1])}"', f)

def main():
    css = (ROOT / "assets/css/naml.css").read_text()
    js = (ROOT / "assets/js/naml.js").read_text()
    ver = hashlib.md5((css + js).encode()).hexdigest()[:8]  # cache-busting
    # WordPress blocks ship without code comments
    css_wp = re.sub(r"/\*.*?\*/\s*", "", css, flags=re.S)
    js_wp = re.sub(r"^\s*//.*\n", "", re.sub(r"/\*.*?\*/\s*", "", js, flags=re.S), flags=re.M)
    (ROOT / "wordpress").mkdir(exist_ok=True)
    for src in sorted((ROOT / "src/pages").glob("*.html")):
        page = src.stem
        raw = src.read_text()
        title = re.search(r"title:\s*(.*?)\s*\|\s*nav:", raw)[1]
        body = re.sub(r"^<!--.*?-->\n", "", raw, count=1)

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="NAML 2027, the 11th Annual Workshop on Naval Applications of Machine Learning, April 12-15, 2027, San Diego, California.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="NAML 2027">
<meta property="og:title" content="{title}">
<meta property="og:description" content="Naval Applications of Machine Learning, April 12-15, 2027, San Diego, California. Abstracts due December 4, 2026.">
<meta property="og:image" content="{SITE_URL}assets/img/og-naml2027.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#02565E">
<link rel="icon" href="assets/img/favicon.ico" sizes="any">
<link rel="icon" href="assets/img/favicon.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="assets/css/naml.css?v={ver}">
<style>body{{margin:0}}html{{scroll-padding-top:90px}}</style>
</head>
<body>
<div class="naml">
  <a class="skip" href="#main">Skip to content</a>
  {header(page)}
  <main id="main" tabindex="-1">
{render(body, site_link, "")}
  </main>
  {FOOTER}
</div>
<script src="assets/js/naml.js?v={ver}"></script>
</body>
</html>
'''
        (ROOT / f"{page}.html").write_text(html)

        wp = f'''<!-- NAML 2027, {title}. WordPress/Elementor HTML widget block, generated by build.py. Do not edit by hand.
     Paste the whole file into one HTML widget in a Full Width section with 0 padding.
     Images load from {SITE_URL}; swap them for Media Library URLs before go-live. -->
{FONTS}
<style>
{css_wp}
</style>
<div class="naml">
{render(body, wp_link, SITE_URL)}
</div>
<script>
{js_wp}
</script>
'''
        (ROOT / "wordpress" / f"{page}.html").write_text(wp)
        print("built", page)

    # WordPress header block (paste into the theme's Header template part)
    hdr = f'''<!-- NAML 2027, HEADER block for the WordPress theme Header (Appearance > Editor > Patterns > Template parts > Header).
     Replace the theme's navigation with one Custom HTML block containing this file. No JavaScript needed. -->
{FONTS}
<style>
{css_wp}
</style>
<div class="naml">
  {header("", wp_link, SITE_URL)}
</div>
'''
    (ROOT / "wordpress" / "_header.html").write_text(hdr)
    ftr = f'''<!-- NAML 2027, FOOTER block for the WordPress theme Footer template part. Paste after _header.html CSS is on the page (or keep the <style> below). -->
{FONTS}
<style>
{css_wp}
</style>
<div class="naml">
  {wp_footer()}
</div>
'''
    (ROOT / "wordpress" / "_footer.html").write_text(ftr)
    print("built _header, _footer")

if __name__ == "__main__":
    main()
