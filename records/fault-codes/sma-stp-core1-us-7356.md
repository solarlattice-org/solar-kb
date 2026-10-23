---
id: fc:sma-stp-core1-us-7356
type: FaultCode
name: SMA CORE1-US 7356
aliases:
- '7356'
- SMA 7356
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7356'
code_key: '7356'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r8
    h: fe3078fdd1c1
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r8
    h: fe3078fdd1c1
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r8
    h: fe3078fdd1c1
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:firmware-update-failure
  note: Update of the inverter web user interface failed.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r8
    h: fe3078fdd1c1
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r8
    h: fe3078fdd1c1
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r8
    h: fe3078fdd1c1
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h232
    h: 6a64d12415ca
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h393
    h: c10b2c8c64ac
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:retry-update
  note: Retry first; contact service if the message recurs.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r8
    h: fe3078fdd1c1
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r8
    h: fe3078fdd1c1
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r8
    h: fe3078fdd1c1
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h233
    h: b963762ed902
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h394
    h: 2b6216ee121d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the message reappears after a retry.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r8
    h: fe3078fdd1c1
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r8
    h: fe3078fdd1c1
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r8
    h: fe3078fdd1c1
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h233
    h: b963762ed902
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h394
    h: 2b6216ee121d
  review: drafted
---
