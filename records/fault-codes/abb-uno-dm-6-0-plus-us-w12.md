---
id: fc:abb-uno-dm-6-0-plus-us-w12
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS W012
aliases:
- W012
- w12
- ABB / FIMER W012
- Batt. Low
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: W012
code_key: w12
display_message: Batt. Low
vendor_severity: Warning
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r2
    h: 431e70c95658
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r2
    h: 431e70c95658
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
---
