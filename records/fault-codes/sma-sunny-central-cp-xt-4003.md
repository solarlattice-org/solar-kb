---
id: fc:sma-sunny-central-cp-xt-4003
type: FaultCode
name: SMA SC-CP-XT 4003
aliases:
- '4003'
- SMA 4003
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '4003'
code_key: '4003'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
  review_note: 'support check: partial - Polarity reversal is detected and polarity is checked, but no
    polarity measurement method is stated.'
- claim_id: c7
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r13
    h: ef0054071769
  review: drafted
---
