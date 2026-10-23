---
id: fc:sma-sb-us-41-7352
type: FaultCode
name: SMA SB-US-41 7352
aliases:
- '7352'
- SMA 7352
- Update of Wi-Fi not successful
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7352'
code_key: '7352'
display_message: Update of Wi-Fi not successful
page: 65
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.51
    h: afc5eddef20e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h378
    h: 538ff39d54b5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r4
    h: 622dc8a01f0e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h225
    h: 1a36338616cc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h379
    h: 07d07e0090ed
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:wifi-module
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r4
    h: 622dc8a01f0e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h225
    h: 1a36338616cc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h379
    h: 07d07e0090ed
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:retry-update
  note: First step; contact service if message recurs.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r4
    h: 622dc8a01f0e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h226
    h: b963762ed902
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h380
    h: 2b6216ee121d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the message appears again after retrying.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r4
    h: 622dc8a01f0e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h226
    h: b963762ed902
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h380
    h: 2b6216ee121d
  review: drafted
---
