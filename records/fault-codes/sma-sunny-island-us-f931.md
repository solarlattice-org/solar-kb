---
id: fc:sma-sunny-island-us-f931
type: FaultCode
name: SMA SI-US F931
aliases:
- F931
- f931
- SMA F931
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F931
code_key: f931
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r13
    h: ac2f10b48cae
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r13
    h: ac2f10b48cae
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-management-error
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r13
    h: ac2f10b48cae
  review: drafted
---
