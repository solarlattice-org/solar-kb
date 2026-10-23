---
id: fc:sma-stp-core1-us-10252
type: FaultCode
name: SMA CORE1-US 10252
aliases:
- '10252'
- SMA 10252
- '[Interface]: communication disrupted'
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10252'
code_key: '10252'
display_message: '[Interface]: communication disrupted'
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h303
    h: 471c768880b9
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h304
    h: c527469c7586
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h220
    h: 471c768880b9
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h221
    h: c527469c7586
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h305
    h: 471c768880b9
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h306
    h: c527469c7586
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h304
    h: c527469c7586
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h480
    h: 0d22961c20a3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h481
    h: 5a9966a8d705
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h305
    h: 3e364e48e1a4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h482
    h: 3e364e48e1a4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h305
    h: 3e364e48e1a4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h482
    h: 3e364e48e1a4
  review: drafted
---
