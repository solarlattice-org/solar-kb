---
id: fc:abb-pvs-166-175-tl-us-e10
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E010
aliases:
- E010
- e10
- ABB / FIMER E010
- Bulk UV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E010
code_key: e10
display_message: Bulk UV
vendor_severity: Error
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r5
    h: d3f062b601b7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r5
    h: d3f062b601b7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r5
    h: d3f062b601b7
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r7
    h: 6698d0568860
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r3
    h: 2a5f8c4ec53e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r5
    h: 26380b7fac19
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r9
    h: fddb829589b0
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:boost-converter
  note: Sporadic cases stem from low irradiance; systematic cases at high irradiance need service.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r5
    h: d3f062b601b7
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r7
    h: 6698d0568860
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r3
    h: 2a5f8c4ec53e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r5
    h: 26380b7fac19
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r9
    h: fddb829589b0
  review: drafted
  review_note: 'support check: partial - Low bulk voltage in the DC-DC circuit and the sporadic/systematic
    split are stated, but the passages never name the boost converter.'
---
