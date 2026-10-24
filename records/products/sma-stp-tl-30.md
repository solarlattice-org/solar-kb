---
id: prod:sma-stp-tl-30
type: Product
name: Sunny Tripower 15000-25000TL-30
aliases:
- STP 15000-25000TL-30
- STP xx000TL-30
- Sunny Tripower 15000TL
- Sunny Tripower 17000TL
- Sunny Tripower 20000TL
- Sunny Tripower 25000TL
- STP 15000TL-30
- STP 17000TL-30
- STP 20000TL-30
- STP 25000TL-30
- STP15000TL-30
- STP25000TL-30
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-sunny-tripower-manuals
    loc: sec=h1
    h: b48a3498e573
  review: drafted
  review_note: 'support check: partial - The passages list Sunny Tripower inverters on SMA''s own service
    site, but nothing states outright that SMA makes them. The "SMA" attribution comes only from the site
    name and the SMA device tables.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Listed as a PV inverter in an SMA device compatibility table.
  cite:
  - src: src:sma-doc-275857
    loc: tbl=3
    h: 63e5d75ca23e
  review: drafted
- claim_id: c3
  rel: lacks
  target: func:system-manager
  scope:
    firmware_min: 3.10.xx.R
  note: The SMA device table marks System Manager functionality with a dash for the STP 15000TL-30 to
    25000TL-30 models.
  cite:
  - src: src:sma-doc-275857
    loc: tbl=3.r3
    h: 0e8516f66e63
  - src: src:sma-doc-275857
    loc: tbl=3
    h: 63e5d75ca23e
  review: drafted
---
The Sunny Tripower 15000-25000TL-30 is an SMA family of three-phase PV inverters. It covers the STP 15000TL-30, 17000TL-30, 20000TL-30 and 25000TL-30 models. An SMA device compatibility list includes these models from firmware version 3.10.xx.R. The same list marks them as not offering System Manager functionality. A second SMA device list gives inverter firmware version 02.80.04.R as the minimum for the STP 15000TL-30, 20000TL-30 and 25000TL-30. SMA offers a power assembly spare-part set and an AC assembly spare-part set for the Sunny Tripower 15000TL, 20000TL and 25000TL. Each set has its own multilingual replacement manual. SMA's Sunny Tripower manuals page includes eManuals for this family.

<!-- review notes
- sentence 1: support check: partial - The four models are listed as PV inverters, but the passages never call them three-phase or describe the family as one group.
- sentence 4: support check: partial - AC assembly and power assembly spare-part sets for the 15000TL / 20000TL / 25000TL are listed. The passages show only an English "Replacement Manual" entry, so the claim of separate multilingual manuals per set is not confirmed.
-->
