---
id: fc:solis-3p-5g-us-ovgv01020304
type: FaultCode
name: Solis 3P-5G-US OV-G-V01/02/03/04
aliases:
- OV-G-V01/02/03/04
- ovgv01020304
- Solis OV-G-V01/02/03/04
- Over grid voltage
category: Inverters
make: solis
make_name: Solis
model_family: 3p-5g-us
family_name: Solis-3P(125-255)K-EHV-5G-US
code: OV-G-V01/02/03/04
code_key: ovgv01020304
display_message: Over grid voltage
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r3
    h: c90cbb857d2d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r3
    h: c90cbb857d2d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  note: High AC cable resistance named as cause.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r3
    h: c90cbb857d2d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:cable-replacement
  note: Larger cross-section grid cable.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r3
    h: c90cbb857d2d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Protection limit change only if utility permits.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r3
    h: c90cbb857d2d
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:solis-3p-5g-us
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r3
    h: c90cbb857d2d
  review: drafted
---
