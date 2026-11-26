# NAML 2027 demo site – upute za Claude

Korisnik (Rafael, Underline Science) piše na hrvatskom i šalje izmjene koje traži klijent (NAML / AFCEA San Diego / NIWC Pacific). Odgovaraj na hrvatskom (latinica), kratko. Svaku izmjenu napravi, pokreni build, provjeri i pushaj na `main`.

## Što je ovo
Višestranični demo web za NAML 2027 (Naval Applications of Machine Learning, 11th Annual Workshop, April 12–15, 2027, San Diego). Kasnije se svaka stranica prebacuje u WordPress/Elementor (naml2027.org) kao jedan HTML widget. Stari web: naml2026.org.

## Konačni rezultat: Elementor HTML za svaku stranicu
Ono što ide u WordPress su datoteke u `wordpress/` (index, registration, agenda, venues, organizers, sponsors, previous-workshops). Svaka je samostalna: fontovi, cijeli CSS, sadržaj i JS, bez headera i footera, jer njih daje WordPress tema. Kad korisnik traži "Elementor verziju" neke stranice, pošalji mu tu datoteku. Prije objave slike trebaju doći iz WordPress Media Libraryja (`SITE_URL` u `build.py` i URL-ovi s naml2026.org).

## WordPress
- Upute za postavljanje su u `WORDPRESS-SETUP.md`: nova stranica, prijenos domene, slugovi, header i footer, site icon.
- Svaki WP blok sadrži naš header, sadržaj i footer, i sam se širi na 100vw (WP_FIX u build.py), pa radi u bilo kojoj temi. Na WordPressu se koristi template "Blank" (Twenty Twenty-Four). Mobilni izbornik je `<details>`, bez JS-a.
- Loading ekran (logo u radaru, `src/parts/boot.html`, oštar SVG brojčanik kao glavni radar) je samo na naslovnici, čisti CSS, oko 1 s.
- Favicon i ikona stranice: stisnuti NAML logo u boji (`favicon.ico`, `favicon.png`, `apple-touch-icon.png`, za WordPress `site-icon-512.png`). Ne radar.
- Blokovi rade na svakom plaćenom planu (i Premium) kad su na stranici uključene hosting značajke (WordPress.com docs, studeni 2026). Nije potrebna posebna Premium verzija.

## Kako se radi izmjena
1. Uređuj samo `src/pages/*.html`, `src/svg/*.svg`, `assets/css/naml.css`, `assets/js/naml.js` ili `build.py` (izbornik i footer su u `build.py`).
2. Pokreni `python3 build.py`, koji generira stranice u rootu i `wordpress/*.html`. Generirane datoteke ne uređuj ručno.
3. Provjeri izgled (screenshot desktop i mobitel ako možeš), pa commitaj i pushaj na `main`. GitHub Pages servira root grane `main`.

Placeholderi u stranicama: `{{base}}` (putanja do assets), `{{link:stranica}}` (interni link), `{{svg:ime}}` (ilustracija iz `src/svg`).

