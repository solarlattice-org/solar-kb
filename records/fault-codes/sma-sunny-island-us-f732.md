---
id: fc:sma-sunny-island-us-f732
type: FaultCode
name: SMA SI-US F732
aliases:
- F732
- f732
- SMA F732
- Error in address assignment of cluster devices
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F732
code_key: f732
display_message: Error in address assignment of cluster devices
vendor_severity: '4'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r19
    h: 2530cd897444
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r19
    h: 2530cd897444
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Address assignment among cluster devices failed.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r19
    h: 2530cd897444
  review: drafted
---
