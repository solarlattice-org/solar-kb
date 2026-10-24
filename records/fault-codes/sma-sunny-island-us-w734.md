---
id: fc:sma-sunny-island-us-w734
type: FaultCode
name: SMA SI-US W734
aliases:
- W734
- w734
- SMA W734
- No message from cluster slave 1
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W734
code_key: w734
display_message: No message from cluster slave 1
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r21
    h: 2c123a490b66
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r21
    h: 2c123a490b66
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: No messages received from cluster slave 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r21
    h: 2c123a490b66
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r21
    h: 2c123a490b66
  review: drafted
---
