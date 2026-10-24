---
id: fc:abb-pvs-60-tl-us-w46
type: FaultCode
name: ABB / FIMER PVS-60-TL W046
aliases:
- W046
- w46
- ABB / FIMER W046
- Grid conn. fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W046
code_key: w46
display_message: Grid conn. fault
vendor_severity: Warning
page: 154
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  review: drafted
- claim_id: c3
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
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  review: drafted
---