## Pravila dizajna
- Sav CSS je pod `.naml` (da radi u Elementor HTML widgetu bez sukoba s temom).
- Paleta NAML 2027: teal #16929E, tamni teal #02565E, koralj #FF544B, žuta #FFC54B, narančasta #FFA04B. Pozadine #013A40 (deep) i #E8F4F5 (mist).
- Fontovi: Bebas Neue (naslovi), Barlow (tekst), IBM Plex Mono (radar, oznake sektora), s Google Fontsa.
- Potpisni detalj: "pomaknuta sjena" kao kod broda u logu (žuta ili koraljna `box-shadow`/`text-shadow` 3–6px).
- Logo: vektoriziran iz originala, `assets/img/naml27-logo-color.svg|.webp` (svijetla pozadina) i `naml27-logo-white.svg|.webp` (tamna); WebP je 2421 px širok.
- Hero na naslovnici: bijeli logo, ispod naslovni blok (bijela linija, veliko žuto "2027", "APRIL 12–15 / SAN DIEGO, CA"), formacija mlažnjaka u pozadini (`src/svg/jets.svg`), gumbi, odbrojavanje do početka radionice (12. 4. 2027, data-end na #naml-count) i radar (`src/parts/radar.html`, radar s oznakama "La Jolla · Days 1–2" i "NIWC Pacific · Days 3–4" i legendom ispod; na unutarnjim stranicama `radar-mini.html`). Bez "11th Annual Workshop" u naslovu.
- Logotipi sponzora i organizacija su u zaobljenim bijelim pločicama (`.spon`), a osobe u karticama (`.person`).
- Radar (glavni na naslovnici, mali na ostalim stranicama i loading ekran) je obavezni dio identiteta. Ne micati ga i ne zamjenjivati.
- "CIC" mrežasta pozadina (`.gridbg`) samo na tamnim dijelovima: heroji, page heroji i sekcija lokacija. Bijele sekcije ostaju bijele.
- Venues koristi tamne "sektor" kartice (`.sector`) umjesto slika lokacija; ne stavljati fotografije lokacija dok se ne potvrdi smijemo li.
- Placeholder `{{part:ime}}` ubacuje HTML iz `src/parts/` (radar, radar-mini, cal = dodavanje u kalendar, types = vrste prezentacija).
- Kontrast: koralj #FF544B nikad kao sitan tekst na svijetlom, nego `--coral-ink` #C2352D. Žuta i narančasta samo kao pozadine ili trake, ne kao tekst na svijetlom.
- Dani 1–2 su teal (open), dani 3–4 koralj (restricted), dosljedno svugdje.
- FAQ je na naslovnici (`#faq`). Odgovori smiju biti samo iz službenog CfP-a.
- Mailto linkovi imaju unaprijed upisan naslov (`?subject=`).
- Bez "AI znakova" (vidi falia.co članak): nema srednjih točkica "·" kao razdjelnika, nema dugih crtica (– —), nema strelica na linkovima i gumbima. Rasponi datuma pišu se s običnom crticom (April 12-15), kao na naml2026.org. Nema kutija s brojkama ni tri jednake kartice; koristi rečenicu, tablicu (`part:dates`) ili listu (`.next`, `part:types`).
- Tamni CIC dijelovi i monospace oznake ostaju (namjerna odluka), ali bez jakog sjaja. Hover samo na gumbima, linkovima i karticama koje su linkovi.
- WP blokovi se generiraju bez komentara u CSS-u i JS-u.
- Boje naslova, teksta i gumba su eksplicitno zadane ("Guard against theme typography" u CSS-u), jer WordPress teme boje h1-h6, p i a. Kod novih elemenata na tamnoj pozadini uvijek zadaj boju.
- Nakon izmjena pokreni QA: svi linkovi i sidra, ID-ovi, alt, JS greške (vidi AUDIT.md).
- CSS i JS imaju `?v=hash` u linkovima (cache-busting) koji dodaje build.

## Stranice
Home, Registration (mjesto za Paperform: PAPERFORM_ID ili PAPERFORM_URL u build.py), Agenda (za NAML 2027; Underline embed je zakomentiran, čeka EVENT_ID), Venues (Hyatt Regency La Jolla dani 1–2, NIWC Pacific dani 3–4), Organizers (General chairs: Erin Hausmann, Pedro Forero; AFCEA chair: RaChelle Curato; Registration chair; Website chair), Sponsors (bez popisa, samo kontakt RaChelle Curato), Previous Workshops (2021–2026 + embed NAML 2026 programa: underline.io/events/508/schedule/embed).

## Kontakti na stranici
- Organizatori: naml@us.navy.mil
- Registration support: naml2027@underline.io
- Sponzorstvo: RaChelle Curato, racurato@deloitte.com
- Info: https://go.mil/naml. Faza predaje sažetaka je gotova: na stranici nema sadržaja o abstractima ni Call for Participation.

## Otvoreno
- Vidi i `AUDIT.md` (zona roka, NIWC zgrada i pristup, potvrda tablice pristupa, .ics i slike u WP Media Library).
- Fotografije organizatora i logotipi sponzora učitavaju se s naml2026.org. Za WordPress ih treba prebaciti u Media Library.
- Odbor za 2027 još nije potvrđen (CfP potpisuju Erin Hausmann i Pedro Forero). Website chair je Rafael-Leopold Grabovica (bez linka, samo slika).
- Link NAML 2026 na Underlineu (events/508/reception) nije provjeren.
- Agenda 2027: kad event postoji na Underlineu, upiši EVENT_ID u `src/pages/agenda.html`.
