---
id: fc:sma-sunny-island-us-w204
type: FaultCode
name: SMA SI-US W204
aliases:
- W204
- w204
- SMA W204
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W204
code_key: w204
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r4
    h: d5a8fc795d28
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r4
    h: d5a8fc795d28
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-voltage-out-of-range
  note: Reported for slave 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r4
    h: d5a8fc795d28
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r4
    h: d5a8fc795d28
  review: drafted
---
