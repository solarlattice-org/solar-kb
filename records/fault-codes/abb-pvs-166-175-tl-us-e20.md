---
id: fc:abb-pvs-166-175-tl-us-e20
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E020
aliases:
- E020
- e20
- ABB / FIMER E020
- Internal error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E020
code_key: e20
display_message: Internal error
vendor_severity: Error
page: 141
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 68d6ef7f3a5e
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 68d6ef7f3a5e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r3
    h: 74e230ac2bbf
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r8
    h: 6eadb79c6052
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 68d6ef7f3a5e
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:boost-converter
  note: Relay of the DC-DC booster stage.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 68d6ef7f3a5e
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Occurs only before grid connection, so the inverter does not connect.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 68d6ef7f3a5e
  review: drafted
  review_note: 'support check: partial - The passages say the alarm occurs only before grid connection
    and the test failed, but they never say production stops…'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists afterwards.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r7
    h: c5630c6556a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 68d6ef7f3a5e
  review: drafted
  review_note: 'support check: partial - A power cycle is advised, but the passages never say the fault
    clears by manual reset. The only follow-up stated…'
- claim_id: c10
  rel: applies_to
  target: prod:abb-pvs-166-175-tl-us
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r4
    h: b5b4664cc538
  review: drafted
---
