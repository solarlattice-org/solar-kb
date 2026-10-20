---
id: fc:sma-stp-core1-us-9038
type: FaultCode
name: SMA CORE1-US 9038
aliases:
- '9038'
- SMA 9038
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9038'
code_key: '9038'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r5
    h: 7d6d4cbeb862
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r5
    h: 7d6d4cbeb862
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:rapid-shutdown-failure
  note: Redundant discharge function cannot be ensured.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r5
    h: 7d6d4cbeb862
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r5
    h: 7d6d4cbeb862
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - Redundant discharge not ensured is stated, but classification
    as rapid shutdown failure symptom is inferred.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r5
    h: 7d6d4cbeb862
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r5
    h: 7d6d4cbeb862
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r5
    h: 7d6d4cbeb862
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r5
    h: 7d6d4cbeb862
  review: drafted
---
