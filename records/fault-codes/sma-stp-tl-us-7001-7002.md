---
id: fc:sma-stp-tl-us-7001-7002
type: FaultCode
name: SMA STP-TL-US 7001-7002
aliases:
- 7001-7002
- SMA 7001-7002
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 7001-7002
code_key: 7001-7002
code_from: 7001
code_to: 7002
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r4
    h: fe071172ce08
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:measurement-signal-error
  note: Sensor fault with fan running permanently.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r4
    h: fe071172ce08
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r4
    h: fe071172ce08
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r4
    h: fe071172ce08
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r4
    h: fe071172ce08
  review: drafted
---
