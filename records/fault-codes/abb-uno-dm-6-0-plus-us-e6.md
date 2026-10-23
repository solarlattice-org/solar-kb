---
id: fc:abb-uno-dm-6-0-plus-us-e6
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E006
aliases:
- E006
- e6
- ABB / FIMER E006
- Output OC
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E006
code_key: e6
display_message: Output OC
vendor_severity: Error
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r12
    h: 17128e36791b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r2
    h: f60bfb607205
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r12
    h: 17128e36791b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r2
    h: f60bfb607205
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r2
    h: bc31b433a887
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r4
    h: ee594f6cca18
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r12
    h: 17128e36791b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r12
    h: 17128e36791b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r2
    h: f60bfb607205
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r6
    h: fd1aa8ff3420
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r2
    h: bc31b433a887
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r4
    h: ee594f6cca18
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r12
    h: 17128e36791b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r12
    h: 17128e36791b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r2
    h: f60bfb607205
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r6
    h: fd1aa8ff3420
  review: drafted
  review_note: 'support check: partial - Switching off and on is a step before contacting assistance;
    the passages do not say it resolves the error.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the error persists.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r2
    h: bc31b433a887
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r4
    h: ee594f6cca18
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r12
    h: 17128e36791b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r12
    h: 17128e36791b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r2
    h: f60bfb607205
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r6
    h: fd1aa8ff3420
  review: drafted
  review_note: 'support check: partial - A power cycle is listed, but the passages do not say a manual
    reset clears the error.'
---
