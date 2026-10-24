---
id: fc:abb-pvs-166-175-tl-us-e51
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E051
aliases:
- E051
- e51
- ABB / FIMER E051
- Safety mem. Fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E051
code_key: e51
display_message: Safety mem. Fault
vendor_severity: Error
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:memory-error
  note: Safety memory fault inside the inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r9
    h: c047ef4e4a9b
  review: drafted
  review_note: 'support check: partial - Safety memory fault is in the message, but passages only say
    error inside the inverter; memory error is by name only.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r9
    h: c047ef4e4a9b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r9
    h: c047ef4e4a9b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r9
    h: c047ef4e4a9b
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r9
    h: c047ef4e4a9b
  review: drafted
  review_note: 'support check: partial - Power cycle then contact assistance stated, but manual-reset
    clearing not explicit.'
- claim_id: c8
  rel: applies_to
  target: prod:abb-pvs-166-175-tl-us
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r8
    h: 0b9e31e8c689
  review: drafted
---
