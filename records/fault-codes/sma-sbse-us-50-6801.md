---
id: fc:sma-sbse-us-50-6801
type: FaultCode
name: SMA SBSE-US-50 6801
aliases:
- '6801'
- SMA 6801
- Self-diagnosis > Input A defective
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '6801'
code_key: '6801'
display_message: Self-diagnosis > Input A defective
page: 113
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.49
    h: 5a80bfdaef29
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h659
    h: fadd96b1d787
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.49
    h: 5a80bfdaef29
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h659
    h: fadd96b1d787
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h660
    h: 5008693fcbb9
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.49
    h: 5a80bfdaef29
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h660
    h: 5008693fcbb9
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.49
    h: 5a80bfdaef29
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h661
    h: 8d3083c9ddd3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.49
    h: 5a80bfdaef29
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h661
    h: 8d3083c9ddd3
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Service follows after verifying a string is connected to the input.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.49
    h: 5a80bfdaef29
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h661
    h: 8d3083c9ddd3
  review: drafted
---
