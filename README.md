# Sensie website

De broncode van de nieuwe Sensie-website. De site bestaat uit zeven statische pagina's in het Nederlands.

## Lokaal bouwen

Python 3 is voldoende; er zijn geen externe Python-pakketten nodig.

```sh
python build.py
python check.py
python -m http.server 8787 --directory dist
```

Open daarna `http://localhost:8787`.

`build.py` genereert de publiceerbare website in `dist/`. Bewerk de teksten in `build.py`, de vormgeving in `styles.css` en de beelden in `practice.webp` en `team.webp`.

De knop voor online afspraken verwijst momenteel naar het afsprakensysteem op [sensie.be](https://www.sensie.be/#Afspraak-maken). Pas die link aan als het domein of afsprakensysteem verhuist. De agenda en tarieven zijn overgenomen van de bestaande site en moeten actueel gehouden worden. Het praktijkbeeld is een sfeerbeeld; de teamfoto komt van de bestaande site.

Het privévoorbeeld staat op [sensie-vernieuwd.pieter-vdh.chatgpt.site](https://sensie-vernieuwd.pieter-vdh.chatgpt.site/).
