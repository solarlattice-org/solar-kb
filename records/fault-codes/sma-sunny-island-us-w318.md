---
id: fc:sma-sunny-island-us-w318
type: FaultCode
name: SMA SI-US W318
aliases:
- W318
- w318
- SMA W318
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W318
code_key: w318
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r9
    h: 3f6a1ad61d77
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r9
    h: 3f6a1ad61d77
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  note: Reported for slave device 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=144.r9
    h: 3f6a1ad61d77
  review: drafted
---
