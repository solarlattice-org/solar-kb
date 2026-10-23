---
id: fc:sma-sunny-island-us-w736
type: FaultCode
name: SMA SI-US W736
aliases:
- W736
- w736
- SMA W736
- No message from cluster slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W736
code_key: w736
display_message: No message from cluster slave 3
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r23
    h: 43d0c7a4947c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r23
    h: 43d0c7a4947c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: No messages received from cluster slave 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r23
    h: 43d0c7a4947c
  review: drafted
---
