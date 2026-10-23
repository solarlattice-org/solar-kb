---
id: fc:solis-3p-5g-us-gimp
type: FaultCode
name: Solis 3P-5G-US G-IMP
aliases:
- G-IMP
- gimp
- Solis G-IMP
- High grid impedance
category: Inverters
make: solis
make_name: Solis
model_family: 3p-5g-us
family_name: Solis-3P(125-255)K-EHV-5G-US
code: G-IMP
code_key: gimp
display_message: High grid impedance
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r7
    h: a71ef8fdaeaf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r7
    h: a71ef8fdaeaf
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r6
    h: 25613ca69b72
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r6
    h: 25613ca69b72
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Protection limit change only if utility permits.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r7
    h: a71ef8fdaeaf
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r6
    h: 25613ca69b72
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r6
    h: 25613ca69b72
  review: drafted
---
