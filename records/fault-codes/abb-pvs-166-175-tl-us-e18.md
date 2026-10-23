---
id: fc:abb-pvs-166-175-tl-us-e18
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E018
aliases:
- E018
- e18
- ABB / FIMER E018
- Leak fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E018
code_key: e18
display_message: Leak fault
vendor_severity: Error
page: 141
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r5
    h: c85485f0064f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 8b960b8e4fb9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r11
    h: 8b960b8e4fb9
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r1
    h: 8d94a07800dd
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r6
    h: 5c456fb6cb36
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r5
    h: c85485f0064f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 8b960b8e4fb9
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r5
    h: c85485f0064f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 8b960b8e4fb9
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:insulation-resistance-test
  note: Measure under the same environmental conditions as the error; 1 megaohm threshold.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r5
    h: c85485f0064f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 8b960b8e4fb9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r11
    h: 8b960b8e4fb9
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r1
    h: 8d94a07800dd
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r6
    h: 5c456fb6cb36
  review: drafted
  review_note: 'support check: partial - The passages give the insulation resistance measurement under
    the same conditions with a 1 megaohm threshold. They describe it as…'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-installer
  note: When resistance below 1 megaohm; otherwise contact service if alarm persists.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r5
    h: c85485f0064f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 8b960b8e4fb9
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: When resistance is above 1 megaohm and the alarm persists.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r2
    h: 2d7c93565057
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r5
    h: c85485f0064f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r11
    h: 8b960b8e4fb9
  review: drafted
---
