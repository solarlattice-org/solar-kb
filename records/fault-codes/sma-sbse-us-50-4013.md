---
id: fc:sma-sbse-us-50-4013
type: FaultCode
name: SMA SBSE-US-50 4013
aliases:
- '4013'
- SMA 4013
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '4013'
code_key: '4013'
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.34
    h: 6616f1442853
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.34
    h: 6616f1442853
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h586
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h587
    h: f7ffbc5bca19
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.34
    h: 6616f1442853
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h586
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h587
    h: f7ffbc5bca19
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h586
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h588
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h588
    h: 9a1cdbbee0a1
  review: drafted
  review_note: 'support check: partial - Passages say to check PV module polarity, but don''t state detection
    by a polarity measurement.'
- claim_id: c6
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare input voltages when irradiation is sufficient.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h588
    h: 9a1cdbbee0a1
  review: drafted
  review_note: 'support check: partial - Passages say to check for the same voltage at the DC inputs when
    irradiation is sufficient, but don''t state it…'
- claim_id: c7
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h588
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h588
    h: 9a1cdbbee0a1
  review: drafted
---
