---
id: fc:abb-pvs-166-175-tl-us-w48
type: FaultCode
name: ABB / FIMER PVS-166-175-TL W048
aliases:
- W048
- w48
- ABB / FIMER W048
- Periodic GridOff
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: W048
code_key: w48
display_message: Periodic GridOff
vendor_severity: Warning
page: 139
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r3
    h: c86bbae59d8b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r3
    h: c86bbae59d8b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:periodic-grid-disconnection
  note: Required disconnection to run the insulation resistance test after the grid-standard time limit
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r8
    h: 1c552187e7fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r4
    h: c89977a731af
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: c89977a731af
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r5
    h: ed6a6728cb2f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r5
    h: ed6a6728cb2f
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Brief disconnection followed by automatic reconnection
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r8
    h: 1c552187e7fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r4
    h: c89977a731af
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: c89977a731af
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r5
    h: ed6a6728cb2f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r5
    h: ed6a6728cb2f
  review: drafted
  review_note: 'support check: partial - Disconnection and reconnection stated, but not described as a
    trip explicitly; reasonable implication.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Contact support only if disconnections happen sooner than expected
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r8
    h: 1c552187e7fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r4
    h: c89977a731af
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: c89977a731af
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r5
    h: ed6a6728cb2f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r5
    h: ed6a6728cb2f
  review: drafted
  review_note: 'support check: partial - Automatic reconnection and contact only if disconnects sooner
    are stated; auto-reset is implied.'
---
