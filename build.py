from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
ASSETS = DIST / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

nav = [
    ("/", "Home"),
    ("/individuele-begeleiding/", "Individueel"),
    ("/relaties-seksualiteit/", "Relaties & seksualiteit"),
    ("/hypnotherapie/", "Hypnotherapie"),
    ("/groepen-agenda/", "Groepen & agenda"),
    ("/over-sensie/", "Over Sensie"),
    ("/praktisch-contact/", "Praktisch & contact"),
]

def link(path, label, current):
    active = ' aria-current="page"' if path == current else ""
    return f'<a href="{path}"{active}>{label}</a>'

def cta(label="Neem contact op"):
    return f'<a class="button button-primary" href="/praktisch-contact/">{label}<span aria-hidden="true">↗</span></a>'

def closing(title="We lopen graag een stukje met je mee.", text="Je hoeft je vraag nog niet precies te kunnen verwoorden. Samen kijken we wat er speelt en wat je nodig hebt."):
    return f'''<section class="closing-band"><div class="container closing-inner"><div><p class="eyebrow">Welkom bij Sensie</p><h2>{title}</h2><p>{text}</p></div>{cta()}</div></section>'''

def layout(path, title, description, body):
    nav_desktop = "".join(link(p, label, path) for p, label in nav)
    nav_mobile = nav_desktop
    page_title = f"{title} | Sensie" if title != "Sensie" else "Sensie | Warme zorg, verbinding en zingeving"
    return f'''<!doctype html>
<html lang="nl-BE">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f7f3ec">
  <meta name="description" content="{escape(description, quote=True)}">
  <title>{escape(page_title)}</title>
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Spring naar inhoud</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="/" aria-label="Sensie, naar de homepage"><span class="brand-mark" aria-hidden="true">S</span><span>Sensie<small>zorg · verbinding · zingeving</small></span></a>
      <nav class="desktop-nav" aria-label="Hoofdnavigatie">{nav_desktop}</nav>
      <details class="mobile-menu"><summary>Menu <span aria-hidden="true">☰</span></summary><nav aria-label="Mobiele navigatie">{nav_mobile}</nav></details>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer"><div class="container footer-grid"><div><a class="footer-brand" href="/">Sensie</a><p>Een plek voor warme zorg, verbinding en zingeving.</p></div><div><h2>Ontdek</h2><a href="/individuele-begeleiding/">Individuele begeleiding</a><a href="/groepen-agenda/">Groepen & agenda</a><a href="/over-sensie/">Over Sensie</a></div><div><h2>Contact</h2><p>Wijnendalestraat 31<br>8800 Beveren-Roeselare</p><a href="tel:+32473814500">Véronique: +32 473 81 45 00</a><a href="tel:+32486213725">Pieter: +32 486 21 37 25</a></div></div><div class="container footer-bottom"><span>© Sensie 2026</span><span>Ondernemingsnummer 0864.335.227</span></div></footer>
</body></html>'''

