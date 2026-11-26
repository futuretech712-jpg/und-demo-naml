# NAML 2027 – postavljanje na WordPress.com (naml2027.org)

"Copy site" ne postoji jer ga može pokrenuti samo vlasnik stranice, i to samo na Business ili Commerce planu. Zato se stranica slaže iznova od HTML blokova iz mape `wordpress/`.

## 0. Plan nove stranice i hosting značajke
Blokovi koriste `<style>`, `<link>` (fontove), `<script>` i `<iframe>` (Underline program). Prema dokumentaciji WordPress.coma (studeni 2026) pluginovi i vlastiti kod dostupni su na svim plaćenim planovima (Personal, Premium, Business, Commerce), ali tek kad se na stranici **uključe hosting značajke**. Prije toga vrijede ista ograničenja kao na besplatnim stranicama.
- **Premium je dovoljan** (naml2026.org je na Premiumu i koristi Elementor).
- Na novoj stranici **uključi hosting značajke** prije lijepljenja blokova. Ako se blok nakon spremanja "pokvari" ili kod nestane, hosting značajke nisu uključene.

## 1. Nova stranica
Sites → **Add new site** → naziv "NAML 2027 – Naval Applications of Machine Learning" → odaberi plan. Za temu je dovoljna bilo koja block tema, npr. Twenty Twenty-Five.

## 2. Domena naml2027.org
Domena je trenutno pod stranicom naml2026.org (registrirana tamo).
1. Otvori naml2026.org → **Domains** → **naml2027.org** → **Settings**.
2. Odaberi **Transfer / Move to another WordPress.com site** i izaberi novu stranicu. To može samo vlasnik domene, a to je račun koji ju je kupio.
3. Na novoj stranici: **Domains** → naml2027.org → **Make primary**.

## 3. Stranice (slug mora biti točno ovakav)
| Stranica | Slug | Datoteka |
|---|---|---|
| Home | (naslovna) | `wordpress/index.html` |
| Call for Participation | `call-for-participation` | `wordpress/call-for-participation.html` |
| Agenda | `agenda` | `wordpress/agenda.html` |
| Venues | `venues` | `wordpress/venues.html` |
| Organizers | `organizers` | `wordpress/organizers.html` |
| Sponsors | `sponsors` | `wordpress/sponsors.html` |
| Previous Workshops | `previous-workshops` | `wordpress/previous-workshops.html` |

Za svaku stranicu:
1. Pages → **Add new**, upiši naslov i provjeri slug.
2. Dodaj jedan **Custom HTML** blok (upiši `/html`) i zalijepi cijeli sadržaj datoteke.
3. Pod Template odaberi praznu varijantu bez naslova ("Blank" ili "No title"), da tema ne ispisuje svoj naslov iznad bloka.

Home postavi kao naslovnicu: **Settings → Reading → Your homepage displays → A static page → Home**.

## 4. Izbornik (header) i footer
Appearance → **Editor** → **Patterns** → **Template parts**:
- **Header:** obriši sadržaj teme i dodaj jedan Custom HTML blok sa sadržajem `wordpress/_header.html`. To je izbornik s logom, Submit gumbom i mobilnim izbornikom, i radi bez JavaScripta.
- **Footer:** isto, sa sadržajem `wordpress/_footer.html`.

## 5. Ikona stranice (favicon)
**Settings → General → Site icon**: uploadaj `assets/img/site-icon-512.png` (stisnuti NAML logo).

## 6. Slike i datoteke
U blokovima se slike, OG slika i `.ics` datoteke učitavaju s GitHub Pagesa (`futuretech712-jpg.github.io/und-demo-naml`).
- Ili uključi GitHub Pages (repo → Settings → Pages → main / root),
- ili sve iz `assets/img` i `assets/cal` uploadaj u Media Library. Onda u `build.py` promijeni `SITE_URL`, pokreni `python3 build.py` i ponovno zalijepi blokove.

Fotografije organizatora i logotipi sponzora još se učitavaju s naml2026.org. Dok je ta stranica online, rade. Za stalno rješenje i njih prebaci u Media Library.

## 7. Provjera
Otvori svaku stranicu na računalu i mobitelu. Na naslovnici kratko treba bljesnuti loading ekran (radar s logom), a izbornik na mobitelu se treba otvarati i zatvarati.
