---
id: fc:abb-uno-dm-6-0-plus-us-w46
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS W046
aliases:
- W046
- w46
- ABB / FIMER W046
- Grid conn. fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: W046
code_key: w46
display_message: Grid conn. fault
vendor_severity: Warning
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-connection-failure
  note: Logged after missing grid, input undervoltage, or manual disconnection during connection
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r3
    h: 181de4964c85
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r3
    h: 181de4964c85
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: drafted
  review_note: 'support check: partial - Grid connection unsuccessful implies no feed-in, but a trip is
    not explicitly stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Retries automatically; if it persists, restart, then contact support
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r3
    h: 181de4964c85
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  note: Only after repeated automatic connection attempts fail
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r3
    h: 181de4964c85
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:abb-uno-dm-6-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r3
    h: 181de4964c85
  review: drafted
---
