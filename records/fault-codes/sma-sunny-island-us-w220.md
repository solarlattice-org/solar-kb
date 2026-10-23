---
id: fc:sma-sunny-island-us-w220
type: FaultCode
name: SMA SI-US W220
aliases:
- W220
- w220
- SMA W220
- Warning SOH < 70%
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W220
code_key: w220
display_message: Warning SOH < 70%
vendor_severity: '1'
page: 211
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r12
    h: 24e6e18fe368
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r12
    h: 24e6e18fe368
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-battery-health
  note: Battery state of health below 70 percent.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r12
    h: 24e6e18fe368
  review: drafted
---
