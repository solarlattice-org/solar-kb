---
id: fc:sma-sb-us-40-7333
type: FaultCode
name: SMA SB-US-40 7333
aliases:
- '7333'
- SMA 7333
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '7333'
code_key: '7333'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r7
    h: 0586c6c20a84
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h264
    h: e4a2a2e70403
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h266
    h: d9a67825634f
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r7
    h: 0586c6c20a84
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h357
    h: 041fe17e3041
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h381
    h: 041fe17e3041
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:retry-update
  note: First step; improve connection quality if via Wi-Fi, then contact service if repeated
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h264
    h: e4a2a2e70403
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h267
    h: ea62f32c68cd
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r7
    h: 0586c6c20a84
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h358
    h: 6992dd0dc9f8
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h382
    h: 6992dd0dc9f8
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:network-connection-check
  note: When connected via Wi-Fi with poor link quality
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h264
    h: e4a2a2e70403
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h267
    h: ea62f32c68cd
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r7
    h: 0586c6c20a84
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h358
    h: 6992dd0dc9f8
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h382
    h: 6992dd0dc9f8
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the message is displayed again
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h264
    h: e4a2a2e70403
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h267
    h: ea62f32c68cd
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r7
    h: 0586c6c20a84
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h358
    h: 6992dd0dc9f8
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h382
    h: 6992dd0dc9f8
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sb-us-40
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r7
    h: 0586c6c20a84
  review: drafted
---
