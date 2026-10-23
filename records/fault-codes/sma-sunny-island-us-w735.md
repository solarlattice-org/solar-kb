---
id: fc:sma-sunny-island-us-w735
type: FaultCode
name: SMA SI-US W735
aliases:
- W735
- w735
- SMA W735
- No message from cluster slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W735
code_key: w735
display_message: No message from cluster slave 2
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r22
    h: cb4c980532b0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r22
    h: cb4c980532b0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: No messages received from cluster slave 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r22
    h: cb4c980532b0
  review: drafted
---
