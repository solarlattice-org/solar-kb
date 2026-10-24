---
id: fc:abb-trio-20-27-6-tl-outd-e49
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL E049
aliases:
- E049
- e49
- ABB / FIMER E049
- AC FF Error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: E049
code_key: e49
display_message: AC FF Error
vendor_severity: Error
page: 113
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  note: Fault in the AC feed-forward circuit inside the inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r6
    h: d6b422a94153
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r7
    h: 15f8077cb0c9
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r11
    h: 1bb507c245bf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 1bb507c245bf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r3
    h: ae46bfedad43
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: ae46bfedad43
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r6
    h: d6b422a94153
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r7
    h: 15f8077cb0c9
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r11
    h: 1bb507c245bf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 1bb507c245bf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r3
    h: ae46bfedad43
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: ae46bfedad43
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r6
    h: d6b422a94153
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r7
    h: 15f8077cb0c9
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r11
    h: 1bb507c245bf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 1bb507c245bf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r3
    h: ae46bfedad43
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: ae46bfedad43
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the error persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r6
    h: d6b422a94153
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r7
    h: 15f8077cb0c9
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r11
    h: 1bb507c245bf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 1bb507c245bf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r3
    h: ae46bfedad43
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: ae46bfedad43
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r6
    h: d6b422a94153
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r7
    h: 15f8077cb0c9
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r11
    h: 1bb507c245bf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 1bb507c245bf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r3
    h: ae46bfedad43
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: ae46bfedad43
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
  review_note: 'support check: partial - Power cycle then contact service is stated, but manual-reset
    clearing is not explicit.'
- claim_id: c8
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r10
    h: b3e01c1c5fde
  review: drafted
---
