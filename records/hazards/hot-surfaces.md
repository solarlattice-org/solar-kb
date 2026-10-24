---
id: hazard:hot-surfaces
type: Hazard
name: Hot surfaces
aliases:
- burn hazard
- hot surface
- Beware of hot surface
category: Thermal
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:avoid-hot-surface-contact
  note: CPS and Solectria manuals name the heat sink and surrounding surfaces, during operation and shortly
    after it; SMA manuals say not to touch the product while it is running.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=h15
    h: 94eb676cd43a
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=h15
    h: 94eb676cd43a
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: sec=h14
    h: 94eb676cd43a
  - src: src:chint-cps-36kw-user-manual-2024
    loc: sec=h15
    h: 94eb676cd43a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: sec=h17
    h: 94eb676cd43a
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h16
    h: 0268ba331d92
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=h17
    h: 5c3b8a5498df
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h37
    h: f95171c3ab6f
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: sec=h47
    h: ed9c65fec77b
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h11
    h: b6748c10b7ed
  - src: src:eq-equip-inverters-sma-stp-core1-50-stp-core-1-user-manual-v1-0-50-62
    loc: sec=h11
    h: b6748c10b7ed
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:cool-down-before-work
  note: SMA inverter manuals give a 30-minute wait for the surface to cool enough before work.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h37
    h: f95171c3ab6f
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: sec=h47
    h: ed9c65fec77b
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-quickrefguide
    loc: sec=h33
    h: f95171c3ab6f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h36
    h: f95171c3ab6f
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h36
    h: f95171c3ab6f
  - src: src:eq-equip-inverters-sma-stp-20000-stp20000tl-us-10-installation
    loc: sec=h24
    h: f95171c3ab6f
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:inaccessible-mounting
  scope:
    products:
    - prod:sma-stp-tl-us
    - prod:sma-shp-peak3
    - prod:sma-sb-us-41
    - prod:sma-sb-us-40
  note: Mount the inverter where people cannot touch it by accident.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h37
    h: f95171c3ab6f
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-quickrefguide
    loc: sec=h33
    h: f95171c3ab6f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h36
    h: f95171c3ab6f
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h36
    h: f95171c3ab6f
  - src: src:eq-equip-inverters-sma-stp-20000-stp20000tl-us-10-installation
    loc: sec=h24
    h: f95171c3ab6f
  review: drafted
  review_note: 'support check: partial - Passages state mounting so the inverter can''t be touched inadvertently,
    but they don''t mention the listed product IDs, so the scope isn''t confirmed.'
- claim_id: c4
  rel: controlled_by
  target: mit:observe-safety-labels
  scope:
    products:
    - prod:sma-stp-tl-us
    - prod:sma-shp-peak3
    - prod:sma-sb-us-41
    - prod:sma-sb-us-40
  note: Follow the hot-surface safety messages on the inverter. The label is explained as 'Beware of hot
    surface'.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h37
    h: f95171c3ab6f
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-quickrefguide
    loc: sec=h33
    h: f95171c3ab6f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h36
    h: f95171c3ab6f
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h36
    h: f95171c3ab6f
  - src: src:eq-equip-inverters-sma-stp-20000-stp20000tl-us-10-installation
    loc: sec=h24
    h: f95171c3ab6f
  review: drafted
  review_note: 'support check: partial - Passages say to observe the safety messages on the inverter,
    but the ''Beware of hot surface'' label explanation isn''t in these passages and the product scope
    isn''t stated.'
---
Inverter surfaces get hot during normal operation, and touching them can burn you. The heat sink and the surfaces around it are the main danger, and they stay hot for some time after the unit stops running. Do not touch the product while it is running, and let it cool down enough before you start any work. SMA manuals say to wait 30 minutes for the surface to cool enough. Mount the inverter where nobody can touch it by accident, and follow the hot-surface safety messages on the unit.

<!-- review notes
- sentence 2: support check: partial - Heat sink and peripheral surfaces and 'shortly after operation' are stated, but not that they are the main danger or that they stay hot for some time.
-->
