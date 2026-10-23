---
id: fc:sma-sunny-island-us-w953
type: FaultCode
name: SMA SI-US W953
aliases:
- W953
- w953
- SMA W953
- Time for external battery management exceeded
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W953
code_key: w953
display_message: Time for external battery management exceeded
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r18
    h: 06c5e3c86a9e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r18
    h: 06c5e3c86a9e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-management-timeout
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r18
    h: 06c5e3c86a9e
  review: drafted
---
