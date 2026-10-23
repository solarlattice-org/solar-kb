---
id: fc:sma-sunny-island-us-w742
type: FaultCode
name: SMA SI-US W742
aliases:
- W742
- w742
- SMA W742
- Internal device communication of slave 3 interrupted
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W742
code_key: w742
display_message: Internal device communication of slave 3 interrupted
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r28
    h: a3e85c11b406
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r28
    h: a3e85c11b406
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  note: Applies to cluster slave 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r28
    h: a3e85c11b406
  review: drafted
---
