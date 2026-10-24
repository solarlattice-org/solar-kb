---
id: fc:abb-pvs-60-tl-us-e16
type: FaultCode
name: ABB / FIMER PVS-60-TL E016
aliases:
- E016
- e16
- ABB / FIMER E016
- Inverter Fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E016
code_key: e16
display_message: Inverter Fail
vendor_severity: Error
page: 156
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r9
    h: 416405e949fa
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r9
    h: 416405e949fa
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r11
    h: dfac6d52db9d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r11
    h: dfac6d52db9d
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r4
    h: 8c0b968fb8c9
  review: drafted
  review_note: 'support check: partial - The passages describe a problem in the inverter DC/AC circuit,
    but do not call it a power stage fault.'
- claim_id: c4
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r9
    h: 416405e949fa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r4
    h: 8c0b968fb8c9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r4
    h: 8c0b968fb8c9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r4
    h: 8c0b968fb8c9
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists afterwards.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r9
    h: 416405e949fa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r4
    h: 8c0b968fb8c9
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Power cycle then contact service is stated, but clearing by manual
    reset is not stated.'
- claim_id: c8
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r3
    h: e67c24c759de
  review: drafted
---
