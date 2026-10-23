---
id: fc:sma-sunny-island-us-f158
type: FaultCode
name: SMA SI-US F158
aliases:
- F158
- f158
- SMA F158
- Voltage on output AC1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F158
code_key: f158
display_message: Voltage on output AC1
vendor_severity: '2'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r25
    h: ecc2d6d1e845
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r25
    h: ecc2d6d1e845
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-output-voltage-present
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r25
    h: ecc2d6d1e845
  review: drafted
---
