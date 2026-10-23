---
id: fc:sma-stp-core1-us-4302
type: FaultCode
name: SMA CORE1-US 4302
aliases:
- '4302'
- SMA 4302
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '4302'
code_key: '4302'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r4
    h: 93c2d6ff802b
  review: drafted
- claim_id: c4
  rel: defined_in
  target: src:sma-kb-stp-us-41-events-4301-4302
  cite:
  - src: src:sma-kb-stp-us-41-events-4301-4302
    loc: sec=h1
    h: f9c7fab7dc47
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Manual reset needed when operation inhibition is activated.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: drafted
---
