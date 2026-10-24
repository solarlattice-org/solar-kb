---
id: fc:solis-rhi-1p-hv-us-overload
type: FaultCode
name: Solis RHI-1P-HV Over-Load
aliases:
- Over-Load
- overload
- Solis Over-Load
- Backup overload fault
category: Inverters
make: solis
make_name: Solis
model_family: rhi-1p-hv-us
family_name: Solis RHI-1P(5-10)K-HVES-5G-US
code: Over-Load
code_key: overload
display_message: Backup overload fault
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r12
    h: 18c3ae415823
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overload
  note: Overload on backup port
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r19
    h: 47dc4f15dbe3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r19
    h: 47dc4f15dbe3
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r19
    h: 47dc4f15dbe3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:backup-power-outlet
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r19
    h: 47dc4f15dbe3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r19
    h: 47dc4f15dbe3
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r19
    h: 47dc4f15dbe3
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:backup-load-reduction
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r19
    h: 47dc4f15dbe3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r19
    h: 47dc4f15dbe3
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r19
    h: 47dc4f15dbe3
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after reducing backup load
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r12
    h: 18c3ae415823
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r12
    h: 18c3ae415823
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: applies_to
  target: prod:solis-rhi-1p-hv-us
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r12
    h: 18c3ae415823
  review: drafted
---
