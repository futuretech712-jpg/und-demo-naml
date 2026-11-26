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
Svaka datoteka u `wordpress/` sadrži cijelu stranicu: naš header s izbornikom, sadržaj i footer. Sama se širi preko cijelog ekrana, bez obzira na temu.

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
1. Pages > Add New Page, upiši naslov i provjeri slug (desno, Page > URL).
2. Dodaj jedan Custom HTML blok (`/html`) i zalijepi cijeli sadržaj datoteke.
3. Desno pod Template odaberi **Blank**, da se ne prikazuju header i footer teme.
4. Publish.

Home postavi kao naslovnicu: Settings > Reading > A static page > Homepage: Home.

## 4. Header i footer
Nije potrebno ništa mijenjati u temi, jer su header i footer ugrađeni u svaku stranicu. `wordpress/_header.html` i `_footer.html` služe samo ako ih poželiš staviti u template parts teme.

## 5. Ikona stranice (favicon)
**Settings → General → Site icon**: uploadaj `assets/img/site-icon-512.png` (stisnuti NAML logo).

## 6. Slike i datoteke
U blokovima se slike, OG slika i `.ics` datoteke učitavaju s GitHub Pagesa (`futuretech712-jpg.github.io/und-demo-naml`).
- Ili uključi GitHub Pages (repo → Settings → Pages → main / root),
- ili sve iz `assets/img` i `assets/cal` uploadaj u Media Library. Onda u `build.py` promijeni `SITE_URL`, pokreni `python3 build.py` i ponovno zalijepi blokove.

Fotografije organizatora i logotipi sponzora još se učitavaju s naml2026.org. Dok je ta stranica online, rade. Za stalno rješenje i njih prebaci u Media Library.

## 7. Provjera
Otvori svaku stranicu na računalu i mobitelu. Na naslovnici kratko treba bljesnuti loading ekran (radar s logom), a izbornik na mobitelu se treba otvarati i zatvarati.
