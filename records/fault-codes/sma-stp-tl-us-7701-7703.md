---
id: fc:sma-stp-tl-us-7701-7703
type: FaultCode
name: SMA STP-TL-US 7701-7703
aliases:
- 7701-7703
- SMA 7701-7703
- Self diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 7701-7703
code_key: 7701-7703
code_from: 7701
code_to: 7703
display_message: Self diagnosis > Interference device
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r3
    h: cdef76a3a08e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r3
    h: cdef76a3a08e
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r3
    h: cdef76a3a08e
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r3
    h: cdef76a3a08e
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r3
    h: cdef76a3a08e
  review: drafted
---
