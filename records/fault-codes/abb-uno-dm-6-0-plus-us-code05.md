---
id: fc:abb-uno-dm-6-0-plus-us-code05
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS CODE:05
aliases:
- CODE:05
- code05
- ABB / FIMER CODE:05
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: CODE:05
code_key: code05
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r1
    h: 672af0ce9fd1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r1
    h: 61049c341a9f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r1
    h: 672af0ce9fd1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r1
    h: 672af0ce9fd1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r3
    h: fa1243509e47
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r1
    h: 61049c341a9f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r1
    h: 672af0ce9fd1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r1
    h: 672af0ce9fd1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r3
    h: fa1243509e47
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h262
    h: ff3e2268fa02
  review: drafted
  review_note: 'support check: partial - Limitation with continued operation implies warning, but not
    explicitly stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Limit percentage is variable; the 50 percent figure is only an example
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r1
    h: 61049c341a9f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r1
    h: 672af0ce9fd1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r1
    h: 672af0ce9fd1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r3
    h: fa1243509e47
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r1
    h: 61049c341a9f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r1
    h: 672af0ce9fd1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r1
    h: 672af0ce9fd1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r3
    h: fa1243509e47
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Clears once the inverter cools down; contact service if it persists after ambient temperature
    is back in range
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=52.r1
    h: 61049c341a9f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=59.r1
    h: 672af0ce9fd1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r1
    h: 672af0ce9fd1
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=43.r3
    h: fa1243509e47
  review: drafted
  review_note: 'support check: partial - Wait for cooldown and contact assistance if persists is stated,
    but auto-reset clearing isn''t explicitly stated.'
---
