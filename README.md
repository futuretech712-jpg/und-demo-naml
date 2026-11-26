# NAML 2027 – demo site

Demo of the NAML 2027 (Naval Applications of Machine Learning) website in the official NAML 2027 palette, built as plain HTML so every page can later be moved into WordPress/Elementor.

**Live demo:** https://futuretech712-jpg.github.io/und-demo-naml/

## Pages

| Page | Demo file | WordPress block |
|---|---|---|
| Home | `index.html` | `wordpress/index.html` |
| Registration | `registration.html` | `wordpress/registration.html` |
| Agenda (NAML 2027) | `agenda.html` | `wordpress/agenda.html` |
| Venues | `venues.html` | `wordpress/venues.html` |
| Organizers | `organizers.html` | `wordpress/organizers.html` |
| Sponsors | `sponsors.html` | `wordpress/sponsors.html` |
| Previous workshops (2021–2026 + NAML 2026 program embed) | `previous-workshops.html` | `wordpress/previous-workshops.html` |

## Structure

```
assets/css/naml.css   shared styles (all scoped under .naml)
assets/js/naml.js     menu, countdown, sonar network
assets/img/           NAML 2027 logos, favicon
src/pages/            page content (edit these)
src/svg/              drawn illustrations
build.py              builds the demo pages and the WordPress blocks
wordpress/            generated: one self-contained block per page
```

Edit files in `src/` or `assets/`, then run:

```
python3 build.py
```

## Moving a page to WordPress

1. Create the page in WordPress (slugs: `call-for-participation`, `agenda`, `venues`, `sponsors`, `previous-workshops`).
2. In Elementor add a Full Width section with 0 padding and an **HTML** widget.
3. Paste the whole matching file from `wordpress/`.
4. Upload the logos from `assets/img/` to the Media Library and replace the image URLs (they point to this GitHub Pages site for now).

The WordPress blocks contain no header or footer, since the WordPress theme provides those.

## Agenda

`agenda.html` is ready for the NAML 2027 program. When the event exists on Underline, uncomment the iframe in `src/pages/agenda.html`, put in the event ID and rebuild.
