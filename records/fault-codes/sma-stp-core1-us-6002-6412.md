---
id: fc:sma-stp-core1-us-6002-6412
type: FaultCode
name: SMA CORE1-US 6002-6412
aliases:
- 6002-6412
- SMA 6002-6412
- Self-diagnosis > Device disturbance
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: 6002-6412
code_key: 6002-6412
code_from: 6002
code_to: 6412
display_message: Self-diagnosis > Device disturbance
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r5
    h: 8f702697fd0e
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r5
    h: 8f702697fd0e
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r6
    h: 8f702697fd0e
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r5
    h: 8f702697fd0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r5
    h: 8f702697fd0e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r6
    h: 8f702697fd0e
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r5
    h: 8f702697fd0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r5
    h: 8f702697fd0e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r6
    h: 8f702697fd0e
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r5
    h: 8f702697fd0e
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r6
    h: 5694fc9103a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r5
    h: 8f702697fd0e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r6
    h: 5694fc9103a2
  review: drafted
---
