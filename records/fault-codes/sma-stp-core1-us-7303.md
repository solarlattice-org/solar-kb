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
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  note: Cause must be determined by service, so intervention is needed.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r10
    h: 417f30a6fb06
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r10
    h: 417f30a6fb06
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
  review: drafted
---
