---
id: fc:sma-stp-core1-us-10250
type: FaultCode
name: SMA CORE1-US 10250
aliases:
- '10250'
- SMA 10250
- '[Interface]: package error rate [ok / high]'
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10250'
code_key: '10250'
display_message: '[Interface]: package error rate [ok / high]'
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h299
    h: b43a65db97ed
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h300
    h: a1c2873a3c05
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h216
    h: b43a65db97ed
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h217
    h: a1c2873a3c05
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h301
    h: b43a65db97ed
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h302
    h: a1c2873a3c05
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:high-packet-error-rate
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h217
    h: a1c2873a3c05
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h463
    h: 71b063208a30
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h476
    h: 71b063208a30
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h301
    h: 3b567be3082c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h303
    h: 3b567be3082c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h464
    h: 2fd95b7595c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h477
    h: 2fd95b7595c5
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h301
    h: 3b567be3082c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h303
    h: 3b567be3082c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h464
    h: 2fd95b7595c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h477
    h: 2fd95b7595c5
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:network-load-reduction
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h301
    h: 3b567be3082c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h303
    h: 3b567be3082c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h464
    h: 2fd95b7595c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h477
    h: 2fd95b7595c5
  review: drafted
---
