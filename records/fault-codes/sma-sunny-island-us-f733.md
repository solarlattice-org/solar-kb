---
id: fc:sma-sunny-island-us-f733
type: FaultCode
name: SMA SI-US F733
aliases:
- F733
- f733
- SMA F733
- No message from cluster master (only slave)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F733
code_key: f733
display_message: No message from cluster master (only slave)
vendor_severity: '4'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r20
    h: ef8bd13bf99b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r20
    h: ef8bd13bf99b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: Raised on a slave when the cluster master stops sending messages.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r20
    h: ef8bd13bf99b
  review: drafted
---
