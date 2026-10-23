---
id: fc:abb-uno-dm-6-0-plus-us-e77
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E077
aliases:
- E077
- e77
- ABB / FIMER E077
- Internal Error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E077
code_key: e77
display_message: Internal Error
vendor_severity: Error
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r6
    h: 4c1ae4c47cdd
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r5
    h: 2572daf81e9b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r5
    h: 5c69790ac011
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r11
    h: 87239aebbaf3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r6
    h: 4c1ae4c47cdd
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r5
    h: 2572daf81e9b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r5
    h: 5c69790ac011
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r11
    h: 87239aebbaf3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r6
    h: 4c1ae4c47cdd
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r5
    h: 2572daf81e9b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r5
    h: 5c69790ac011
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r11
    h: 87239aebbaf3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
  review_note: 'support check: partial - Restart is implied as a first step, but the passages don''t say
    it mitigates the fault.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r6
    h: 4c1ae4c47cdd
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r5
    h: 2572daf81e9b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r5
    h: 5c69790ac011
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r11
    h: 87239aebbaf3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r6
    h: 4c1ae4c47cdd
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r5
    h: 2572daf81e9b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r5
    h: 5c69790ac011
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 5c69790ac011
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r11
    h: 87239aebbaf3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r11
    h: 87239aebbaf3
  review: drafted
  review_note: 'support check: partial - The power-cycle-then-service sequence is stated, but the passages
    don''t say the fault clears by manual reset.'
---
