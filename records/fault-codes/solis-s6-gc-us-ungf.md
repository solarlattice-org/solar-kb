---
id: fc:solis-s6-gc-us-ungf
type: FaultCode
name: Solis S6-GC UN-G-F
aliases:
- UN-G-F
- ungf
- Solis UN-G-F
- Grid under frequency
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: UN-G-F
code_key: ungf
display_message: Grid under frequency
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r5
    h: 176f8102cb5a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r5
    h: 176f8102cb5a
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r3
    h: 078019ba3a53
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r3
    h: 078019ba3a53
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r5
    h: 176f8102cb5a
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r3
    h: 078019ba3a53
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: Lower frequency limit adjusted only with utility permission.
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r3
    h: 078019ba3a53
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r5
    h: 176f8102cb5a
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:solis-s6-gc-us
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r5
    h: 176f8102cb5a
  review: drafted
---
