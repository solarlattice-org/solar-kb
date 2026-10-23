---
id: fc:sma-sunny-island-us-w851
type: FaultCode
name: SMA SI-US W851
aliases:
- W851
- w851
- SMA W851
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W851
code_key: w851
vendor_severity: '1'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r15
    h: d9419620ae36
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r15
    h: d9419620ae36
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  note: Battery side of charge controller 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r15
    h: d9419620ae36
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:external-short-circuit
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r15
    h: d9419620ae36
  review: drafted
---
