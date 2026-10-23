---
id: fc:solis-s6-gc-us-ovgf
type: FaultCode
name: Solis S6-GC OV-G-F
aliases:
- OV-G-F
- ovgf
- Solis OV-G-F
- Over Grid Frequency
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: OV-G-F
code_key: ovgf
display_message: Over Grid Frequency
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=13.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=12.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=11.r1
    h: 88ec1865ce8c
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r2
    h: 7a54860ecda0
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=11.r1
    h: 88ec1865ce8c
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r2
    h: 7a54860ecda0
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Upper frequency limit change only with utility approval.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=11.r1
    h: 88ec1865ce8c
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r2
    h: 7a54860ecda0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=11.r1
    h: 88ec1865ce8c
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r2
    h: 7a54860ecda0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=11.r1
    h: 88ec1865ce8c
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r2
    h: 7a54860ecda0
  review: drafted
---
