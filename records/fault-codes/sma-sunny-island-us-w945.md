---
id: fc:sma-sunny-island-us-w945
type: FaultCode
name: SMA SI-US W945
aliases:
- W945
- w945
- SMA W945
- 'Warning via SiCom: error in the battery'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W945
code_key: w945
display_message: 'Warning via SiCom: error in the battery'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r12
    h: 0690c4cd2d74
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r12
    h: 0690c4cd2d74
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-error
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r12
    h: 0690c4cd2d74
  review: drafted
---
