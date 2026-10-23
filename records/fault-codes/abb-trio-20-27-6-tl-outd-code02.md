---
id: fc:abb-trio-20-27-6-tl-outd-code02
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL CODE:02
aliases:
- CODE:02
- code02
- ABB / FIMER CODE:02
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: CODE:02
code_key: code02
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r3
    h: ce5b66c1f3c3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r3
    h: d30e5976b8e0
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r3
    h: a329616ef69f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r3
    h: a329616ef69f
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r3
    h: ce5b66c1f3c3
  review: drafted
  review_note: 'support check: partial - Limitation is due to overvoltage of average grid voltage, but
    it is a user-set derating rather than a direct grid…'
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: Power limitation message; inverter keeps operating at reduced output
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r3
    h: d30e5976b8e0
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r3
    h: a329616ef69f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r3
    h: a329616ef69f
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r3
    h: ce5b66c1f3c3
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h262
    h: ff3e2268fa02
  review: drafted
  review_note: 'support check: partial - Power limitation with the inverter continuing is stated, but
    warning classification is only implied, not explicit.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Limit percentage is variable; the 50 percent figure is only an example
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r3
    h: d30e5976b8e0
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r3
    h: a329616ef69f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r3
    h: a329616ef69f
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r3
    h: ce5b66c1f3c3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Limit comes from the user-set 10-minute average overvoltage derating parameter
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r3
    h: d30e5976b8e0
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r3
    h: a329616ef69f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r3
    h: a329616ef69f
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r3
    h: ce5b66c1f3c3
  review: drafted
---
