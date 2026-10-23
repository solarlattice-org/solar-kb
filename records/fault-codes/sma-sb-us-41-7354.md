---
id: fc:sma-sb-us-41-7354
type: FaultCode
name: SMA SB-US-41 7354
aliases:
- '7354'
- SMA 7354
- Update of time zone database not successful
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7354'
code_key: '7354'
display_message: Update of time zone database not successful
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.53
    h: 26c4d26384ea
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h385
    h: 99bad10e128f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:timezone-database-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r6
    h: 3313c7d0fe28
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h229
    h: e8812949e30a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h386
    h: 07aa9e611a14
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:retry-update
  note: First step; contact service if message recurs.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r6
    h: 3313c7d0fe28
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h230
    h: b963762ed902
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h387
    h: 2b6216ee121d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the message appears again after retrying.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h230
    h: b963762ed902
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h387
    h: 2b6216ee121d
  review: drafted
---
