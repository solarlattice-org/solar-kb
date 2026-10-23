---
id: fc:solis-1p-4g-us-afcicheckfault
type: FaultCode
name: Solis 1P-4G-US AFCI Check FAULT
aliases:
- AFCI Check FAULT
- afcicheckfault
- Solis AFCI Check FAULT
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: AFCI Check FAULT
code_key: afcicheckfault
page: 63
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r2
    h: 86c0c0357b95
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r2
    h: 86c0c0357b95
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r2
    h: 86c0c0357b95
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r2
    h: 86c0c0357b95
  review: drafted
  review_note: 'support check: partial - The self-check fault of the AFCI module is stated, but a board
    failure is not explicitly stated.'
- claim_id: c5
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r2
    h: 86c0c0357b95
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r2
    h: 86c0c0357b95
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r2
    h: 86c0c0357b95
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r2
    h: 86c0c0357b95
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  review: drafted
  review_note: 'support check: partial - Replace inverter is listed as the last step, but the condition
    only if restart fails is implied by order, not stated.'
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15
    h: a3924957d8fb
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; escalate to installer or inverter replacement if persistent.
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=14.r1
    h: b7cb293629dc
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r2
    h: 86c0c0357b95
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r2
    h: 86c0c0357b95
  review: drafted
  review_note: 'support check: partial - Restart/reset is the stated solution, but ''manual reset'' clearing
    is implied; replace-inverter/installer escalation is stated, though clearing behavior isn''t explicit.'
---
