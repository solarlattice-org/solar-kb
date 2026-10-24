---
id: fc:solis-s6-eh1p-h-us-ovvbatth
type: FaultCode
name: Solis S6-EH1P OV-Vbatt-H
aliases:
- OV-Vbatt-H
- ovvbatth
- Solis OV-Vbatt-H
- Battery overvoltage hardware fault
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: OV-Vbatt-H
code_key: ovvbatth
display_message: Battery overvoltage hardware fault
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r11
    h: 686e06868ba3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r11
    h: 686e06868ba3
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r11
    h: 686e06868ba3
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:battery-connection-check
  note: Battery fuses and breaker tripped state
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r11
    h: 686e06868ba3
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r11
    h: 686e06868ba3
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after checking battery circuit
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r11
    h: 686e06868ba3
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r11
    h: 686e06868ba3
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:solis-s6-eh1p-h-us
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r11
    h: 686e06868ba3
  review: drafted
---