pages = {
"/": (
    "Sensie",
    "Sensie is een groepspraktijk in Beveren-Roeselare voor therapie, coaching, ontmoeting en persoonlijke ontwikkeling.",
    f'''<section class="hero"><div class="container hero-grid"><div class="hero-copy"><p class="eyebrow">Groepspraktijk in Beveren-Roeselare</p><h1>Een plek voor warme zorg, verbinding en <em>zingeving.</em></h1><p class="lead">Sensie is een groepspraktijk waar therapie, coaching, ontmoeting en persoonlijke ontwikkeling samenkomen. Je bent welkom wanneer je vastloopt, met vragen zit of voelt dat je iets wilt veranderen of beter begrijpen.</p><div class="button-row"><a class="button button-primary" href="#aanbod">Ontdek wat bij je past <span aria-hidden="true">↗</span></a><a class="text-link" href="/over-sensie/">Leer Sensie kennen <span aria-hidden="true">→</span></a></div></div><div class="hero-image"><img src="/assets/praktijk.webp" alt="Sfeerbeeld van een warme, lichte zitruimte" onerror="this.closest('.hero-image').classList.add('image-unavailable');this.remove()"><span class="image-caption">Een plek om even te mogen zijn.<small>Sfeerbeeld</small></span></div></div></section>
    <section class="intro-section"><div class="container intro-grid"><div><p class="eyebrow">Wat ons verbindt</p><h2>Wat geeft jouw leven betekenis?</h2></div><div class="prose"><p>Waar krijg je energie van? Wat geeft je richting, verbinding en voldoening? Soms zijn dat grote levensvragen. Soms raken we het contact ermee kwijt door wat er op ons pad komt.</p><p>Bij Sensie is zingeving de rode draad. We kijken naar jou als mens, met je hele verhaal, en maken ruimte voor kwetsbaarheid én kracht.</p></div></div></section>
    <section class="section offerings" id="aanbod"><div class="container"><div class="section-heading"><div><p class="eyebrow">Ons aanbod</p><h2>Ondersteuning die bij je past</h2></div><p>Een gesprek, een andere blik, of de kracht van samenkomen. Er zijn verschillende manieren om weer ruimte te voelen.</p></div><div class="card-grid"><a class="offer-card" href="/individuele-begeleiding/"><span class="card-number">01</span><h3>Individuele begeleiding</h3><p>Voor vastlopen, rouw en verlies, identiteitsvragen, hoogsensitiviteit, hoogbegaafdheid en persoonlijke groei.</p><span class="card-link">Meer over begeleiding <span aria-hidden="true">↗</span></span></a><a class="offer-card" href="/relaties-seksualiteit/"><span class="card-number">02</span><h3>Relaties & seksualiteit</h3><p>Een veilige plek voor vragen over verbinding, relatiepatronen, intimiteit en seksualiteit. Alleen of samen.</p><span class="card-link">Ontdek de mogelijkheden <span aria-hidden="true">↗</span></span></a><a class="offer-card" href="/groepen-agenda/"><span class="card-number">03</span><h3>Groepen & ontmoeting</h3><p>Familieopstellingen, deelcirkels en andere momenten om samen te delen, ontdekken en ervaren.</p><span class="card-link">Bekijk het groepsaanbod <span aria-hidden="true">↗</span></span></a></div><p class="aside-link">Ook benieuwd naar <a href="/hypnotherapie/">hypnotherapie</a>?</p></div></section>
    <section class="quote-section"><div class="container quote-inner"><span class="quote-mark" aria-hidden="true">“</span><blockquote>Zorg hoeft niet altijd te betekenen dat je tegenover iemand in een stoel zit en vertelt wat er moeilijk gaat. Soms helpt een gesprek. Soms het samenbrengen van mensen. Soms gewoon een plek waar je even mag zijn.</blockquote></div></section>
    <section class="section"><div class="container split-content"><div><p class="eyebrow">Voor wie</p><h2>Je hoeft geen duidelijke hulpvraag te hebben.</h2></div><div class="prose"><p>Misschien loop je vast in jezelf, op je werk of in relaties. Misschien draag je een verlies mee, zoek je naar wie je bent of verlang je naar meer diepgang.</p><p>Ook als je nog niet precies weet wat er knelt, ben je welkom. We staan samen stil bij wat er is en ontdekken wat voor jou belangrijk is.</p><a class="text-link" href="/individuele-begeleiding/">Lees hoe we je begeleiden <span aria-hidden="true">→</span></a></div></div></section>{closing()}'''
),
"/individuele-begeleiding/": (
    "Individuele begeleiding",
    "Individuele therapie en coaching bij Sensie rond rouw, vastlopen, identiteit, zingeving, hoogsensitiviteit en hoogbegaafdheid.",
    f'''<section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Aanbod · voor jou</p><h1>Individuele begeleiding</h1><p class="lead">Soms loopt het leven anders dan je had gehoopt. In een persoonlijk gesprek zoeken we samen naar ruimte, inzicht en een weg die bij jou past.</p></div></section><section class="section"><div class="container split-content"><div><p class="eyebrow">Wanneer je welkom bent</p><h2>Met een vraag. Of met een gevoel dat iets knelt.</h2></div><div class="prose"><p>Misschien loop je vast in jezelf, je werk of je familie. Misschien draag je een verlies mee, zoek je naar wie je bent of wil je meer uit jezelf en het leven halen. Je hoeft vooraf niet precies te weten wat je nodig hebt.</p><p>We bieden individuele begeleiding rond onder meer rouw en verlies, zelfontplooiing, identiteitsvragen en zingeving. Ook bij hoogsensitiviteit en hoogbegaafdheid kan je ondersteuning vinden.</p></div></div></section><section class="section tinted"><div class="container"><p class="eyebrow">Thema’s</p><h2>Waar we samen bij kunnen stilstaan</h2><div class="topic-grid"><div>Rouw, verlies en gemis</div><div>Vastlopen en verandering</div><div>Identiteit en zingeving</div><div>Hoogsensitiviteit en prikkels</div><div>Hoogbegaafdheid en talent</div><div>Persoonlijke groei en grenzen</div></div></div></section><section class="section"><div class="container split-content"><div><p class="eyebrow">Het eerste gesprek</p><h2>We beginnen met luisteren.</h2></div><div class="prose"><p>In een eerste gesprek maken we kennis en luisteren we naar wat er nu voor jou speelt. Samen onderzoeken we wat helpend kan zijn en hoe een eventueel vervolgtraject eruitziet. We stemmen de begeleiding af op jouw verhaal en jouw tempo.</p><p>De praktijk verwelkomt jongeren vanaf 14 jaar en volwassenen.</p><a class="text-link" href="/praktisch-contact/">Bekijk praktische informatie <span aria-hidden="true">→</span></a></div></div></section>{closing()}'''
),
"/relaties-seksualiteit/": (
    "Relaties & seksualiteit",
    "Relatietherapie en sekscounseling bij Sensie in Beveren-Roeselare, voor koppels en individuen.",
    f'''<section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Aanbod · verbinding</p><h1>Relaties & seksualiteit</h1><p class="lead">Relaties en intimiteit raken aan wie we zijn. Wanneer het moeilijk loopt of vragen oproept, kan het helpen om samen met iemand van buitenaf stil te staan.</p></div></section><section class="section"><div class="container split-content"><div><p class="eyebrow">Relatietherapie</p><h2>Opnieuw ruimte maken voor elkaar.</h2></div><div class="prose"><p>Misschien zijn er terugkerende conflicten, is vertrouwen beschadigd of voelt de verbinding anders dan vroeger. Misschien zoeken jullie jullie weg als nieuw samengesteld gezin. In relatietherapie kijken we zonder oordeel naar wat er speelt en wat ieder nodig heeft.</p><p>Je kan als koppel komen, maar ook alleen met vragen over je relatie. Het doel is om patronen te begrijpen en weer met meer helderheid met elkaar in gesprek te kunnen gaan.</p></div></div></section><section class="section tinted"><div class="container split-content"><div><p class="eyebrow">Sekscounseling</p><h2>Ook over seksualiteit mag je spreken.</h2></div><div class="prose"><p>Vragen over verlangen, intimiteit, seksuele verschillen of je identiteit kunnen gevoelig zijn. We bieden een veilige plek om ze in je eigen woorden te verkennen, zonder oordeel of haast.</p><p>Je bent welkom alleen of samen met je partner. We zoeken naar wat voor jou of jullie helpend is.</p></div></div></section>{closing("Je hoeft het niet alleen uit te zoeken.", "Een eerste gesprek kan helpen om woorden te geven aan wat moeilijk loopt en te ontdekken welke ondersteuning past.")}'''
),
"/hypnotherapie/": (
    "Hypnotherapie",
    "Lees hoe hypnotherapie bij Sensie verloopt en wat je tijdens een sessie kan verwachten.",
    f'''<section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Aanbod · verdieping</p><h1>Hypnotherapie</h1><p class="lead">Soms helpt een andere ingang dan alleen praten. Hypnotherapie biedt ruimte om met aandacht en verbeelding stil te staan bij gedachten, gevoelens en patronen.</p></div></section><section class="section"><div class="container split-content"><div><p class="eyebrow">Hoe het werkt</p><h2>Diepe aandacht, met regie bij jou.</h2></div><div class="prose"><p>Hypnose is een toestand van gerichte aandacht en ontspanning, vergelijkbaar met helemaal opgaan in een boek of muziek. Tijdens een sessie werken we onder meer met visualisaties en gerichte suggesties. Je blijft bewust en in controle; hypnotherapie is een samenwerking.</p><p>Bij Sensie kan deze werkwijze worden ingezet bij onder meer stress, rouw, gedragsverandering en persoonlijke groei. In een kennismaking bespreken we of ze past bij jouw vraag.</p></div></div></section><section class="section tinted"><div class="container"><p class="eyebrow">Veelgestelde vragen</p><h2>Wat kan je verwachten?</h2><div class="faq-list"><details><summary>Verlies ik de controle tijdens hypnose?</summary><p>Nee. Je blijft bewust van wat er gebeurt en doet niets tegen je wil.</p></details><details><summary>Is één sessie voldoende?</summary><p>Een sessie kan inzicht geven. Verandering vraagt vaak meer tijd. Samen bespreken we wat voor jouw vraag passend is.</p></details><details><summary>Moet ik vooraf weten of hypnotherapie bij me past?</summary><p>Nee. Tijdens een eerste contact bekijken we samen je vraag en de mogelijkheden.</p></details></div></div></section>{closing("Benieuwd of hypnotherapie bij je past?", "Neem gerust contact op. We luisteren naar je vraag en denken met je mee.")}'''
),
"/groepen-agenda/": (
    "Groepen & agenda",
    "Ontdek groepsactiviteiten bij Sensie: familieopstellingen, deelcirkels en ruimte voor ontmoeting.",
    f'''<section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Samen ontdekken</p><h1>Groepen & ontmoeting</h1><p class="lead">Soms ontstaat beweging juist door samen te komen: delen, luisteren, herkennen en ervaren. Bij Sensie geloven we in de kracht van ontmoeting.</p></div></section><section class="section"><div class="container"><div class="section-heading"><div><p class="eyebrow">Groepsaanbod</p><h2>Er is plaats voor jouw verhaal.</h2></div><p>Je kan deelnemen op de manier die voor jou goed voelt. We creëren een warme omgeving met ruimte voor stilte én verbinding.</p></div><div class="card-grid"><article class="offer-card"><span class="card-number">01</span><h3>Familieopstellingen</h3><p>Een ervaringsgerichte manier om zicht te krijgen op patronen en dynamieken in je familie of andere relaties. Individueel of in een groep.</p></article><article class="offer-card"><span class="card-number">02</span><h3>Deelcirkels</h3><p>Een plek om te delen en te luisteren, zonder dat je iets moet oplossen. Herkenning en oprechte aandacht staan centraal.</p></article><article class="offer-card"><span class="card-number">03</span><h3>Samen ervaren</h3><p>Momenten om samen iets te doen, te onderzoeken of gewoon te genieten van het samenzijn.</p></article></div></div></section><section class="section tinted"><div class="container split-content"><div><p class="eyebrow">Agenda</p><h2>Komende momenten</h2></div><div class="prose"><p>Het programma wisselt. Neem contact op voor de actuele data van familieopstellingen, deelcirkels en andere bijeenkomsten, of om je interesse te laten weten.</p><a class="text-link" href="/praktisch-contact/">Vraag naar de agenda <span aria-hidden="true">→</span></a></div></div></section>{closing("Je bent welkom om aan te sluiten.", "Ook als je eerst wil weten hoe een groepsmoment verloopt, beantwoorden we graag je vragen.")}'''
),
"/over-sensie/": (
    "Over Sensie",
    "Maak kennis met Sensie, onze visie op warme zorg en de mensen achter de groepspraktijk.",
    f'''<section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Onze plek en onze visie</p><h1>Over Sensie</h1><p class="lead">Een warme plek waar ruimte is voor kwetsbaarheid én kracht, voor zoeken én groeien, voor stilte én verbinding.</p></div></section><section class="section"><div class="container split-content"><div><p class="eyebrow">Waarom Sensie bestaat</p><h2>Gezien worden als mens, met je hele verhaal.</h2></div><div class="prose"><p>Bij Sensie komen therapie, coaching, ontmoeting en persoonlijke ontwikkeling samen. Zingeving loopt als een rode draad door wat we doen: wat geeft jouw leven richting, energie en voldoening?</p><p>We geloven dat zorg verschillende vormen kan aannemen. Soms helpt een gesprek. Soms een andere blik. Soms het samenbrengen van mensen. We lopen graag een stukje met je mee om stil te staan bij wat er is en opnieuw ruimte te maken voor wat betekenisvol voelt.</p></div></div></section><section class="section tinted"><div class="container"><p class="eyebrow">De mensen achter Sensie</p><h2>Maak kennis met ons</h2><div class="people-grid"><article><span class="portrait-letter" aria-hidden="true">V</span><h3>Véronique Vanhixe</h3><p>Véronique begeleidt mensen onder meer rond rouw en verlies, relaties, seksualiteit, zingeving en familieopstellingen. Ze werkt warm, betrokken en integratief.</p></article><article><span class="portrait-letter" aria-hidden="true">P</span><h3>Pieter Vandenhende</h3><p>Pieter brengt mensen samen in deelcirkels en begeleidt vanuit aandacht voor verbinding, authenticiteit en het unieke verhaal van ieder mens.</p></article></div></div></section><section class="section"><div class="container split-content"><div><p class="eyebrow">Onze werkwijze</p><h2>Professioneel en persoonlijk.</h2></div><div class="prose"><p>We stemmen onze begeleiding af op de persoon voor ons. Door regelmatig deel te nemen aan intervisie en supervisie blijven we leren en zorg dragen voor de kwaliteit van ons werk. Daarbij staat jouw privacy voorop.</p><a class="text-link" href="/praktisch-contact/">Zo bereik je ons <span aria-hidden="true">→</span></a></div></div></section>{closing()}'''
),
"/praktisch-contact/": (
    "Praktisch & contact",
    "Praktische informatie over sessies bij Sensie in Beveren-Roeselare: locatie, tarieven, afspraken en contact.",
    f'''<section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Welkom bij Sensie</p><h1>Praktisch & contact</h1><p class="lead">Wil je een afspraak maken of eerst iets vragen? Je kan rechtstreeks contact opnemen. We helpen je graag de juiste eerste stap te vinden.</p></div></section><section class="section"><div class="container contact-grid"><div class="contact-panel"><p class="eyebrow">Neem contact op</p><h2>We luisteren graag.</h2><p>Vertel gerust kort wat je zoekt. Je hoeft je vraag nog niet helemaal duidelijk te hebben.</p><a class="contact-link" href="tel:+32473814500">Véronique <strong>+32 473 81 45 00</strong></a><a class="contact-link" href="tel:+32486213725">Pieter <strong>+32 486 21 37 25</strong></a></div><div class="contact-panel pale"><p class="eyebrow">De praktijk</p><h2>Je vindt ons hier.</h2><address>Wijnendalestraat 31<br>8800 Beveren-Roeselare</address><a class="text-link" href="https://www.google.com/maps/search/?api=1&query=Wijnendalestraat+31%2C+8800+Beveren-Roeselare" target="_blank" rel="noopener noreferrer">Bekijk de route <span aria-hidden="true">↗</span></a><p class="small-note">We werken uitsluitend op afspraak.</p></div></div></section><section class="section tinted"><div class="container"><p class="eyebrow">Veelgestelde praktische vragen</p><h2>Goed om te weten</h2><div class="faq-list"><details><summary>Wat kost een sessie?</summary><p>Volgens de huidige informatie kost een individuele sessie van 55 minuten € 70 en een koppelgesprek van anderhalf uur € 110. Tarieven voor andere vormen van begeleiding kunnen verschillen. Vraag bij het maken van je afspraak naar het actuele tarief.</p></details><details><summary>Hoe lang duurt een sessie?</summary><p>Een individueel gesprek duurt doorgaans 55 minuten. Voor een koppelgesprek is anderhalf uur voorzien. De duur van andere sessies bespreken we vooraf.</p></details><details><summary>Hoe kan ik betalen?</summary><p>Volgens de huidige praktische informatie kan je cash of via Payconiq betalen.</p></details><details><summary>Wat als ik mijn afspraak moet verplaatsen?</summary><p>Laat het zo vroeg mogelijk weten. Op de huidige site staat dat bij annulering minder dan 48 uur vooraf een verzuimvergoeding wordt aangerekend. Bespreek de actuele voorwaarden wanneer je een afspraak maakt.</p></details></div></div></section>{closing("Zet de eerste stap op jouw manier.", "Bel ons met je vraag of om een afspraak te maken. We denken graag met je mee.")}'''
),
}

