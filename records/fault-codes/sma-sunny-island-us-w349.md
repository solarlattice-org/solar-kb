---
id: fc:sma-sunny-island-us-w349
type: FaultCode
name: SMA SI-US W349
aliases:
- W349
- w349
- SMA W349
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W349
code_key: w349
vendor_severity: '1'
page: 213
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r10
    h: 6486a79674fb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r10
    h: 6486a79674fb
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overload
  note: Reported for slave 2
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=146.r10
    h: 6486a79674fb
  review: drafted
---
