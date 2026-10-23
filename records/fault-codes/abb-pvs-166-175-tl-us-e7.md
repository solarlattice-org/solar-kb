---
id: fc:abb-pvs-166-175-tl-us-e7
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E007
aliases:
- E007
- e7
- ABB / FIMER E007
- IGBT Sat
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E007
code_key: e7
display_message: IGBT Sat
vendor_severity: Error
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r3
    h: 573d7922b896
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r3
    h: 573d7922b896
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:igbt-saturation
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r3
    h: 573d7922b896
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r5
    h: 3b5ad120cf21
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: 09a57c6bd3e7
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r3
    h: 91ec03e02949
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r7
    h: a5ef159dc628
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r3
    h: 573d7922b896
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r5
    h: 3b5ad120cf21
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: 09a57c6bd3e7
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r3
    h: 91ec03e02949
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r7
    h: a5ef159dc628
  review: drafted
  review_note: 'support check: partial - The passages say the IGBT active devices of the inverter are
    in saturation, and the inverter bridge is not named.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r3
    h: 573d7922b896
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r5
    h: 3b5ad120cf21
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: 09a57c6bd3e7
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r3
    h: 91ec03e02949
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r7
    h: a5ef159dc628
  review: drafted
  review_note: 'support check: partial - The inverter attempts to resume normal operation, which implies
    an interruption, but a production stop is not stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Sporadic occurrences from grid or input transients self-clear; persistent recurrence needs service.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r3
    h: 573d7922b896
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r5
    h: 3b5ad120cf21
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: 09a57c6bd3e7
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r3
    h: 91ec03e02949
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r7
    h: a5ef159dc628
  review: drafted
---
