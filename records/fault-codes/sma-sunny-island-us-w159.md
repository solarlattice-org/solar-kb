---
id: fc:sma-sunny-island-us-w159
type: FaultCode
name: SMA SI-US W159
aliases:
- W159
- w159
- SMA W159
- Voltage on output AC1 slave 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W159
code_key: w159
display_message: Voltage on output AC1 slave 1
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r26
    h: aba34289cbdc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r26
    h: aba34289cbdc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-output-voltage-present
  note: Reported for slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r26
    h: aba34289cbdc
  review: drafted
---
