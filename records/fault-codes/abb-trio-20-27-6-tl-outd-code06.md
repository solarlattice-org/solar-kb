---
id: fc:abb-trio-20-27-6-tl-outd-code06
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL CODE:06
aliases:
- CODE:06
- code06
- ABB / FIMER CODE:06
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: CODE:06
code_key: code06
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  note: Some manuals label the input overvoltage as AC; the input voltage measurement points to the DC
    side
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h262
    h: ff3e2268fa02
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Power limitation with continued operation implies warning, but
    class isn''t explicit.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Limit percentage is variable; the 50 percent figure is only an example
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When the measured input voltage is above the operating range maximum
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
  review_note: 'support check: partial - Check PV generator configuration when voltage is above range
    is stated, but ''string configuration correction'' is a slightly stronger action.'
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: When the measured voltage is within range, which points to an internal malfunction
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r2
    h: ab0fd3beeef6
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r2
    h: bfaaaaca05fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r2
    h: bfaaaaca05fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r4
    h: 2ade33456bef
  review: drafted
---
