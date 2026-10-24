---
id: fc:sma-sbse-us-50-4014
type: FaultCode
name: SMA SBSE-US-50 4014
aliases:
- '4014'
- SMA 4014
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '4014'
code_key: '4014'
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.35
    h: 126e4fb489f7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.35
    h: 126e4fb489f7
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h591
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h592
    h: f7ffbc5bca19
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.35
    h: 126e4fb489f7
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h591
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h592
    h: f7ffbc5bca19
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h591
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h593
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h593
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
    loc: sec=h593
    h: 9a1cdbbee0a1
  review: drafted
  review_note: 'support check: partial - Passages say to check for the same voltage at the DC inputs when
    irradiation is sufficient, but don''t state it…'
- claim_id: c7
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h593
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h593
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.35
    h: 126e4fb489f7
  review: drafted
---
