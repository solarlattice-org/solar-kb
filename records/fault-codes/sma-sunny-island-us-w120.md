---
id: fc:sma-sunny-island-us-w120
type: FaultCode
name: SMA SI-US W120
aliases:
- W120
- w120
- SMA W120
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W120
code_key: w120
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r12
    h: d45bd19e38f7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r12
    h: d45bd19e38f7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  note: Short-circuit current control active too long on slave device 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r12
    h: d45bd19e38f7
  review: drafted
---
