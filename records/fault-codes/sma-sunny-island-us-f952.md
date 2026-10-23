---
id: fc:sma-sunny-island-us-f952
type: FaultCode
name: SMA SI-US F952
aliases:
- F952
- f952
- SMA F952
- Time for external battery management exceeded
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F952
code_key: f952
display_message: Time for external battery management exceeded
vendor_severity: '3'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r17
    h: 804f83351d54
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r17
    h: 804f83351d54
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-management-timeout
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r17
    h: 804f83351d54
  review: drafted
---
