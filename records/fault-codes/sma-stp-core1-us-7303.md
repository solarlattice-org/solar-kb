---
id: fc:sma-stp-core1-us-7303
type: FaultCode
name: SMA CORE1-US 7303
aliases:
- '7303'
- SMA 7303
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7303'
code_key: '7303'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r10
    h: 417f30a6fb06
  review: drafted
- claim_id: c4
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
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
- claim_id: c6
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
