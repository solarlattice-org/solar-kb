---
id: fc:abb-trio-20-27-6-tl-outd-w12
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL W012
aliases:
- W012
- w12
- ABB / FIMER W012
- Batt. Flat
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: W012
code_key: w12
display_message: Batt. Flat
vendor_severity: Warning
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r3
    h: 078ce4c16243
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r3
    h: 078ce4c16243
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:clock-battery-low
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r1
    h: 298b1ff70174
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 431e70c95658
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r2
    h: 431e70c95658
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:backup-battery
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r1
    h: 298b1ff70174
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 431e70c95658
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r2
    h: 431e70c95658
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clock-reset
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r1
    h: 298b1ff70174
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 431e70c95658
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r2
    h: 431e70c95658
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:backup-battery-replacement
  note: When date/time reverts to default after full power-off and restart
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r1
    h: 298b1ff70174
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 431e70c95658
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r2
    h: 431e70c95658
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r3
    h: 078ce4c16243
  review: drafted
---
