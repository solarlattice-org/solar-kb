---
id: fc:sma-sunny-island-us-e901
type: FaultCode
name: SMA SI-US E901
aliases:
- E901
- e901
- SMA E901
- SOC recalibration started
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E901
code_key: e901
display_message: SOC recalibration started
page: 209
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=140.r3
    h: 33fe113708b2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting the start of battery state-of-charge recalibration.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=140.r3
    h: 33fe113708b2
  review: drafted
---
