# NAML 2027 – pregled weba (24. 11. 2026)

Tri kruga: dizajn, tehnička provjera i 10 tipova posjetitelja. Sve navedeno je napravljeno, osim stavki pod "Otvoreno".

## 1. Dizajn i paleta
| Problem | Promjena |
|---|---|
| Koraljna (#FF544B) kao sitan tekst na bijelom (aktivni izbornik, linkovi u karticama) ima kontrast samo 3.2:1 | Uvedena `--coral-ink` #C2352D (5.5:1) za tekst. Aktivna stavka izbornika je tamna s koraljnom crtom. |
| Žute i narančaste oznake ("POSTER", "OTHER") na svijetloj podlozi su nečitljive | Brojke i oznake su tamni teal, boja je samo na bočnoj traci. |
| Dupli nazivi ("POSTER / POSTERS", "OTHER / OTHER CONTENT") | "Poster / Poster session" i "Your idea / Other formats". |
| Sličice kartica u tri različita stila (crtež, kalendar, CIC) | Sve tri su u istom tamnom CIC stilu (mreža, žuta i koraljna). |
| Agenda je imala ravnu ilustraciju kalendara umjesto radara kao ostale stranice | Mali radar kao na ostalim stranicama. |
| Dani 3–4 na Agendi u različitim bojama (koralj i žuta) | Dani 1–2 su teal (otvoreno), dani 3–4 koralj (ograničeno), dosljedno s Venues. |
| Plava pločica godine (#16929E) sa sitnim tekstom ima kontrast 2.7:1 | Tamniji teal #117680, a tekst ima kontrast iznad 5:1. |
| Panel "Ready to submit" na CfP-u je bio većinom prazan | Upute "How to submit" u 4 koraka. |
| Na mobitelu je radar stajao iznad loga i datuma | Na mobitelu je radar ispod teksta, pa su ključne informacije prve. |

## 2. Tehnička provjera
Provjereno automatski na svim stranicama i WP blokovima: nema neispravnih internih linkova i sidara, dupliciranih ID-ova, slika bez alt teksta, nezatvorenih tagova ni JS grešaka.

Popravljeno i dodano:
- **Mobilni izbornik:** zatvara se na Escape, klikom na link i klikom izvan izbornika, a fokus se vraća na gumb. Gumb piše Menu ili Close.
- **Pristupačnost:**
  - dodan "Skip to content" link i `main` element
  - odbrojavanje je skriveno od čitača ekrana, a čitač dobiva statički tekst roka
  - logo u naslovu nema dupli alt tekst
- **Mobitel:** gumb "Submit" je uvijek vidljiv u headeru.
- **Dijeljenje na društvenim mrežama:** Open Graph i Twitter meta oznake, slika `og-naml2027.png` (1200×630) i boja preglednika.
- **E-mail linkovi** imaju unaprijed upisan naslov (pitanje, sponzorstvo, registracija, pristup).
- **Čišćenje:** maknuti su neiskorišteni SVG-ovi i mrtvi JS kod.
- **Sidra:** provjereno je da `#faq` i ostala sidra nisu skrivena ispod ljepljivog headera.

## 3. Posjetitelji i njihovi problemi
| Posjetitelj | Problem | Rješenje |
|---|---|---|
| Istraživač u Navyju predaje sažetak | Pravila su raspršena, nema jasnog postupka | 4 koraka na CfP-u i FAQ |
| Inženjer iz industrije | Smije li tvrtka prezentirati? | FAQ: da, ali bez prodajnog pitcha, uz link na sponzorstvo |
| Profesor ili doktorand | Koji format i kad stiže odgovor | Presentation types, FAQ "When will I hear back?" |
| Strani ili nekleareni istraživač | Može li doći na dane 3–4? | Tablica "Who can attend what" na Venues, FAQ |
| Vojni časnik ili državni službenik | Kotizacija i podaci za putni nalog | FAQ o kotizaciji, točne adrese obiju lokacija, dodavanje u kalendar |
| Netko tko planira dolazak u NIWC | Pristup bazi traži vrijeme | Napomena o zahtjevu za posjet (opća pravila NIWC Pacifica traže najmanje 15 radnih dana) i kontakt |
| Sponzor ili marketing | Gdje se javiti | Gumb "Ask about sponsorship" u zaglavlju Sponsors, mail s naslovom |
| Korisnik na mobitelu | Teško do glavnih akcija | Uvijek vidljiv Submit, radar ispod sadržaja |
| Korisnik čitača ekrana ili tipkovnice | Nema preskakanja izbornika, odbrojavanje "brblja" | Skip link, aria-hidden na odbrojavanju, fokus |
| Netko tko čeka registraciju | Kad se otvara i koga pitati | FAQ s kontaktom naml2027@underline.io |
| Bilo tko | Rokovi se lako zaborave | "Add to calendar" (Google i .ics) za rok sažetaka i radionicu |

## Otvoreno (treba potvrdu organizatora)
- **Vremenska zona roka:** odbrojavanje računa do kraja 4. 12. 2026 po pacifičkom vremenu (pretpostavka, CfP ne navodi zonu).
- **NIWC Pacific:** navedena je adresa sjedišta (53560 Hull Street). Točna zgrada i postupak pristupa za radionicu nisu poznati.
- **Tablica "Who can attend what":** sastavljena iz teksta CfP-a. Neka je organizatori potvrde.
- **WordPress:** `.ics` datoteke, logotipi i OG slika trebaju biti u Media Libraryju. Dok se to ne napravi, treba uključiti GitHub Pages.
