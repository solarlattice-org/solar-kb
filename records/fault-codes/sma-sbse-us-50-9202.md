---
id: fc:sma-sbse-us-50-9202
type: FaultCode
name: SMA SBSE-US-50 9202
aliases:
- '9202'
- SMA 9202
- AC overvoltage in backup operation
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9202'
code_key: '9202'
display_message: AC overvoltage in backup operation
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.73
    h: 4f10eb927314
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h776
    h: a0cd72becf14
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:backup-ac-overvoltage
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h257
    h: 1166ed5f4cee
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h776
    h: a0cd72becf14
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:backup-power-outlet
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h257
    h: 1166ed5f4cee
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h258
    h: 70bd6c064910
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h258
    h: 70bd6c064910
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h778
    h: c87e8fc90a2c
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h777
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h778
    h: c87e8fc90a2c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.73
    h: 4f10eb927314
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h776
    h: a0cd72becf14
  review: drafted
---
