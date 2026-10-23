---
id: fc:sma-sunny-island-us-e110
type: FaultCode
name: SMA SI-US E110
aliases:
- E110
- e110
- SMA E110
- Shutdown due to error
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E110
code_key: e110
display_message: Shutdown due to error
page: 206
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r3
    h: 06da97e14c00
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: The device shuts down because of an error.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r3
    h: 06da97e14c00
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r3
    h: 06da97e14c00
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-shutdown
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=132.r3
    h: 06da97e14c00
  review: drafted
---
