---
id: fc:solis-s6-eh3p-75-150k-us-12powerfault
type: FaultCode
name: Solis S6-EH3P75-150K 12Power-FAULT
aliases:
- 12Power-FAULT
- 12powerfault
- Solis 12Power-FAULT
- 12V undervoltage failure
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: 12Power-FAULT
code_key: 12powerfault
display_message: 12V undervoltage failure
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r7
    h: c2eeb05ceb1e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:auxiliary-supply-undervoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r8
    h: 75e8c1157edc
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r8
    h: c2eeb05ceb1e
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r7
    h: c2eeb05ceb1e
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:internal-power-supply-fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r4
    h: fefea5f24846
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r4
    h: fefea5f24846
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r4
    h: fefea5f24846
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r4
    h: fefea5f24846
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ground-conductor-check
  note: Also check wiring for leakage to ground.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r8
    h: 75e8c1157edc
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r8
    h: c2eeb05ceb1e
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r7
    h: c2eeb05ceb1e
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r4
    h: fefea5f24846
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11
    h: 76c7a1a42932
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact installer if persistent.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r4
    h: fefea5f24846
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r4
    h: fefea5f24846
  review: drafted
  review_note: 'support check: partial - Restart or contact installer is stated, but clearing by manual
    reset is only implied.'
---
