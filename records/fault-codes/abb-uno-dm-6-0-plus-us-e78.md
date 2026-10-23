---
id: fc:abb-uno-dm-6-0-plus-us-e78
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E078
aliases:
- E078
- e78
- ABB / FIMER E078
- Riso Test fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E078
code_key: e78
display_message: Riso Test fail
vendor_severity: Error
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:self-test-failure
  note: Failure during the insulation resistance test phase
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r7
    h: 356a321b60fb
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r6
    h: 9a626a2d00d5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r6
    h: ba53827e2aef
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r12
    h: 600dce5282b8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:insulation-monitor
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r7
    h: 356a321b60fb
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r6
    h: 9a626a2d00d5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r6
    h: ba53827e2aef
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r12
    h: 600dce5282b8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
  review_note: 'support check: partial - The Riso (insulation resistance) test is mentioned, but the passages
    don''t name an insulation monitoring device.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r7
    h: 356a321b60fb
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r6
    h: 9a626a2d00d5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r6
    h: ba53827e2aef
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r12
    h: 600dce5282b8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
  review_note: 'support check: partial - Restart is implied as a first step, but the passages don''t say
    it mitigates the fault.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r7
    h: 356a321b60fb
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r6
    h: 9a626a2d00d5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r6
    h: ba53827e2aef
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r12
    h: 600dce5282b8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r7
    h: 356a321b60fb
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r6
    h: 9a626a2d00d5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r6
    h: ba53827e2aef
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r6
    h: ba53827e2aef
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r12
    h: 600dce5282b8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r12
    h: 600dce5282b8
  review: drafted
  review_note: 'support check: partial - Passages say switch off/on and contact assistance if it persists,
    but never state it clears by manual reset; it''s an…'
---
