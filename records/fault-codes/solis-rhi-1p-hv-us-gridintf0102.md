---
id: fc:solis-rhi-1p-hv-us-gridintf0102
type: FaultCode
name: Solis RHI-1P-HV GRID-INTF01/02
aliases:
- GRID-INTF01/02
- gridintf0102
- Solis GRID-INTF01/02
- Grid interference
category: Inverters
make: solis
make_name: Solis
model_family: rhi-1p-hv-us
family_name: Solis RHI-1P(5-10)K-HVES-5G-US
code: GRID-INTF01/02
code_key: gridintf0102
display_message: Grid interference
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-instability
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r12
    h: 02f61ff2da17
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r7
    h: 08b308fe3d39
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:power-board
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r12
    h: 02f61ff2da17
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r7
    h: 08b308fe3d39
  review: drafted
  review_note: 'support check: partial - Change power board is a solution, but the board being affected
    is only implied.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r12
    h: 02f61ff2da17
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r7
    h: 08b308fe3d39
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: mitigated_by
  target: mit:power-board-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r12
    h: 02f61ff2da17
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r7
    h: 08b308fe3d39
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; power board replacement if persistent.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r12
    h: 02f61ff2da17
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r7
    h: 08b308fe3d39
  review: drafted
  review_note: 'support check: partial - Restart is the first step, but the passages do not say it clears
    by manual reset.'
---
