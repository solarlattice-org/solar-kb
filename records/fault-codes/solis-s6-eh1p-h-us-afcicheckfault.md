---
id: fc:solis-s6-eh1p-h-us-afcicheckfault
type: FaultCode
name: Solis S6-EH1P AFCI Check FAULT
aliases:
- AFCI Check FAULT
- afcicheckfault
- Solis AFCI Check FAULT
- AFCI module self check fault
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: AFCI Check FAULT
code_key: afcicheckfault
display_message: AFCI module self check fault
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r2
    h: 86c0c0357b95
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
  review_note: 'review: partial - Replace inverter appears as the last solution step in tbl=15.r1/14.r1,
    but no cited passage states the condition that it applies only when…'
- claim_id: c7
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
- claim_id: c8
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
