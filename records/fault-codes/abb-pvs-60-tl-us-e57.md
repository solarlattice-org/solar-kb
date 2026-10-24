---
id: fc:abb-pvs-60-tl-us-e57
type: FaultCode
name: ABB / FIMER PVS-60-TL E057
aliases:
- E057
- e57
- ABB / FIMER E057
- Vbulk reading error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E057
code_key: e57
display_message: Vbulk reading error
vendor_severity: Error
page: 159
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  note: Input voltage exceeds internal bulk voltage; may be a false reading from internal malfunction
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r3
    h: 5fc2d69c30d9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r3
    h: 48ff173bd832
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 48ff173bd832
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: b8b62dd1e311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r2
    h: 297e1c80ae5e
  review: drafted
  review_note: 'support check: partial - Vin exceeding Vbulk, and a possible internal malfunction, are
    stated, but the passages don''t call it a DC overvoltage. The…'
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r3
    h: 5fc2d69c30d9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r3
    h: 48ff173bd832
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 48ff173bd832
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: b8b62dd1e311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r2
    h: 297e1c80ae5e
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  note: When measured input exceeds the operating range
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r3
    h: 5fc2d69c30d9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r3
    h: 48ff173bd832
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 48ff173bd832
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: b8b62dd1e311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r2
    h: 297e1c80ae5e
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:boost-converter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r3
    h: 5fc2d69c30d9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r3
    h: 48ff173bd832
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 48ff173bd832
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: b8b62dd1e311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r2
    h: 297e1c80ae5e
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When input voltage is genuinely above the operating range
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r3
    h: 5fc2d69c30d9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r3
    h: 48ff173bd832
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 48ff173bd832
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: b8b62dd1e311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r2
    h: 297e1c80ae5e
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: When input voltage is within range, indicating internal malfunction
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r3
    h: 5fc2d69c30d9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r3
    h: 48ff173bd832
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 48ff173bd832
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: b8b62dd1e311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r2
    h: 297e1c80ae5e
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r2
    h: 6a7f23b5a822
  review: drafted
---
