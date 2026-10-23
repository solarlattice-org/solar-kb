---
id: fc:sma-stp-core1-us-6702
type: FaultCode
name: SMA CORE1-US 6702
aliases:
- '6702'
- SMA 6702
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '6702'
code_key: '6702'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r2
    h: bcf0d1913bc2
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r2
    h: bcf0d1913bc2
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r2
    h: bcf0d1913bc2
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
