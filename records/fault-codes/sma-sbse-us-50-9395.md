---
id: fc:sma-sbse-us-50-9395
type: FaultCode
name: SMA SBSE-US-50 9395
aliases:
- '9395'
- SMA 9395
- Battery separated externally
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9395'
code_key: '9395'
display_message: Battery separated externally
page: 121
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.80
    h: c84606e01edd
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h808
    h: 0a7b1ea9488d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-disconnected
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h808
    h: 0a7b1ea9488d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h809
    h: 7b4ea5b62a64
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.80
    h: c84606e01edd
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h808
    h: 0a7b1ea9488d
  review: drafted
---
