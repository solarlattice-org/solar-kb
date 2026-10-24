---
id: fc:sma-sunny-island-us-w606
type: FaultCode
name: SMA SI-US W606
aliases:
- W606
- w606
- SMA W606
- Transfer relay does not open slave 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W606
code_key: w606
display_message: Transfer relay does not open slave 1
vendor_severity: '1'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r2
    h: 23c27acd51be
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r2
    h: 23c27acd51be
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  note: On slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r2
    h: 23c27acd51be
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:transfer-relay
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r2
    h: 23c27acd51be
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=149.r2
    h: 23c27acd51be
  review: drafted
---
