---
id: fc:sma-sunny-island-us-w761
type: FaultCode
name: SMA SI-US W761
aliases:
- W761
- w761
- SMA W761
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W761
code_key: w761
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r18
    h: 731e075d37e3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r18
    h: 731e075d37e3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:no-output-voltage
  note: Applies to slave 3 of the main cluster
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r18
    h: 731e075d37e3
  review: drafted
---
