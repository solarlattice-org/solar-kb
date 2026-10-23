---
id: fc:sma-stp-core1-us-10904
type: FaultCode
name: SMA CORE1-US 10904
aliases:
- '10904'
- SMA 10904
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10904'
code_key: '10904'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r8
    h: 2d9a561369ff
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Reports a configured voltage monitoring disconnection limit when Webconnect is enabled
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r8
    h: 2d9a561369ff
  review: drafted
---
