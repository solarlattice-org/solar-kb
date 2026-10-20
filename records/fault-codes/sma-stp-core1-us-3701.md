---
id: fc:sma-stp-core1-us-3701
type: FaultCode
name: SMA CORE1-US 3701
aliases:
- '3701'
- SMA 3701
- Residual current too high > Check PV array
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3701'
code_key: '3701'
display_message: Residual current too high > Check PV array
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r1
    h: a1fc2477c9ae
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r1
    h: a1fc2477c9ae
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  note: Residual current caused by brief grounding of the PV array.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r1
    h: a1fc2477c9ae
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r1
    h: a1fc2477c9ae
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r1
    h: a1fc2477c9ae
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r1
    h: a1fc2477c9ae
  review: drafted
---
