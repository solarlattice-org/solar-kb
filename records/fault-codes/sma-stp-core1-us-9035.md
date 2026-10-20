---
id: fc:sma-stp-core1-us-9035
type: FaultCode
name: SMA CORE1-US 9035
aliases:
- '9035'
- SMA 9035
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9035'
code_key: '9035'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r3
    h: c0aa437efcaf
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r3
    h: c0aa437efcaf
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:rapid-shutdown
  note: Successful discharge of DC inputs and AC output.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r3
    h: c0aa437efcaf
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r3
    h: c0aa437efcaf
  review: drafted
  review_note: 'support check: partial - Rapid Shutdown successful is stated, but ''triggered'' is not
    explicitly stated in these passages.'
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r3
    h: c0aa437efcaf
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r3
    h: c0aa437efcaf
  review: drafted
---
