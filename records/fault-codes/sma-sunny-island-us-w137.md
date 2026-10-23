---
id: fc:sma-sunny-island-us-w137
type: FaultCode
name: SMA SI-US W137
aliases:
- W137
- w137
- SMA W137
- Derating due to temperature (heat sink or transformer)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W137
code_key: w137
display_message: Derating due to temperature (heat sink or transformer)
vendor_severity: '1'
page: 210
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
  review_note: 'support check: partial - Derating due to temperature implies over-temperature but the
    passage doesn''t state overtemperature explicitly.'
- claim_id: c5
  rel: affects
  target: comp:heat-sink
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:transformer
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:derate
  note: No reduced-output value is given.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r17
    h: 8ac6350ddbbb
  review: drafted
---
