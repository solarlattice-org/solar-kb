---
id: fc:sma-sunny-island-us-w784
type: FaultCode
name: SMA SI-US W784
aliases:
- W784
- w784
- SMA W784
- Slave does not receive a Syncpuls Slave 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W784
code_key: w784
display_message: Slave does not receive a Syncpuls Slave 1
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r22
    h: 4932754af33a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r22
    h: 4932754af33a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:sync-pulse-missing
  note: Applies to slave 1
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r22
    h: 4932754af33a
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r22
    h: 4932754af33a
  review: drafted
---
