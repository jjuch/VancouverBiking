# VancouverBiking — Adaptive Vancouver Bike Route Planner

A free, open‑data‑powered web app that computes bike routes in **Vancouver** tailored to your day: seek **shade** when it’s hot or raining, prefer **protected bikeways**, minimize **air‑pollution exposure**, choose **quieter streets**, or dial in **workout hills**—all on top of a robust routing engine and real‑time environmental inputs. The app uses **OpenStreetMap** for the routable network (ODbL) and enriches it with **City of Vancouver** datasets (OGL–Vancouver), **Environment & Climate Change Canada** hourly weather, and **Metro Vancouver** / **BC AQHI** air‑quality feeds. [\[github.com\]](https://github.com/Yuki-20000/vancouver-311-dashboard), [\[city-of-va...arcgis.com\]](https://city-of-vancouver-wa-geo-hub-cityofvancouver.hub.arcgis.com/datasets/city-of-vancouver-street-segments/about), [\[geogratis.gc.ca\]](https://geogratis.gc.ca/site/eng/elevation), [\[open.canada.ca\]](https://open.canada.ca/data/en/dataset/7b4fef7e-7cae-4379-97b8-62b03e9ac83d)

***

## ✨ Key Features

*   **Multi‑criteria routing**: shortest vs. *Shady & Cool* vs. *Clean & Calm* vs. *Hurry* with left‑turn penalties at signalized intersections. (Uses OSM base graph + City **Bikeways**, **Traffic Signals**, **Street Intersections**.) [\[wiki.opens...eetmap.org\]](https://wiki.openstreetmap.org/wiki/Attribution_guidelines/2021-06-04_draft), [\[env.gov.bc.ca\]](https://www.env.gov.bc.ca/epd/bcairquality/data/aqhi-table.html), [\[van311.ca\]](https://van311.ca/)
*   **Canopy‑aware paths**: favors tree‑lined streets (City **Public Trees**), great for heat or drizzle. [\[Vancouver City Hall\]](http://www.vancouver.ca/)
*   **Elevation‑aware routing**: computes gain/grade from the **LiDAR‑derived Digital Elevation Model (1 m)**. [\[github.com\]](https://github.com/carsonyl/translink-derived-datasets)
*   **Weather & air‑quality adaptive**: toggles weights based on **ECCC hourly weather** and **Metro Vancouver/AQHI** air‑quality conditions. [\[city-of-va...arcgis.com\]](https://city-of-vancouver-wa-geo-hub-cityofvancouver.hub.arcgis.com/datasets/city-of-vancouver-street-segments/about), [\[geogratis.gc.ca\]](https://geogratis.gc.ca/site/eng/elevation), [\[open.canada.ca\]](https://open.canada.ca/data/en/dataset/7b4fef7e-7cae-4379-97b8-62b03e9ac83d)
*   **Simple UI + NL helper**: checkbox/sliders *or* a natural‑language box (“I want a shady, calm ride”).
*   **Zero/near‑zero cost**: open data, MapLibre/Leaflet, and free‑tier hosting patterns (GH Pages + Fly.io/Render).

***

## 🗺️ Data Sources (Open & Free)

*   **OpenStreetMap** (routing base graph), licensed **ODbL** — attribution required.
*   **City of Vancouver Open Data** (OGL–Vancouver):
    *   **Bikeways** (protected/local bikeways). [\[wiki.opens...eetmap.org\]](https://wiki.openstreetmap.org/wiki/Attribution_guidelines/2021-06-04_draft)
    *   **Public Trees** (points with species). [\[Vancouver City Hall\]](http://www.vancouver.ca/)
    *   **Traffic Signals** (signal locations). [\[env.gov.bc.ca\]](https://www.env.gov.bc.ca/epd/bcairquality/data/aqhi-table.html)
    *   **Street Intersections** (topology). [\[van311.ca\]](https://van311.ca/)
    *   **Public Streets** (centerlines). [\[vancouver....erstats.ca\]](https://vancouver.weatherstats.ca/download.html)
    *   **Digital Elevation Model (LiDAR 2013, \~1 m)**. [\[github.com\]](https://github.com/carsonyl/translink-derived-datasets)
*   **Real‑time / recent conditions**:
    *   **Weather** — ECCC **OGC API** hourly observations. [\[city-of-va...arcgis.com\]](https://city-of-vancouver-wa-geo-hub-cityofvancouver.hub.arcgis.com/datasets/city-of-vancouver-street-segments/about)
    *   **Air Quality** — **Metro Vancouver** current conditions & warnings; **BC AQHI** for health‑risk scaling. [\[geogratis.gc.ca\]](https://geogratis.gc.ca/site/eng/elevation), [\[open.canada.ca\]](https://open.canada.ca/data/en/dataset/7b4fef7e-7cae-4379-97b8-62b03e9ac83d)

> See **Attribution & Licenses** below for footer and README text you must retain.

***


## 🏷️ Attribution & Licenses (Keep in README and UI Footer)

*   **© OpenStreetMap contributors.** Data available under the **Open Database License (ODbL)** — see the OSM **copyright & attribution** page and follow the **Attribution Guidelines**.
*   **City of Vancouver Open Data** — published under the **Open Government Licence – Vancouver** (attribution required). [\[github.com\]](https://github.com/Yuki-20000/vancouver-311-dashboard)
*   **Weather:** Environment and Climate Change Canada **OGC API**. [\[city-of-va...arcgis.com\]](https://city-of-vancouver-wa-geo-hub-cityofvancouver.hub.arcgis.com/datasets/city-of-vancouver-street-segments/about)
*   **Air Quality:** Metro Vancouver **AirMap** services & **BC AQHI**. [\[geogratis.gc.ca\]](https://geogratis.gc.ca/site/eng/elevation), [\[open.canada.ca\]](https://open.canada.ca/data/en/dataset/7b4fef7e-7cae-4379-97b8-62b03e9ac83d)
*   **Elevation:** City of Vancouver **Digital Elevation Model (LiDAR 2013)**. [\[github.com\]](https://github.com/carsonyl/translink-derived-datasets)

> This repository’s code is licensed under **MIT** (unless you choose differently).  
> Data you download/transform from the sources above **remains under their original licenses**.

***

## 💸 Cost & Hosting Notes

*   Frontend on **GitHub Pages** (free).
*   Backend & routing on **Fly.io/Render** free tiers; cache real‑time sources to stay within limits.
*   Avoid heavy use of free public OSM tiles; prefer MapLibre + self‑hosted or cached vector tiles. (Always include OSM attribution.)

***

## 🤝 Contributing

Issues and PRs are welcome! Please include:

*   What you changed & why
*   Data licenses respected (ODbL/OGL)
*   Screenshots/GIFs for UI changes
*   Any **rate‑limit** or **cost** implications

***

## 📎 Acknowledgements

Thanks to open data stewards and communities:

*   **OSM contributors** and the OSMF for open geodata under ODbL.
*   **City of Vancouver** Open Data teams (Transportation Planning; Parks & Recreation; GIS). [\[wiki.opens...eetmap.org\]](https://wiki.openstreetmap.org/wiki/Attribution_guidelines/2021-06-04_draft), [\[Vancouver City Hall\]](http://www.vancouver.ca/), [\[env.gov.bc.ca\]](https://www.env.gov.bc.ca/epd/bcairquality/data/aqhi-table.html)
*   **Environment & Climate Change Canada** (OGC APIs). [\[city-of-va...arcgis.com\]](https://city-of-vancouver-wa-geo-hub-cityofvancouver.hub.arcgis.com/datasets/city-of-vancouver-street-segments/about)
*   **Metro Vancouver** Air Quality & **BC AQHI** programs. [\[geogratis.gc.ca\]](https://geogratis.gc.ca/site/eng/elevation), [\[open.canada.ca\]](https://open.canada.ca/data/en/dataset/7b4fef7e-7cae-4379-97b8-62b03e9ac83d)

***

### Contact

Questions or suggestions? Open an issue in this repo: **VancouverBiking**.
