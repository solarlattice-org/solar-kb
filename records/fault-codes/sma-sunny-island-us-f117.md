---
id: fc:sma-sunny-island-us-f117
type: FaultCode
name: SMA SI-US F117
aliases:
- F117
- f117
- SMA F117
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F117
code_key: f117
vendor_severity: '2'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r9
    h: bced2600d253
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r9
    h: bced2600d253
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Short-circuit current control remained active too long.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r9
    h: bced2600d253
  review: drafted
---
