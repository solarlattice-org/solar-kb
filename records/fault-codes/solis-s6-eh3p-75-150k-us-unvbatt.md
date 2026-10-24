---
id: fc:solis-s6-eh3p-75-150k-us-unvbatt
type: FaultCode
name: Solis S6-EH3P75-150K UN-Vbatt
aliases:
- UN-Vbatt
- unvbatt
- Solis UN-Vbatt
- Battery undervoltage detected
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: UN-Vbatt
code_key: unvbatt
display_message: Battery undervoltage detected
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r4
    h: 62500ce97876
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-voltage-out-of-range
  note: Sources disagree on under- versus overvoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r4
    h: f2a7150b5a13
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r4
    h: b6ca222b5413
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r4
    h: 62500ce97876
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact manufacturer service if it persists
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r4
    h: f2a7150b5a13
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r4
    h: b6ca222b5413
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r4
    h: 62500ce97876
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:solis-s6-eh3p-75-150k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r4
    h: 62500ce97876
  review: drafted
---
