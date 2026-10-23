---
id: fc:abb-uno-dm-3-3-5-0-plus-us-w58
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS W058
aliases:
- W058
- w58
- ABB / FIMER W058
- System Frozen
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: W058
code_key: w58
display_message: System Frozen
vendor_severity: Warning
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r6
    h: dae742fba622
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r7
    h: dbd86f1e8310
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r6
    h: dae742fba622
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r7
    h: dbd86f1e8310
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:operation-inhibited
  note: Converter locked until commissioning sets startup and grid connection conditions
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r10
    h: 284eac9626a4
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r6
    h: dae742fba622
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: dae742fba622
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r7
    h: dbd86f1e8310
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r7
    h: 85b200e243a8
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Converter does not start or connect while locked
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r10
    h: 284eac9626a4
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r6
    h: dae742fba622
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: dae742fba622
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r7
    h: dbd86f1e8310
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r7
    h: 85b200e243a8
  review: drafted
  review_note: 'support check: partial - The locked state and missing startup/grid-connection conditions
    are stated, but the passages never say production stops or that the converter…'
- claim_id: c6
  rel: mitigated_by
  target: mit:complete-device-configuration
  note: Finish commissioning; if it persists after a restart, contact support
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r10
    h: 284eac9626a4
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r6
    h: dae742fba622
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: dae742fba622
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r7
    h: dbd86f1e8310
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r7
    h: 85b200e243a8
  review: drafted
---
