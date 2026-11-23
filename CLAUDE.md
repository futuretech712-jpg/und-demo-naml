# NAML 2027 demo site – upute za Claude

Korisnik (Rafael, Underline Science) piše na hrvatskom i šalje izmjene koje traži klijent (NAML / AFCEA San Diego / NIWC Pacific). Odgovaraj na hrvatskom (latinica), kratko. Svaku izmjenu napravi, pokreni build, provjeri i pushaj na `main`.

## Što je ovo
Višestranični demo web za NAML 2027 (Naval Applications of Machine Learning, 11th Annual Workshop, April 12–15, 2027, San Diego). Kasnije se svaka stranica prebacuje u WordPress/Elementor (naml2027.org) kao jedan HTML widget. Stari web: naml2026.org.

## Konačni rezultat: Elementor HTML za svaku stranicu
Ono što ide u WordPress su datoteke u `wordpress/` (index, call-for-participation, agenda, venues, organizers, sponsors, previous-workshops). Svaka je samostalna: fontovi, cijeli CSS, sadržaj i JS, bez headera i footera, jer njih daje WordPress tema. Kad korisnik traži "Elementor verziju" neke stranice, pošalji mu tu datoteku. Prije objave slike trebaju doći iz WordPress Media Libraryja (`SITE_URL` u `build.py` i URL-ovi s naml2026.org).

## Kako se radi izmjena
1. Uređuj samo `src/pages/*.html`, `src/svg/*.svg`, `assets/css/naml.css`, `assets/js/naml.js` ili `build.py` (izbornik i footer su u `build.py`).
2. Pokreni `python3 build.py`, koji generira stranice u rootu i `wordpress/*.html`. Generirane datoteke ne uređuj ručno.
3. Provjeri izgled (screenshot desktop i mobitel ako možeš), pa commitaj i pushaj na `main`. GitHub Pages servira root grane `main`.

Placeholderi u stranicama: `{{base}}` (putanja do assets), `{{link:stranica}}` (interni link), `{{svg:ime}}` (ilustracija iz `src/svg`).

## Pravila dizajna
- Sav CSS je pod `.naml` (da radi u Elementor HTML widgetu bez sukoba s temom).
- Paleta NAML 2027: teal #16929E, tamni teal #02565E, koralj #FF544B, žuta #FFC54B, narančasta #FFA04B. Pozadine #013A40 (deep) i #E8F4F5 (mist).
- Fontovi: Bebas Neue (naslovi), Barlow (tekst), s Google Fontsa.
- Potpisni detalj: "pomaknuta sjena" kao kod broda u logu (žuta ili koraljna `box-shadow`/`text-shadow` 3–6px).
- Logo: `assets/img/naml27-logo-color.webp` (svijetla pozadina), `naml27-logo-white.webp` (tamna).
- Hero na naslovnici: bijeli logo, "2027", datumi, gumbi, odbrojavanje do 4. 12. 2026 i radar (`src/svg/sonar.svg`). Bez "11th Annual Workshop" u naslovu.
- Logotipi sponzora i organizacija su u zaobljenim bijelim pločicama (`.spon`), a osobe u karticama (`.person`).
- CSS i JS imaju `?v=hash` u linkovima (cache-busting) koji dodaje build.

## Stranice
Home, Call for Participation, Agenda (za NAML 2027; Underline embed je zakomentiran, čeka EVENT_ID), Venues (Hyatt Regency La Jolla dani 1–2, NIWC Pacific dani 3–4), Organizers, Sponsors (NAML 2026 sponzori kao primjer), Previous Workshops (2021–2026 + embed NAML 2026 programa: underline.io/events/508/schedule/embed).

## Kontakti na stranici
- Organizatori: naml@us.navy.mil
- Platforma, registracija, Underline: naml2027@underline.io
- Sponzorstvo: RaChelle Curato, racurato@deloitte.com
- Abstract forma: https://go.mil/naml2027sub · info: https://go.mil/naml

## Otvoreno
- Fotografije organizatora i logotipi sponzora učitavaju se s naml2026.org. Za WordPress ih treba prebaciti u Media Library.
- Odbor za 2027 još nije potvrđen (CfP potpisuju Erin Hausmann i Pedro Forero). Website chair je Rafael-Leopold Grabovica (bez linka, samo slika).
- Link NAML 2026 na Underlineu (events/508/reception) nije provjeren.
- Agenda 2027: kad event postoji na Underlineu, upiši EVENT_ID u `src/pages/agenda.html`.
