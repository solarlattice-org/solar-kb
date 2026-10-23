---
id: fc:sma-sunny-island-us-f810
type: FaultCode
name: SMA SI-US F810
aliases:
- F810
- f810
- SMA F810
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F810
code_key: f810
vendor_severity: '4'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r8
    h: 66fbd94a3117
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r8
    h: 66fbd94a3117
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:supply-voltage-invalid
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r8
    h: 66fbd94a3117
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:internal-power-supply-fault
  note: 15 V supply of the Multicluster Box.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r8
    h: 66fbd94a3117
  review: drafted
---
