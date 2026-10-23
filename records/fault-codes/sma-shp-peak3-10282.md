---
id: fc:sma-shp-peak3-10282
type: FaultCode
name: SMA PEAK3-US 10282
aliases:
- '10282'
- SMA 10282
- '|tn0|-Login via |tn4| locked'
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '10282'
code_key: '10282'
display_message: '|tn0|-Login via |tn4| locked'
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.45
    h: 50e42b1eabd9
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h495
    h: f3a11156bb99
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
---
