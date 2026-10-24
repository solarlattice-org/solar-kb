---
id: fc:abb-pvs-60-tl-us-e55
type: FaultCode
name: ABB / FIMER PVS-60-TL E055
aliases:
- E055
- e55
- ABB / FIMER E055
- AFDD wrong conf.
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E055
code_key: e55
display_message: AFDD wrong conf.
vendor_severity: Error
page: 158
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Arc detection board parameters could not be read
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r2
    h: 4252e93c15c9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r1
    h: 10a581c99b06
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r1
    h: 10a581c99b06
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r7
    h: a0d28dc7dba6
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r2
    h: 4252e93c15c9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r1
    h: 10a581c99b06
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r1
    h: 10a581c99b06
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r7
    h: a0d28dc7dba6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r2
    h: 4252e93c15c9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r1
    h: 10a581c99b06
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r1
    h: 10a581c99b06
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r7
    h: a0d28dc7dba6
  review: drafted
  review_note: 'support check: partial - Restart is implied as a first step, but the passages don''t say
    it mitigates the fault.'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r2
    h: 4252e93c15c9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r1
    h: 10a581c99b06
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r1
    h: 10a581c99b06
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r7
    h: a0d28dc7dba6
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r2
    h: 4252e93c15c9
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r1
    h: 10a581c99b06
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r1
    h: 10a581c99b06
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r7
    h: a0d28dc7dba6
  review: drafted
  review_note: 'support check: partial - The power-cycle-then-service sequence is stated, but the passages
    don''t say the fault clears by manual reset.'
- claim_id: c8
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r12
    h: bc120a2dff37
  review: drafted
---
