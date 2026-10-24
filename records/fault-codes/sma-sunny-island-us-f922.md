---
id: fc:sma-sunny-island-us-f922
type: FaultCode
name: SMA SI-US F922
aliases:
- F922
- f922
- SMA F922
- 'Error message via SiCom: Battery undervoltage'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F922
code_key: f922
display_message: 'Error message via SiCom: Battery undervoltage'
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r4
    h: 7de1e6cb5839
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r4
    h: 7de1e6cb5839
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-undervoltage
  note: Reported via SiCom communication
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r4
    h: 7de1e6cb5839
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r4
    h: 7de1e6cb5839
  review: drafted
---
