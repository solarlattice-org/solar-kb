---
id: fc:sma-sunny-island-us-w940
type: FaultCode
name: SMA SI-US W940
aliases:
- W940
- w940
- SMA W940
- 'Warning via SiCom: Battery undertemperature'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W940
code_key: w940
display_message: 'Warning via SiCom: Battery undertemperature'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r7
    h: d499d43d67b1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r7
    h: d499d43d67b1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-battery-temperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r7
    h: d499d43d67b1
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
