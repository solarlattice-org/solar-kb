---
id: fc:sma-sbse-us-50-302
type: FaultCode
name: SMA SBSE-US-50 302
aliases:
- '302'
- SMA 302
- Active power limited AC voltage
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '302'
code_key: '302'
display_message: Active power limited AC voltage
page: 100
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.9
    h: 35fd9fa6070a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h463
    h: 3f3acb3f07c6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.9
    h: 35fd9fa6070a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h463
    h: 3f3acb3f07c6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h464
    h: b0237c7a42a9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.6
    h: cc50f23d4539
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h397
    h: 3f3acb3f07c6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h398
    h: b0237c7a42a9
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.9
    h: 35fd9fa6070a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h464
    h: b0237c7a42a9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.6
    h: cc50f23d4539
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h398
    h: b0237c7a42a9
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h465
    h: 72931e15dadd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h399
    h: 72931e15dadd
  review: drafted
  review_note: 'support check: partial - Passages advise checking the grid voltage, but don''t state the
    event is detected by grid voltage measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: Only when fluctuations and the message occur frequently.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h465
    h: 72931e15dadd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h399
    h: 72931e15dadd
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only after grid operator approval, coordinated with manufacturer service.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h465
    h: 72931e15dadd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h399
    h: 72931e15dadd
  review: drafted
---
