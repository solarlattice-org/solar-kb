---
id: fc:sma-shp-peak3-6701
type: FaultCode
name: SMA PEAK3-US 6701
aliases:
- '6701'
- SMA 6701
- Communication impaired
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '6701'
code_key: '6701'
display_message: Communication impaired
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.16
    h: 6fa74dde73e4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h352
    h: 425aae51d4ca
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h316
    h: 425aae51d4ca
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h352
    h: 425aae51d4ca
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h318
    h: 9ae650369fe8
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h354
    h: 9ae650369fe8
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h317
    h: c766760ec4c5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h353
    h: c766760ec4c5
  review: drafted
---
