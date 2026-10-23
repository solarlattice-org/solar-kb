---
id: fc:sma-sunny-island-us-w946
type: FaultCode
name: SMA SI-US W946
aliases:
- W946
- w946
- SMA W946
- 'Warning via SiCom: short circuit'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W946
code_key: w946
display_message: 'Warning via SiCom: short circuit'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r13
    h: 3d6fcdd239fb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r13
    h: 3d6fcdd239fb
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:short-circuit
  note: Reported by the battery side over SiCom.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r13
    h: 3d6fcdd239fb
  review: drafted
  review_note: 'support check: partial - Short circuit via SiCom stated; ''battery side'' not stated.'
---
