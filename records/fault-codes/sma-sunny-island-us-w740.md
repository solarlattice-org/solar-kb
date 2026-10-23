---
id: fc:sma-sunny-island-us-w740
type: FaultCode
name: SMA SI-US W740
aliases:
- W740
- w740
- SMA W740
- Internal device communication of slave 1 interrupted
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W740
code_key: w740
display_message: Internal device communication of slave 1 interrupted
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r26
    h: 0aa4eb86d756
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r26
    h: 0aa4eb86d756
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  note: Applies to cluster slave 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r26
    h: 0aa4eb86d756
  review: drafted
---
