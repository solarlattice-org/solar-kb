---
id: fc:solis-s6-eh1p-h-us-ovvbatt1
type: FaultCode
name: Solis S6-EH1P OV-Vbatt1
aliases:
- OV-Vbatt1
- ovvbatt1
- Solis OV-Vbatt1
- The detection of battery overvol tage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: OV-Vbatt1
code_key: ovvbatt1
display_message: The detection of battery overvol tage
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r10
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
---
