---
id: fc:sma-stp-core1-us-10282
type: FaultCode
name: SMA CORE1-US 10282
aliases:
- '10282'
- SMA 10282
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10282'
code_key: '10282'
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r4
    h: efae52ef907b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:invalid-access-code
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r4
    h: efae52ef907b
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h283
    h: 17ff9482ed5f
  review: drafted
  review_note: 'support check: partial - Login is blocked after incorrect login attempts, which fits an
    invalid access code, but the passages don''t name an invalid…'
- claim_id: c3
  rel: mitigated_by
  target: mit:enter-access-code
  note: Retry only after the lockout time has expired.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r4
    h: efae52ef907b
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h284
    h: 7cf37d41bd5c
  review: drafted
  review_note: 'support check: partial - Waiting for the lockout to expire and then retrying login is
    stated, but entering the correct access code is not.'
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r4
    h: efae52ef907b
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h283
    h: 17ff9482ed5f
  review: drafted
  review_note: 'support check: partial - It is a lockout notice that is not stated as a fault or warning,
    so informational is only implied.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Login lock lifts after a fixed time, 15 minutes for user and 12 hours for Grid Guard.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r4
    h: efae52ef907b
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h283
    h: 17ff9482ed5f
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r4
    h: efae52ef907b
  review: drafted
---
