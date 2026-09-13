# Data provenance

This prototype's network is built from two real, verifiable sources, queried live
via their public APIs (raw responses saved alongside this file):

## 1. OpenStreetMap (via Overpass API) — `osm_raw.json`
Query window: lat 13.19-13.37, lon 74.68-74.80 (Malpe / Udupi / Manipal / Kaup corridor).
Retrieved: 13 hospitals, 18 clinics, 10 schools, 6 substations, 47 place localities
(towns/suburbs/villages), and 76 bridge-tagged road segments.
License: ODbL, © OpenStreetMap contributors.

25 of the 32 nodes in the simulator use a name and lat/lon taken directly from this
data. OpenStreetMap did **not** have any `man_made=water_works` or
`man_made=pumping_station` tags in this window, and only one substation near the
Udupi city core — those 7 utility nodes are placed at estimated positions and
clearly marked `source:'estimated'` in the app (dashed node outline).

## 2. NASA/USGS SRTM 30m elevation (via OpenTopoData) — `elevations.json`
Every node's elevation, including the estimated utility placeholders, is a real
SRTM30m reading for its coordinate, not invented. Two results anchor the whole
flood model:
- **Malpe Bridge: 0.0m** (real reading) — the actual coastal crossing sits at sea level.
- **Unnamed creek crossing near Kaup: 4.0m** (real reading) — a genuine low point
  between otherwise-higher ground (surrounding localities read 15-27m).

Every hospital in the dataset sits at 24-102m, safely above any realistic storm-surge
range. This is why the simulator's dominant failure mode is **road access being cut
by these two low crossings**, not hospital buildings flooding — a finding driven by
the real data, not assumed in advance.

## What is NOT real data (clearly labeled in-app)
- Population and shelter-capacity figures are planning-order-of-magnitude estimates
  (no population tag existed in OSM for these localities), shown with a `~` prefix.
- Equity/vulnerability multipliers are judgment calls, not measured.
- Power/water dependency edges (which substation feeds which locality) are modeled
  by geographic proximity to the real substation/pump positions, not sourced from a
  utility-company dependency map (none is publicly available).
- Intervention costs (₹ lakh figures) are illustrative planning order-of-magnitude
  tiers, not certified estimates.
- Scenario likelihood weights in the "Robust plan" optimizer are illustrative for
  planning discussion, not measured return-period statistics.
- The map is a schematic projection (independent x/y scaling), not drawn to true
  geographic scale — route-comparison distances are shown as a relative index, not km.

Retrieved 2026-09-13 via `overpass-api.de` and `api.opentopodata.org` (both public,
free, no-auth endpoints).
