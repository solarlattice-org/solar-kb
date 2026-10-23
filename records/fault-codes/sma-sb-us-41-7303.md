---
id: fc:sma-sb-us-41-7303
type: FaultCode
name: SMA SB-US-41 7303
aliases:
- '7303'
- SMA 7303
- Update main CPU failed
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7303'
code_key: '7303'
display_message: Update main CPU failed
page: 63
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.41
    h: abe5a8660de6
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h342
    h: e75a5be9e1aa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r10
    h: 417f30a6fb06
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r3
    h: 2916d0bca0f3
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r4
    h: 24fe6af1e29f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h342
    h: e75a5be9e1aa
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h367
    h: e75a5be9e1aa
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r10
    h: 417f30a6fb06
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r3
    h: 2916d0bca0f3
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r4
    h: 24fe6af1e29f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h344
    h: 417f2f122215
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h369
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r10
    h: 417f30a6fb06
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r3
    h: 2916d0bca0f3
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r4
    h: 24fe6af1e29f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h343
    h: cca77e1e7cd3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h344
    h: 417f2f122215
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h368
    h: cca77e1e7cd3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h369
    h: 417f2f122215
  review: drafted
---
