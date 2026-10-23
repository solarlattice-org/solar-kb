---
id: fc:abb-pvs-166-175-tl-us-e54
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E054
aliases:
- E054
- e54
- ABB / FIMER E054
- AFDD comm. Fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E054
code_key: e54
display_message: AFDD comm. Fault
vendor_severity: Error
page: 144
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  note: Serial link between inverter and arc detection board
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r11
    h: 2253563b3bbb
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r14
    h: dd4f897b70ee
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r14
    h: dd4f897b70ee
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 3b11ed9361e3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r11
    h: 2253563b3bbb
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r14
    h: dd4f897b70ee
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r14
    h: dd4f897b70ee
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 3b11ed9361e3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r11
    h: 2253563b3bbb
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r14
    h: dd4f897b70ee
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r14
    h: dd4f897b70ee
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 3b11ed9361e3
  review: drafted
  review_note: 'support check: partial - Restart is implied as a first step, but the passages don''t say
    it mitigates the fault.'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r11
    h: 2253563b3bbb
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r14
    h: dd4f897b70ee
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r14
    h: dd4f897b70ee
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 3b11ed9361e3
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r1
    h: 9567bd31690a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r11
    h: 2253563b3bbb
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r14
    h: dd4f897b70ee
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r14
    h: dd4f897b70ee
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 3b11ed9361e3
  review: drafted
  review_note: 'support check: partial - The power-cycle-then-service sequence is stated, but the passages
    don''t say the fault clears by manual reset.'
---
