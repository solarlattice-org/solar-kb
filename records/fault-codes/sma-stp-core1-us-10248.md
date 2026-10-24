---
id: fc:sma-stp-core1-us-10248
type: FaultCode
name: SMA CORE1-US 10248
aliases:
- '10248'
- SMA 10248
- '[Interface]: network busy'
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10248'
code_key: '10248'
display_message: '[Interface]: network busy'
page: 57
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h294
    h: 383199b9accb
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h296
    h: c208e7ec47d6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:degraded-network-link
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h296
    h: c208e7ec47d6
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h455
    h: a9ea2cd45dc0
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h466
    h: a9ea2cd45dc0
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:network-load-reduction
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h297
    h: b3e08eb2b517
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h456
    h: b3e08eb2b517
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h467
    h: b3e08eb2b517
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h296
    h: c208e7ec47d6
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h455
    h: a9ea2cd45dc0
  review: drafted
  review_note: 'support check: partial - The passages describe a degraded condition and nothing stops,
    which is consistent with a warning, but the passages never state…'
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h294
    h: 383199b9accb
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h296
    h: c208e7ec47d6
  review: drafted
---
