---
id: prod:sma-sunny-island
type: Product
name: Sunny Island 4.4M / 6.0H / 8.0H
aliases:
- SI 4.4M
- SI 6.0H
- SI 8.0H
- Sunny Island 6.0H
- Sunny Island
- SI4.4M-13
- SI6.0H-13
- SI8.0H-13
- SI4.4M-12
- SI6.0H-12
- SI8.0H-12
- SI4.4M-11
- SI6.0H-11
- SI8.0H-11
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: sec=1.1
    h: ee9662fba317
  - src: src:sma-doc-278303
    loc: sec=2.1
    h: d5fde0d85e95
  review: drafted
  review_note: 'support check: partial - Passages name the devices as SMA Flexible Storage System device
    types, but never state SMA is the manufacturer in an explicit manufacturer relation (only implied
    by ''SMA'' in the system name).'
- claim_id: c2
  attr: rated_power
  value:
    nominal: 3300
    unit: unit:W
  conditions: Sunny Island 4.4M rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=23
    h: 85602c706c7d
  - src: src:sma-doc-259463
    loc: tbl=23.r1
    h: 4691ffc191e4
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions)
- claim_id: c3
  attr: rated_power
  value:
    nominal: 4600
    unit: unit:W
  conditions: Sunny Island 6.0H rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=23
    h: 85602c706c7d
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions)
- claim_id: c4
  attr: rated_power
  value:
    nominal: 6000
    unit: unit:W
  conditions: Sunny Island 8.0H rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=23
    h: 85602c706c7d
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions)
---
The Sunny Island 4.4M, 6.0H and 8.0H are SMA battery inverters, and the documents refer to all three together as the Sunny Island. Rated output power is 3300 W for the 4.4M, 4600 W for the 6.0H and 6000 W for the 8.0H. For backup systems, the maximum tripping characteristic is B6 for the 4.4M and B16 for the 6.0H and 8.0H. SMA publishes a list of lithium-ion battery makers approved for use with these inverters.

<!-- review notes
- sentence 3: support check: partial - The tripping characteristics B6 and B16 are stated, but the passages don't say they apply specifically to backup systems.
-->