title, description, body = pages["/groepen-agenda/"]
body = body.replace(
    '<p>Het programma wisselt. Neem contact op voor de actuele data van familieopstellingen, deelcirkels en andere bijeenkomsten, of om je interesse te laten weten.</p><a class="text-link" href="/praktisch-contact/">Vraag naar de agenda <span aria-hidden="true">→</span></a>',
    '''<p>Dit zijn de eerstvolgende momenten volgens de huidige agenda. Mail ons voor meer informatie of om je aan te melden.</p>
    <div class="event-list">
      <div><strong>2 oktober 2026</strong><span>Open deelcirkel rond het vuur</span></div>
      <div><strong>12 en 15 oktober 2026</strong><span>Filosofisch atelier in Beveren en Roeselare</span></div>
      <div><strong>13 november 2026</strong><span>Open deelcirkel rond het vuur</span></div>
      <div><strong>15 november 2026</strong><span>Familieopstellingen bij Sensie</span></div>
    </div><a class="text-link" href="mailto:info@sensie.be?subject=Vraag%20over%20groepsactiviteit">Vraag informatie of meld je aan <span aria-hidden="true">→</span></a>'''
)
pages["/groepen-agenda/"] = (title, description, body)

title, description, body = pages["/praktisch-contact/"]
body = body.replace(
    '<a class="contact-link" href="tel:+32473814500">',
    '<a class="contact-link" href="mailto:info@sensie.be">E-mail <strong>info@sensie.be</strong></a><a class="contact-link" href="tel:+32473814500">'
)
body = body.replace(
    '<a class="contact-link" href="mailto:info@sensie.be">',
    '<a class="booking-link" href="https://www.sensie.be/#Afspraak-maken" target="_blank" rel="noopener noreferrer">Maak online een afspraak <span aria-hidden="true">↗</span></a><a class="contact-link" href="mailto:info@sensie.be">'
)
body = body.replace(
    'Volgens de huidige informatie kost een individuele sessie van 55 minuten € 70 en een koppelgesprek van anderhalf uur € 110. Tarieven voor andere vormen van begeleiding kunnen verschillen. Vraag bij het maken van je afspraak naar het actuele tarief.',
    'Een individuele sessie van 55 minuten kost € 70. Een koppelgesprek van anderhalf uur kost € 110. Vraag bij het maken van je afspraak naar het tarief voor andere vormen van begeleiding.'
)
body = body.replace('Volgens de huidige praktische informatie kan je cash of via Payconiq betalen.', 'Je kan cash of via Payconiq betalen.')
body = body.replace(
    'Laat het zo vroeg mogelijk weten. Op de huidige site staat dat bij annulering minder dan 48 uur vooraf een verzuimvergoeding wordt aangerekend. Bespreek de actuele voorwaarden wanneer je een afspraak maakt.',
    'Laat het minstens 48 uur vooraf weten als je je afspraak wil annuleren of verplaatsen. Bij een latere annulering wordt een verzuimvergoeding van € 65 aangerekend.'
)
body = body.replace('href="/praktisch-contact/">Neem contact op', 'href="mailto:info@sensie.be">Stuur een e-mail')
pages["/praktisch-contact/"] = (title, description, body)

title, description, body = pages["/over-sensie/"]
body = body.replace(
    '<div class="people-grid">',
    '<figure class="team-figure"><img src="/assets/team.webp" alt="Pieter en Véronique, de mensen achter Sensie"><figcaption>Pieter en Véronique</figcaption></figure><div class="people-grid">'
)
pages["/over-sensie/"] = (title, description, body)

for route, (title, description, body) in pages.items():
    folder = DIST if route == "/" else DIST / route.strip("/")
    folder.mkdir(parents=True, exist_ok=True)
    html = layout(route, title, description, body)
    html = html.replace('<a href="tel:+32473814500">Véronique:', '<a href="mailto:info@sensie.be">info@sensie.be</a><a href="tel:+32473814500">Véronique:')
    (folder / "index.html").write_text(html, encoding="utf-8")

shutil.copy2(ROOT / "styles.css", ASSETS / "styles.css")
shutil.copy2(ROOT / "favicon.svg", ASSETS / "favicon.svg")
shutil.copy2(ROOT / "practice.webp", ASSETS / "praktijk.webp")
shutil.copy2(ROOT / "team.webp", ASSETS / "team.webp")
print(f"Built {len(pages)} pages in {DIST}")
