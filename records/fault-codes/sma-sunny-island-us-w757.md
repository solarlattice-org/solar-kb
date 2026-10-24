---
id: fc:sma-sunny-island-us-w757
type: FaultCode
name: SMA SI-US W757
aliases:
- W757
- w757
- SMA W757
- Battery-preservation mode 3 (LBM)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W757
code_key: w757
display_message: Battery-preservation mode 3 (LBM)
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r14
    h: 0aa0678679c0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r14
    h: 0aa0678679c0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-protection-mode
  note: Battery preservation mode stage 3
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r14
    h: 0aa0678679c0
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r14
    h: 0aa0678679c0
  review: drafted
---
