---
id: fc:abb-uno-dm-6-0-plus-us-w15
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS W015
aliases:
- W015
- w15
- ABB / FIMER W015
- Island Detect.
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: W015
code_key: w15
display_message: Island Detect.
vendor_severity: Warning
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r4
    h: f3324fb791da
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r4
    h: 9041a81bf5ce
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r4
    h: f3324fb791da
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r4
    h: 9041a81bf5ce
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r3
    h: 7961c68b1b44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r4
    h: f3324fb791da
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r4
    h: f3324fb791da
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: 9041a81bf5ce
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r4
    h: 9041a81bf5ce
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Inverter disconnects by anti-islanding protection
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r3
    h: 7961c68b1b44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r4
    h: f3324fb791da
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r4
    h: f3324fb791da
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: 9041a81bf5ce
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r4
    h: 9041a81bf5ce
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r3
    h: 7961c68b1b44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r4
    h: f3324fb791da
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r4
    h: f3324fb791da
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: 9041a81bf5ce
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r4
    h: 9041a81bf5ce
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Switch off and on; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r3
    h: 7961c68b1b44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r4
    h: f3324fb791da
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r4
    h: f3324fb791da
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: 9041a81bf5ce
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r4
    h: 9041a81bf5ce
  review: drafted
  review_note: 'support check: partial - Switch off/on is an operator restart (manual reset) but only
    when grid is an island grid, and the passages don''t…'
---
