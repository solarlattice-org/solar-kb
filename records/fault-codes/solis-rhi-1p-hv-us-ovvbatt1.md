---
id: fc:solis-rhi-1p-hv-us-ovvbatt1
type: FaultCode
name: Solis RHI-1P-HV OV-Vbatt1
aliases:
- OV-Vbatt1
- ovvbatt1
- Solis OV-Vbatt1
- The detection of battery overvol tage
category: Inverters
make: solis
make_name: Solis
model_family: rhi-1p-hv-us
family_name: Solis RHI-1P(5-10)K-HVES-5G-US
code: OV-Vbatt1
code_key: ovvbatt1
display_message: The detection of battery overvol tage
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r10
    h: aca9c87b0e6b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r10
    h: aca9c87b0e6b
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r10
    h: aca9c87b0e6b
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Overvoltage protection point setting
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r10
    h: aca9c87b0e6b
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r10
    h: aca9c87b0e6b
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after verifying the protection setting
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r10
    h: aca9c87b0e6b
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r10
    h: aca9c87b0e6b
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:solis-rhi-1p-hv-us
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r10
    h: aca9c87b0e6b
  review: drafted
---
