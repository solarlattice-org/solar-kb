---
id: fc:sma-stp-tl-us-101-103
type: FaultCode
name: SMA STP-TL-US 101-103
aliases:
- 101-103
- SMA 101-103
- Grid fault
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 101-103
code_key: 101-103
code_from: 101
code_to: 103
display_message: Grid fault
page: 45
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  review: drafted
  review_note: 'support check: partial - Passage says grid voltage or impedance is too high; overvoltage
    is covered, but not exclusively.'
- claim_id: c3
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  review: drafted
  review_note: 'support check: partial - Grid voltage or grid impedance too high; impedance is one alternative
    cause.'
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h178
    h: a5022aba0189
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When grid voltage is out of range due to local grid conditions; otherwise contact service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h177
    h: 36c1f790b083
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h178
    h: a5022aba0189
  review: drafted
---
