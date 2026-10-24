---
id: fc:sma-sbse-us-50-4017
type: FaultCode
name: SMA SBSE-US-50 4017
aliases:
- '4017'
- SMA 4017
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '4017'
code_key: '4017'
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h606
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h607
    h: f7ffbc5bca19
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h606
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h607
    h: f7ffbc5bca19
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h607
    h: f7ffbc5bca19
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h608
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h608
    h: 9a1cdbbee0a1
  review: drafted
  review_note: 'support check: partial - Polarity check is a corrective measure, not explicitly a detection
    method.'
- claim_id: c7
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare voltages across DC inputs when irradiation is sufficient.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h608
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h608
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h608
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.38
    h: ded08969f3d6
  review: drafted
---
