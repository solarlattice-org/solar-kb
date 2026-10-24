---
id: fc:sma-sunny-island-us-w941
type: FaultCode
name: SMA SI-US W941
aliases:
- W941
- w941
- SMA W941
- 'Warning via SiCom: Battery overtemperature in charge mode'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W941
code_key: w941
display_message: 'Warning via SiCom: Battery overtemperature in charge mode'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r8
    h: 77807e4cd828
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r8
    h: 77807e4cd828
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-battery-temperature
  note: Only while the battery is in charge mode.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r8
    h: 77807e4cd828
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r8
    h: 77807e4cd828
  review: drafted
---
