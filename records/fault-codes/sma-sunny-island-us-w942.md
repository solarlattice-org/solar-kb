---
id: fc:sma-sunny-island-us-w942
type: FaultCode
name: SMA SI-US W942
aliases:
- W942
- w942
- SMA W942
- 'Warning via SiCom: Battery undertemperature in charge mode'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W942
code_key: w942
display_message: 'Warning via SiCom: Battery undertemperature in charge mode'
vendor_severity: '1'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r9
    h: 4a366fe1c88b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r9
    h: 4a366fe1c88b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-battery-temperature
  note: Applies while the battery is in charge mode, as reported by the battery management over SiCom.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r9
    h: 4a366fe1c88b
  review: drafted
  review_note: 'support check: partial - Charge mode and SiCom stated; ''by the battery management'' not
    stated.'
---
