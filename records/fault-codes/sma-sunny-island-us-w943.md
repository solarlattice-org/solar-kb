---
id: fc:sma-sunny-island-us-w943
type: FaultCode
name: SMA SI-US W943
aliases:
- W943
- w943
- SMA W943
- 'Warning via SiCom: battery charging current too high'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W943
code_key: w943
display_message: 'Warning via SiCom: battery charging current too high'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r10
    h: be5d14ac6c9b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r10
    h: be5d14ac6c9b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-charge-overcurrent
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r10
    h: be5d14ac6c9b
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r10
    h: be5d14ac6c9b
  review: drafted
---
