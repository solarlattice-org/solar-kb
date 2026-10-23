---
id: fc:abb-pvs-60-tl-us-e81
type: FaultCode
name: ABB / FIMER PVS-60-TL E081
aliases:
- E081
- e81
- ABB / FIMER E081
- Internal Error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E081
code_key: e81
display_message: Internal Error
vendor_severity: Error
page: 159
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r8
    h: f0bb385ac1f5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r8
    h: f0bb385ac1f5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r8
    h: f0bb385ac1f5
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r1
    h: 02b8eb3b3ed2
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r1
    h: 02b8eb3b3ed2
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r8
    h: f0bb385ac1f5
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r1
    h: 02b8eb3b3ed2
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r1
    h: 02b8eb3b3ed2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:enclosure-sealing-check
  note: Applies after maintenance or installation work on the cover or glands; otherwise contact service
    directly.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r8
    h: f0bb385ac1f5
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r1
    h: 02b8eb3b3ed2
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r1
    h: 02b8eb3b3ed2
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Reconnect and switch on after checks; service required if it persists or no work was done.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r8
    h: f0bb385ac1f5
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r1
    h: 02b8eb3b3ed2
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r1
    h: 02b8eb3b3ed2
  review: drafted
  review_note: 'support check: partial - Reconnect and switch on after checks, contact assistance if persists,
    are stated, but manual reset is only implied.'
---
