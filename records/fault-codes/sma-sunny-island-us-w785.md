---
id: fc:sma-sunny-island-us-w785
type: FaultCode
name: SMA SI-US W785
aliases:
- W785
- w785
- SMA W785
- Slave does not receive a Syncpuls Slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W785
code_key: w785
display_message: Slave does not receive a Syncpuls Slave 2
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r23
    h: b2a2cf52a260
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r23
    h: b2a2cf52a260
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:sync-pulse-missing
  note: Applies to slave 2
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r23
    h: b2a2cf52a260
  review: drafted
---
