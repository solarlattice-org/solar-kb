---
id: fc:sma-sbse-us-50-4015
type: FaultCode
name: SMA SBSE-US-50 4015
aliases:
- '4015'
- SMA 4015
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '4015'
code_key: '4015'
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.36
    h: b2416fc8d9ba
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.36
    h: b2416fc8d9ba
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h596
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h597
    h: f7ffbc5bca19
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.36
    h: b2416fc8d9ba
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h596
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h597
    h: f7ffbc5bca19
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h596
    h: 13dcd5c17caa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h598
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare input voltages when irradiation is sufficient.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h598
    h: 9a1cdbbee0a1
  review: drafted
  review_note: 'support check: partial - Passage says check whether same voltage is present at DC inputs
    if irradiation sufficient, but doesn''t link it to event…'
- claim_id: c6
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h598
    h: 9a1cdbbee0a1
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h598
    h: 9a1cdbbee0a1
  review: drafted
---
