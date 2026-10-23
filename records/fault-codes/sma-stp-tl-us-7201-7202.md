---
id: fc:sma-stp-tl-us-7201-7202
type: FaultCode
name: SMA STP-TL-US 7201-7202
aliases:
- 7201-7202
- SMA 7201-7202
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 7201-7202
code_key: 7201-7202
code_from: 7201
code_to: 7202
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r3
    h: f277066369bf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:data-storage-failure
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r3
    h: f277066369bf
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r3
    h: f277066369bf
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r3
    h: f277066369bf
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r3
    h: f277066369bf
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r3
    h: f277066369bf
  review: drafted
---
