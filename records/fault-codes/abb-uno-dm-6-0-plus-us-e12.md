---
id: fc:abb-uno-dm-6-0-plus-us-e12
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E012
aliases:
- E012
- e12
- ABB / FIMER E012
- DcDc Fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E012
code_key: e12
display_message: DcDc Fail
vendor_severity: Error
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: 1072581597a0
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r7
    h: e0524b883746
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: 1072581597a0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r7
    h: e0524b883746
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r7
    h: 40b49dd8ee73
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r9
    h: b7367d84ac37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: 1072581597a0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r7
    h: e0524b883746
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r11
    h: 893002f5a049
  review: drafted
  review_note: 'support check: partial - The passages describe an internal inverter error in the Booster
    circuit, but do not call it an internal device fault…'
- claim_id: c5
  rel: affects
  target: comp:boost-converter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r7
    h: 40b49dd8ee73
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r9
    h: b7367d84ac37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: 1072581597a0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r7
    h: e0524b883746
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r11
    h: 893002f5a049
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r7
    h: 40b49dd8ee73
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r9
    h: b7367d84ac37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: 1072581597a0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r7
    h: e0524b883746
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r11
    h: 893002f5a049
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the error persists.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r7
    h: 40b49dd8ee73
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r9
    h: b7367d84ac37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: 1072581597a0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r7
    h: e0524b883746
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r11
    h: 893002f5a049
  review: drafted
  review_note: 'support check: partial - Power cycle then contact service is stated, but clearing by manual
    reset is not stated.'
---
