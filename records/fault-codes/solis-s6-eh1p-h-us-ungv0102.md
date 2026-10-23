---
id: fc:solis-s6-eh1p-h-us-ungv0102
type: FaultCode
name: Solis S6-EH1P UN-G-V01/02
aliases:
- UN-G-V01/02
- ungv0102
- Solis UN-G-V01/02
- Under grid voltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: UN-G-V01/02
code_key: ungv0102
display_message: Under grid voltage
page: 74
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r3
    h: 0218c07cb39e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r4
    h: d7395e354cea
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r3
    h: 0218c07cb39e
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r3
    h: 0218c07cb39e
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Protection limit change only if utility permits.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r4
    h: d7395e354cea
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r3
    h: 0218c07cb39e
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r3
    h: 0218c07cb39e
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r3
    h: 0218c07cb39e
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11
    h: 76c7a1a42932
  review: drafted
---
