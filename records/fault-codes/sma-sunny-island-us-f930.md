---
id: fc:sma-sunny-island-us-f930
type: FaultCode
name: SMA SI-US F930
aliases:
- F930
- f930
- SMA F930
- 'Error message via SiCom: Short circuit'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F930
code_key: f930
display_message: 'Error message via SiCom: Short circuit'
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r12
    h: 5de9c9959559
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r12
    h: 5de9c9959559
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:short-circuit
  note: Reported via SiCom by the battery management.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r12
    h: 5de9c9959559
  review: drafted
  review_note: 'support check: partial - Short circuit via SiCom stated; ''by the battery management''
    not stated.'
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r12
    h: 5de9c9959559
  review: drafted
---
