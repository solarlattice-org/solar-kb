---
id: fc:abb-pvs-166-175-tl-us-e2
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E002
aliases:
- E002
- e2
- ABB / FIMER E002
- Input OV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E002
code_key: e2
display_message: Input OV
vendor_severity: Error
page: 139
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r12
    h: 7fb81d0cdd63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r8
    h: c92424d52505
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r8
    h: c92424d52505
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r9
    h: b5278e0746fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r9
    h: b5278e0746fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r2
    h: e1b0f3237f9c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r12
    h: 7fb81d0cdd63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r8
    h: c92424d52505
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r8
    h: c92424d52505
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r9
    h: b5278e0746fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r9
    h: b5278e0746fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r2
    h: e1b0f3237f9c
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r12
    h: 7fb81d0cdd63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r8
    h: c92424d52505
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r8
    h: c92424d52505
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r9
    h: b5278e0746fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r9
    h: b5278e0746fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r2
    h: e1b0f3237f9c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when measured voltage exceeds the operating range; otherwise internal malfunction, contact
    service.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r12
    h: 7fb81d0cdd63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r8
    h: c92424d52505
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r8
    h: c92424d52505
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r9
    h: b5278e0746fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r9
    h: b5278e0746fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r2
    h: e1b0f3237f9c
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Inverter does not start while input exceeds the overvoltage threshold.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r7
    h: 81d08857ddbe
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r12
    h: 7fb81d0cdd63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r8
    h: c92424d52505
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r8
    h: c92424d52505
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r9
    h: b5278e0746fb
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r9
    h: b5278e0746fb
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r2
    h: e1b0f3237f9c
  review: drafted
---
