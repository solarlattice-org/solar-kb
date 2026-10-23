---
id: fc:sma-sunny-island-us-f927
type: FaultCode
name: SMA SI-US F927
aliases:
- F927
- f927
- SMA F927
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F927
code_key: f927
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r9
    h: 155b307f1d8b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r9
    h: 155b307f1d8b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-charge-overcurrent
  note: Reported via SiCom communication
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r9
    h: 155b307f1d8b
  review: drafted
---
