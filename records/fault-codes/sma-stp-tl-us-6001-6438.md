---
id: fc:sma-stp-tl-us-6001-6438
type: FaultCode
name: SMA STP-TL-US 6001-6438
aliases:
- 6001-6438
- SMA 6001-6438
- Self diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 6001-6438
code_key: 6001-6438
code_from: 6001
code_to: 6438
display_message: Self diagnosis > Interference device
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r4
    h: e298415e4957
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r4
    h: e298415e4957
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r4
    h: e298415e4957
  review: drafted
  review_note: 'support check: partial - It is a device interference needing Service, but the inverter
    is not explicitly named as the affected component.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r4
    h: e298415e4957
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r4
    h: e298415e4957
  review: drafted
---
