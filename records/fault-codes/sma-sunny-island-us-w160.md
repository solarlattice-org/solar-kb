---
id: fc:sma-sunny-island-us-w160
type: FaultCode
name: SMA SI-US W160
aliases:
- W160
- w160
- SMA W160
- Voltage on output AC1 slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W160
code_key: w160
display_message: Voltage on output AC1 slave 2
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r27
    h: e1cb27a345d0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r27
    h: e1cb27a345d0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-output-voltage-present
  note: Reported for slave 2
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r27
    h: e1cb27a345d0
  review: drafted
---
