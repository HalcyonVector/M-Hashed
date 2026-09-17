# Ripple: Cascading Infrastructure Failure Simulator

**Live app:** [`index.html`](index.html)
**Field guide:** [`field-guide.html`](field-guide.html)

A client-side simulator of cascading infrastructure failure across a real coastal corridor: Malpe, Udupi, Manipal and Kaup, Karnataka. Built for Manipal Hackathon 2026, Round 1, under the theme "The Butterfly Effect," for the problem statement "Cascading Failure: When One Failure Becomes Many" (SDG 11, Sustainable Cities and Communities). Every node position and elevation reading is real, pulled from OpenStreetMap and NASA/USGS SRTM data, not fabricated. Vanilla HTML, CSS and JavaScript, no framework, no backend, no build step, runs entirely in the browser.

---

## Features

- Interactive water-level slider that drives a live cascade simulation, with presets from a normal high tide to an extreme flood
- 32 real assets, hospitals, schools, shelters, substations, pumps, bridges and residential localities, across Udupi, Manipal and Kaup
- Direct failure by real elevation against the chosen water level, and indirect cascade failure traced through power, water and road dependency edges (BFS propagation)
- Equity-weighted impact score: population served, multiplied by a vulnerability weight, summed across every failed asset
- Betweenness centrality ranking of critical assets (Brandes' algorithm, unweighted), independent of today's water level
- Dijkstra-based shortest-route-versus-safest-route comparison for reaching a hospital
- Capacity-aware overload modeling: substations and pumps have a rated capacity, and a backup tie can rescue a failed peer only up to that limit, distinct from a plain up-or-down failure
- Budget-constrained multi-scenario intervention optimizer (knapsack over a small set of real interventions), recommending which fix helps most per rupee across weighted illustrative scenarios
- Pan and zoom vector map, drawn from real coastline geometry, not a static image
- Plain-language onboarding banner for first-time visitors, reopenable any time from the header

---

## Data Source

The network is built from two real, verifiable sources, queried live via their public APIs. Raw responses are saved in `data/`.

1. **OpenStreetMap**, via the Overpass API (`data/osm_raw.json`). Query window: lat 13.19 to 13.37, lon 74.68 to 74.80, the Malpe, Udupi, Manipal and Kaup corridor. 25 of the 32 nodes use a name and coordinate taken directly from this data. Licensed ODbL, (c) OpenStreetMap contributors.
2. **NASA/USGS SRTM 30m elevation**, via the OpenTopoData API (`data/elevations.json`). Every node's elevation, including the estimated utility placeholders, is a real SRTM30m reading for its coordinate.

7 utility nodes (water works, pumping stations) that OpenStreetMap does not tag in this window are placed at estimated positions, clearly marked `source: estimated` in the app with a dashed outline. Population figures, dependency edges, capacities and intervention costs are documented, labeled planning estimates, not sourced data. The full breakdown of what is real versus estimated lives in [`data/PROVENANCE.md`](data/PROVENANCE.md).

---

## A finding the data produced

Every hospital in the dataset sits at 24 to 102 metres of real elevation, safely above any realistic storm surge. The two lowest points in the entire network are road crossings, not buildings: Malpe Bridge at 0.0 metres, and an unnamed creek crossing near Kaup at 4.0 metres. Cutting either one leaves people without hospital access while every hospital itself stays dry. This is the simulator's dominant failure mode, and it fell out of the real elevation data. It was not designed in ahead of time.

---

## Tech Stack

| Layer | Tech |
|---|---|
| Frontend | Vanilla HTML, CSS, JavaScript. No framework, no build step |
| Rendering | Hand-built SVG, manual viewBox pan and zoom |
| Fonts | Big Shoulders, IBM Plex Sans, IBM Plex Mono (Google Fonts) |
| Data | Static JSON, fetched once at load, no backend |
| Algorithms | BFS cascade propagation, Brandes' betweenness centrality, Dijkstra shortest path, knapsack budget optimizer |
| Persistence | `localStorage`, for the dismissible onboarding banner only |

---

## Project Structure

```
Ripple/
├── index.html              The simulator: nodes, edges, simulation engine and UI, all in one file
├── field-guide.html         Plain-language reference for every marker, line and number in the simulator
└── data/
    ├── PROVENANCE.md         Full accounting of what is real data versus estimated
    ├── osm_raw.json           Raw Overpass API response
    ├── elevations.json        Raw OpenTopoData SRTM30m response
    ├── nodes_merged.json      OSM and elevation data, merged per node
    ├── nodes_projected.json   Nodes projected to the map's local x/y coordinate space
    ├── coastline_raw.json
    ├── coastline_projected.json
    ├── coastline_final.json
    ├── coastline_chains.json  Real coastline geometry, at each stage of extraction and projection
    ├── coastline_js.txt       Final coastline geometry, formatted for direct use in index.html
    ├── nodes_draft.py         Script used to merge and project the node data
    └── basemap/               An earlier raster-tile basemap approach, tried and reverted (see PROVENANCE.md)
```

---

## Quick Start

No install, no server, no build step.

```bash
git clone https://github.com/HalcyonVector/M-Hashed.git
cd M-Hashed
```

Open `index.html` directly in any browser, or use the live link at the top of this file.

---

## Authors

Sagnik Basu

Man Mohit Kumar

Yashaswi Mohan

Pagavath D P

Amritanshu
