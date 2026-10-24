---
id: fc:sma-stp-core1-us-8209
type: FaultCode
name: SMA CORE1-US 8209
aliases:
- '8209'
- SMA 8209
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '8209'
code_key: '8209'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r1
    h: a3b3ba978302
  review: drafted
- claim_id: c4
  rel: defined_in
  target: src:sma-kb-stp-us-41-events-8209-8212
  cite:
  - src: src:sma-kb-stp-us-41-events-8209-8212
    loc: sec=h1
    h: 35f6cfaf2a6f
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:self-test-failure
  note: Arc fault detection self-test error, interference level too low.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r1
    h: a3b3ba978302
  - src: src:sma-kb-stp-us-41-events-8209-8212
    loc: sec=h1
    h: 35f6cfaf2a6f
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r1
    h: a3b3ba978302
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:firmware-update
  note: 'Knowledge base: verify firmware is current before calling service.'
  cite:
  - src: src:sma-kb-stp-us-41-events-8209-8212
    loc: sec=h1
    h: 35f6cfaf2a6f
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r1
    h: a3b3ba978302
  - src: src:sma-kb-stp-us-41-events-8209-8212
    loc: sec=h1
    h: 35f6cfaf2a6f
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:service-required
  note: Manual says service must determine cause; knowledge base suggests firmware update first.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r1
    h: a3b3ba978302
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r1
    h: a3b3ba978302
  - src: src:sma-kb-stp-us-41-events-8209-8212
    loc: sec=h1
    h: 35f6cfaf2a6f
  review: drafted
---
