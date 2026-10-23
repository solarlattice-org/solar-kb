---
id: fc:sma-sunny-island-us-w755
type: FaultCode
name: SMA SI-US W755
aliases:
- W755
- w755
- SMA W755
- Battery-preservation mode 1 (LBM)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W755
code_key: w755
display_message: Battery-preservation mode 1 (LBM)
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r12
    h: '500e83690236'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r12
    h: '500e83690236'
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-protection-mode
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r12
    h: '500e83690236'
  review: drafted
---
