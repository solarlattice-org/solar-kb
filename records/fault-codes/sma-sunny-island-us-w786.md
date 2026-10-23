---
id: fc:sma-sunny-island-us-w786
type: FaultCode
name: SMA SI-US W786
aliases:
- W786
- w786
- SMA W786
- Slave does not receive a Syncpuls Slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W786
code_key: w786
display_message: Slave does not receive a Syncpuls Slave 3
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r24
    h: 9c7b3b9312c6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r24
    h: 9c7b3b9312c6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:sync-pulse-missing
  note: Applies to slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r24
    h: 9c7b3b9312c6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
