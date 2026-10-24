---
id: fc:sma-sb-us-41-6702
type: FaultCode
name: SMA SB-US-41 6702
aliases:
- '6702'
- SMA 6702
- Communication impaired
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '6702'
code_key: '6702'
display_message: Communication impaired
page: 61
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.34
    h: 470ac2c4917f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h320
    h: 425aae51d4ca
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r2
    h: bcf0d1913bc2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h320
    h: 425aae51d4ca
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h321
    h: c766760ec4c5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r2
    h: bcf0d1913bc2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h321
    h: c766760ec4c5
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r2
    h: bcf0d1913bc2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h322
    h: 9ae650369fe8
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r2
    h: bcf0d1913bc2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h321
    h: c766760ec4c5
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r2
    h: bcf0d1913bc2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r2
    h: bcf0d1913bc2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h321
    h: c766760ec4c5
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.34
    h: 470ac2c4917f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h320
    h: 425aae51d4ca
  review: drafted
---
