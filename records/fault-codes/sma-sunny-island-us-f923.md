---
id: fc:sma-sunny-island-us-f923
type: FaultCode
name: SMA SI-US F923
aliases:
- F923
- f923
- SMA F923
- 'Error message via SiCom: Battery overtemperature'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F923
code_key: f923
display_message: 'Error message via SiCom: Battery overtemperature'
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r5
    h: 38660ed0c7e2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r5
    h: 38660ed0c7e2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-battery-temperature
  note: Reported via SiCom communication
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r5
    h: 38660ed0c7e2
  review: drafted
---
