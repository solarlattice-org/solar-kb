---
id: fc:sma-stp-core1-us-10286
type: FaultCode
name: SMA CORE1-US 10286
aliases:
- '10286'
- SMA 10286
- Wi-Fi connection lost
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10286'
code_key: '10286'
display_message: Wi-Fi connection lost
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h322
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h323
    h: c03208dd7c40
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h239
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h240
    h: c03208dd7c40
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: Inverter lost its Wi-Fi link to the selected network.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h322
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h323
    h: c03208dd7c40
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h239
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h240
    h: c03208dd7c40
  review: drafted
---
