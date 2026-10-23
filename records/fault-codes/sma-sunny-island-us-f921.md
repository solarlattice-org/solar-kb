---
id: fc:sma-sunny-island-us-f921
type: FaultCode
name: SMA SI-US F921
aliases:
- F921
- f921
- SMA F921
- 'Error message via SiCom: Battery overvoltage'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F921
code_key: f921
display_message: 'Error message via SiCom: Battery overvoltage'
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r3
    h: 89527f8af382
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r3
    h: 89527f8af382
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-overvoltage
  note: Reported via SiCom communication
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r3
    h: 89527f8af382
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
