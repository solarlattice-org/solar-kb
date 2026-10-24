---
id: fc:sma-stp-x-us-50-6602
type: FaultCode
name: SMA STP-X-US 6602
aliases:
- '6602'
- SMA 6602
- Overvoltage grid (SW)
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6602'
code_key: '6602'
display_message: Overvoltage grid (SW)
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.38
    h: 547f96f2e784
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h553
    h: 4bfe97e73d18
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.46
    h: 9078a10332a0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h644
    h: 4bfe97e73d18
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h645
    h: 0afd72265d0b
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.46
    h: 9078a10332a0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h646
    h: b9ec9a9f9f23
  review: drafted
  review_note: 'support check: partial - Check the grid voltage is stated as a measure, but not explicitly
    a detection method.'
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.46
    h: 9078a10332a0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h646
    h: b9ec9a9f9f23
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When local grid conditions keep voltage outside the permitted range.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.46
    h: 9078a10332a0
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h646
    h: b9ec9a9f9f23
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.38
    h: 547f96f2e784
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h553
    h: 4bfe97e73d18
  review: drafted
---
