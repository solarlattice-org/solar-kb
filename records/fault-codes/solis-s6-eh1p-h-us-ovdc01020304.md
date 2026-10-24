---
id: fc:solis-s6-eh1p-h-us-ovdc01020304
type: FaultCode
name: Solis S6-EH1P OV-DC01/02/03/04
aliases:
- OV-DC01/02/03/04
- ovdc01020304
- Solis OV-DC01/02/03/04
- Over DC voltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: OV-DC01/02/03/04
code_key: ovdc01020304
display_message: Over DC voltage
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r1
    h: 91947f55308b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r9
    h: 1f836cab2884
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r1
    h: 91947f55308b
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r9
    h: 1f836cab2884
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r1
    h: 91947f55308b
  review: drafted
  review_note: 'support check: partial - Reducing modules in series implies the PV array, but the array
    is not named as affected.'
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Fewer modules in series.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r9
    h: 1f836cab2884
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r1
    h: 91947f55308b
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:solis-s6-eh1p-h-us
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r1
    h: 91947f55308b
  review: drafted
---
