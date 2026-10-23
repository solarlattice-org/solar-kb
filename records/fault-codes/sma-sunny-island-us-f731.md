---
id: fc:sma-sunny-island-us-f731
type: FaultCode
name: SMA SI-US F731
aliases:
- F731
- f731
- SMA F731
- Error in cluster configuration
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F731
code_key: f731
display_message: Error in cluster configuration
vendor_severity: '4'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r18
    h: d1dc53b6de92
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r18
    h: d1dc53b6de92
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Cluster configuration of multiple devices is faulty.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r18
    h: d1dc53b6de92
  review: drafted
---
