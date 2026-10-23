---
id: fc:sma-sbse-us-50-8205
type: FaultCode
name: SMA SBSE-US-50 8205
aliases:
- '8205'
- SMA 8205
- AFCI self-test successful
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '8205'
code_key: '8205'
display_message: AFCI self-test successful
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.59
    h: c7c850bb46d2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h709
    h: 82e78c4d0e6b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.59
    h: c7c850bb46d2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h709
    h: 82e78c4d0e6b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h710
    h: f76209535fc2
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.59
    h: c7c850bb46d2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h710
    h: f76209535fc2
  review: drafted
---
