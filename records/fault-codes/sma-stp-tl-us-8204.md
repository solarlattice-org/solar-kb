---
id: fc:sma-stp-tl-us-8204
type: FaultCode
name: SMA STP-TL-US 8204
aliases:
- '8204'
- SMA 8204
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '8204'
code_key: '8204'
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r6
    h: cbef91964667
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r6
    h: cbef91964667
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r6
    h: cbef91964667
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r6
    h: cbef91964667
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r6
    h: cbef91964667
  review: drafted
---
