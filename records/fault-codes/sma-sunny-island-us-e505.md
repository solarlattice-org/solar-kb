---
id: fc:sma-sunny-island-us-e505
type: FaultCode
name: SMA SI-US E505
aliases:
- E505
- e505
- SMA E505
- Manual grid request
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E505
code_key: e505
display_message: Manual grid request
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r5
    h: 1b4ca5234b19
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Logs an operator-initiated grid request.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r5
    h: 1b4ca5234b19
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r5
    h: 1b4ca5234b19
  review: drafted
---
