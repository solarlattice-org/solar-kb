---
id: fc:sma-sunny-island-us-w741
type: FaultCode
name: SMA SI-US W741
aliases:
- W741
- w741
- SMA W741
- Internal device communication of slave 2 interrupted
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W741
code_key: w741
display_message: Internal device communication of slave 2 interrupted
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r27
    h: 2143ec8d94db
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r27
    h: 2143ec8d94db
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  note: Applies to cluster slave 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r27
    h: 2143ec8d94db
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r27
    h: 2143ec8d94db
  review: drafted
---
