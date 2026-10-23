---
id: fc:solis-s6-eh3p-75-150k-us-ovgi
type: FaultCode
name: Solis S6-EH3P75-150K OV-G-I
aliases:
- OV-G-I
- ovgi
- Solis OV-G-I
- A phase RMS value overcurrent
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: OV-G-I
code_key: ovgi
display_message: A phase RMS value overcurrent
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r13
    h: 850505372fc6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r13
    h: da3a0c0f5b8d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r4
    h: 6fb54cddc4d9
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r13
    h: e1de121d91c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r13
    h: 850505372fc6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r13
    h: 850505372fc6
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:power-board
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r13
    h: da3a0c0f5b8d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r4
    h: 6fb54cddc4d9
  review: drafted
  review_note: 'support check: partial - Change power board is a listed solution, implying involvement,
    but it is not explicitly stated as the affected component.'
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r13
    h: e1de121d91c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r13
    h: 850505372fc6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r13
    h: 850505372fc6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r13
    h: e1de121d91c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r13
    h: 850505372fc6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r13
    h: 850505372fc6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r13
    h: da3a0c0f5b8d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r4
    h: 6fb54cddc4d9
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r13
    h: e1de121d91c4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r13
    h: 850505372fc6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r13
    h: 850505372fc6
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r13
    h: da3a0c0f5b8d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r4
    h: 6fb54cddc4d9
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; power board replacement if the fault persists.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r13
    h: da3a0c0f5b8d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r4
    h: 6fb54cddc4d9
  review: drafted
  review_note: 'support check: partial - Restart then power board replacement is stated, but clearing
    by manual reset is not stated explicitly.'
---
