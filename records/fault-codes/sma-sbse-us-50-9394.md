---
id: fc:sma-sbse-us-50-9394
type: FaultCode
name: SMA SBSE-US-50 9394
aliases:
- '9394'
- SMA 9394
- Deep discharge protection activated
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9394'
code_key: '9394'
display_message: Deep discharge protection activated
page: 121
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.79
    h: ce59786cbf21
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h805
    h: 4535b16cf07b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-deep-discharge
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h805
    h: 4535b16cf07b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h806
    h: 0aebb35044f4
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: Holds for grid-connected systems, where it is an event rather than a warning.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h806
    h: 0aebb35044f4
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.79
    h: ce59786cbf21
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h805
    h: 4535b16cf07b
  review: drafted
---
