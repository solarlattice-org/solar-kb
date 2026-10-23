---
id: fc:sma-sunny-island-us-w939
type: FaultCode
name: SMA SI-US W939
aliases:
- W939
- w939
- SMA W939
- 'Warning via SiCom: Battery overtemperature'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W939
code_key: w939
display_message: 'Warning via SiCom: Battery overtemperature'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r6
    h: bf8df6cc3b95
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r6
    h: bf8df6cc3b95
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-battery-temperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r6
    h: bf8df6cc3b95
  review: drafted
---
