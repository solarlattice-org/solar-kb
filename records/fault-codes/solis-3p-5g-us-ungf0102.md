---
id: fc:solis-3p-5g-us-ungf0102
type: FaultCode
name: Solis 3P-5G-US UN-G-F01/02
aliases:
- UN-G-F01/02
- ungf0102
- Solis UN-G-F01/02
- Under grid frequency
category: Inverters
make: solis
make_name: Solis
model_family: 3p-5g-us
family_name: Solis-3P(125-255)K-EHV-5G-US
code: UN-G-F01/02
code_key: ungf0102
display_message: Under grid frequency
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r6
    h: 014bb367b27e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r6
    h: 014bb367b27e
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r2
    h: 89cadd6cacbe
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r2
    h: 89cadd6cacbe
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Protection limit change only if utility permits.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r6
    h: 014bb367b27e
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r2
    h: 89cadd6cacbe
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r2
    h: 89cadd6cacbe
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r2
    h: 89cadd6cacbe
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11
    h: 76c7a1a42932
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:solis-3p-5g-us
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r6
    h: 014bb367b27e
  review: drafted
---
