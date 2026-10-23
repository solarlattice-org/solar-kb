---
id: fc:solis-rhi-1p-hv-us-ovgv0102030405
type: FaultCode
name: Solis RHI-1P-HV OV-G-V01/02/03/04/05
aliases:
- OV-G-V01/02/03/04/05
- ovgv0102030405
- Solis OV-G-V01/02/03/04/05
- Over grid voltage
category: Inverters
make: solis
make_name: Solis
model_family: rhi-1p-hv-us
family_name: Solis RHI-1P(5-10)K-HVES-5G-US
code: OV-G-V01/02/03/04/05
code_key: ovgv0102030405
display_message: Over grid voltage
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r3
    h: 5d5187c7ae2a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r3
    h: 5d5187c7ae2a
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r3
    h: 5d5187c7ae2a
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  note: Excessive AC cable resistance named as cause
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r3
    h: 5d5187c7ae2a
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r3
    h: 5d5187c7ae2a
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:cable-replacement
  note: Larger gauge grid cable
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r3
    h: 5d5187c7ae2a
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r3
    h: 5d5187c7ae2a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Protection limit change only if the utility permits
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r3
    h: 5d5187c7ae2a
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r3
    h: 5d5187c7ae2a
  review: drafted
---
