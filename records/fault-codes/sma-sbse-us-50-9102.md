---
id: fc:sma-sbse-us-50-9102
type: FaultCode
name: SMA SBSE-US-50 9102
aliases:
- '9102'
- SMA 9102
- Permanent operation inhibition
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9102'
code_key: '9102'
display_message: Permanent operation inhibition
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.71
    h: cc739024daa6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h766
    h: 9f1921bbbff2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:operation-inhibited
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h766
    h: 9f1921bbbff2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h767
    h: 66ec867e0332
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h767
    h: 66ec867e0332
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h768
    h: 199879385b16
  review: drafted
  review_note: 'support check: partial - Operation permanently interrupted and needs parameter reset by
    operator, but fault classification isn''t stated explicitly.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Charging and discharging operation is permanently interrupted.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h767
    h: 66ec867e0332
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Operator sets the operating mode parameter back to start.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h768
    h: 199879385b16
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h768
    h: 199879385b16
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.71
    h: cc739024daa6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h766
    h: 9f1921bbbff2
  review: drafted
---
