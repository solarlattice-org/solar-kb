---
id: fc:sma-stp-tl-us-6603-6604
type: FaultCode
name: SMA STP-TL-US 6603-6604
aliases:
- 6603-6604
- SMA 6603-6604
- Self-diagnosis > Overload
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 6603-6604
code_key: 6603-6604
code_from: 6603
code_to: 6604
display_message: Self-diagnosis > Overload
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r7
    h: 970d7aaecf47
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overload
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r7
    h: 970d7aaecf47
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r7
    h: 970d7aaecf47
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r7
    h: 970d7aaecf47
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r7
    h: 970d7aaecf47
  review: drafted
---
