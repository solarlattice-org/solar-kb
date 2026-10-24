---
id: fc:sma-stp-core1-us-10253
type: FaultCode
name: SMA CORE1-US 10253
aliases:
- '10253'
- SMA 10253
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10253'
code_key: '10253'
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:degraded-network-link
  note: Applies when the speed drops to 10 Mbit.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h276
    h: f59bf0d5be4c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h474
    h: 325c332151ed
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h277
    h: ddb00c73f56a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h475
    h: 3e364e48e1a4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h277
    h: ddb00c73f56a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h475
    h: 3e364e48e1a4
  review: drafted
  review_note: 'support check: partial - The network cable checks fit, but the concept is communication
    cable check and the passages only name the Ethernet network cable.'
- claim_id: c5
  rel: mitigated_by
  target: mit:network-connection-check
  note: Verify router and switches operate correctly.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h277
    h: ddb00c73f56a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h475
    h: 3e364e48e1a4
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:informational
  note: Corrective action needed only when the status is 10 Mbit.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h276
    h: f59bf0d5be4c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h474
    h: 325c332151ed
  review: drafted
  review_note: 'support check: partial - It is a status change notification and the corrective action
    applies only for 10 Mbit, but informational is not stated.'
- claim_id: c7
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r1
    h: 5fc6799b7f4c
  review: drafted
---
