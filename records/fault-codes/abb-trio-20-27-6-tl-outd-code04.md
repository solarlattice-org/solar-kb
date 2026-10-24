---
id: fc:abb-trio-20-27-6-tl-outd-code04
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL CODE:04
aliases:
- CODE:04
- code04
- ABB / FIMER CODE:04
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: CODE:04
code_key: code04
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r5
    h: 4d9606c648cb
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r5
    h: cd3db30e04d1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r5
    h: cd3db30e04d1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r5
    h: 4d9606c648cb
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r5
    h: cd3db30e04d1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r5
    h: cd3db30e04d1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h262
    h: ff3e2268fa02
  review: drafted
  review_note: 'support check: partial - Output limitation while operating implies warning, but class
    isn''t explicit.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Limitation may occur; the percentage is variable and 50 percent is only an example
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r5
    h: 4d9606c648cb
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r5
    h: cd3db30e04d1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r5
    h: cd3db30e04d1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r5
    h: 4d9606c648cb
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r5
    h: cd3db30e04d1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r5
    h: cd3db30e04d1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  review: drafted
  review_note: 'support check: partial - Grid voltage is checked as part of the solution, but detection
    by measurement is only loosely implied.'
- claim_id: c6
  rel: mitigated_by
  target: mit:utility-consultation
  note: Only if the low grid voltage condition persists
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r5
    h: 4d9606c648cb
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r5
    h: cd3db30e04d1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r5
    h: cd3db30e04d1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r2
    h: c17952906c97
  review: drafted
---
