---
id: fc:solis-3p-5g-us-ovgf0102
type: FaultCode
name: Solis 3P-5G-US OV-G-F01/02
aliases:
- OV-G-F01/02
- ovgf0102
- Solis OV-G-F01/02
- Over grid frequency
category: Inverters
make: solis
make_name: Solis
model_family: 3p-5g-us
family_name: Solis-3P(125-255)K-EHV-5G-US
code: OV-G-F01/02
code_key: ovgf0102
display_message: Over grid frequency
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r5
    h: 1ac98be7c247
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r5
    h: 1ac98be7c247
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r5
    h: 32736be48f58
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Protection limit change only if utility permits.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r5
    h: 1ac98be7c247
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r5
    h: 32736be48f58
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:solis-3p-5g-us
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r5
    h: 1ac98be7c247
  review: drafted
---
