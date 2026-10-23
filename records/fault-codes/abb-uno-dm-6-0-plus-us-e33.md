---
id: fc:abb-uno-dm-6-0-plus-us-e33
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E033
aliases:
- E033
- e33
- ABB / FIMER E033
- UTH
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E033
code_key: e33
display_message: UTH
vendor_severity: Error
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 1a05df850357
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r9
    h: 1e8781e01615
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 1a05df850357
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r9
    h: 1e8781e01615
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-undertemperature
  note: Ambient below -25 °C
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r10
    h: f5ed4f8ec21e
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r1
    h: 4bf39c01a85b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r6
    h: 1a05df850357
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 1a05df850357
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r9
    h: 1e8781e01615
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r4
    h: fa59d10539b9
  review: drafted
  review_note: 'support check: partial - Ambient below -25°C is stated, but the passages don''t call it
    inverter undertemperature, though the code UTH/Undertemper. fits.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Clears when temperature returns to range; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r10
    h: f5ed4f8ec21e
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r1
    h: 4bf39c01a85b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r6
    h: 1a05df850357
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 1a05df850357
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r9
    h: 1e8781e01615
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r4
    h: fa59d10539b9
  review: drafted
  review_note: 'support check: partial - Waiting for temperature to return and contacting support if it
    persists are stated, but auto-reset isn''t explicit.'
---
