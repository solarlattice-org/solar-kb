---
id: fc:sma-stp-tl-us-8101-8104
type: FaultCode
name: SMA STP-TL-US 8101-8104
aliases:
- 8101-8104
- SMA 8101-8104
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 8101-8104
code_key: 8101-8104
code_from: 8101
code_to: 8104
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r5
    h: 1c48e4b89fc2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  note: Communication disturbed
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r5
    h: 1c48e4b89fc2
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r5
    h: 1c48e4b89fc2
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r5
    h: 1c48e4b89fc2
  review: drafted
---
