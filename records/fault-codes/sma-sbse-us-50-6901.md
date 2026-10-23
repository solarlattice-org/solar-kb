---
id: fc:sma-sbse-us-50-6901
type: FaultCode
name: SMA SBSE-US-50 6901
aliases:
- '6901'
- SMA 6901
- Self-diagnosis > Input B defective
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '6901'
code_key: '6901'
display_message: Self-diagnosis > Input B defective
page: 113
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.50
    h: 9d5f3b77e091
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h664
    h: f7315b8a64ea
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.50
    h: 9d5f3b77e091
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h664
    h: f7315b8a64ea
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h665
    h: 399c45624de0
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.50
    h: 9d5f3b77e091
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h665
    h: 399c45624de0
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.50
    h: 9d5f3b77e091
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h666
    h: 03f467e448eb
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.50
    h: 9d5f3b77e091
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h666
    h: 03f467e448eb
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Service follows after verifying a string is connected to the input.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.50
    h: 9d5f3b77e091
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h666
    h: 03f467e448eb
  review: drafted
---
