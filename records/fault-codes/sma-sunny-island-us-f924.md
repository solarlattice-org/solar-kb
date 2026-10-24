---
id: fc:sma-sunny-island-us-f924
type: FaultCode
name: SMA SI-US F924
aliases:
- F924
- f924
- SMA F924
- 'Error message via SiCom: Battery undertemperature'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F924
code_key: f924
display_message: 'Error message via SiCom: Battery undertemperature'
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r6
    h: d3559cba2236
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r6
    h: d3559cba2236
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-battery-temperature
  note: Reported via SiCom communication
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r6
    h: d3559cba2236
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r6
    h: d3559cba2236
  review: drafted
---
