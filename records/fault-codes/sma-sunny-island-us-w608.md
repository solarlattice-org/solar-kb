---
id: fc:sma-sunny-island-us-w608
type: FaultCode
name: SMA SI-US W608
aliases:
- W608
- w608
- SMA W608
- Transfer relay does not open slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W608
code_key: w608
display_message: Transfer relay does not open slave 3
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r4
    h: 355d9785edcd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r4
    h: 355d9785edcd
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  note: On slave device 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r4
    h: 355d9785edcd
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r4
    h: 355d9785edcd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
