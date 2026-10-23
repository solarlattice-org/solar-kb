---
id: fc:solis-s6-eh3p-75-150k-us-dcintf
type: FaultCode
name: Solis S6-EH3P75-150K DC-INTF
aliases:
- DC-INTF
- dcintf
- Solis DC-INTF
- DC hardware overcurrent (1, 2, 3, 4)
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: DC-INTF
code_key: dcintf
display_message: DC hardware overcurrent (1, 2, 3, 4)
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r12
    h: 4959393243cf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r15
    h: eae16f7d5f0f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r12
    h: b0a286d4f4c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r12
    h: 4959393243cf
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r12
    h: 4959393243cf
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r12
    h: b0a286d4f4c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r12
    h: 4959393243cf
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r12
    h: 4959393243cf
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:power-board
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r15
    h: eae16f7d5f0f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r5
    h: 32765dbfaba4
  review: drafted
  review_note: 'support check: partial - Changing the power board is a listed solution, implying involvement,
    but it is not stated as the affected component.'
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r12
    h: b0a286d4f4c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r12
    h: 4959393243cf
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r12
    h: 4959393243cf
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r15
    h: eae16f7d5f0f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r5
    h: 32765dbfaba4
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r15
    h: eae16f7d5f0f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r5
    h: 32765dbfaba4
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r15
    h: eae16f7d5f0f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r5
    h: 32765dbfaba4
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r2
    h: a97b8efd906c
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; if persisting, isolate faulty MPPT string, then power board or inverter replacement.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r2
    h: a97b8efd906c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r15
    h: eae16f7d5f0f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r5
    h: 32765dbfaba4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r5
    h: 32765dbfaba4
  review: drafted
  review_note: 'support check: partial - Restart then isolate string then replacement sequence is stated,
    but nothing says the fault clears by manual reset.'
---
