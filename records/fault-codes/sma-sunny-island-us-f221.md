---
id: fc:sma-sunny-island-us-f221
type: FaultCode
name: SMA SI-US F221
aliases:
- F221
- f221
- SMA F221
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F221
code_key: f221
vendor_severity: '4'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r13
    h: 8b82500ca8a9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r13
    h: 8b82500ca8a9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: External battery management present but no external energy management configured.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r13
    h: 8b82500ca8a9
  review: drafted
---
