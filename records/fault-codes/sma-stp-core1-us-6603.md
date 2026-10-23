---
id: fc:sma-stp-core1-us-6603
type: FaultCode
name: SMA CORE1-US 6603
aliases:
- '6603'
- SMA 6603
- Self-diagnosis > Overload
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '6603'
code_key: '6603'
display_message: Self-diagnosis > Overload
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r10
    h: 2cc675d4ac77
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r10
    h: 2cc675d4ac77
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r10
    h: 1862a479c741
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-overload
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r10
    h: 2cc675d4ac77
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r10
    h: 2cc675d4ac77
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r10
    h: 1862a479c741
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r10
    h: 1862a479c741
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19
    h: 3a4b34317f01
  review: drafted
  review_note: 'support check: partial - Cause must be determined by (the Service), text truncated; contact
    Service appears only in row layout adjacent to 6604, somewhat implied.'
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r10
    h: 1862a479c741
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19
    h: 3a4b34317f01
  review: drafted
  review_note: 'support check: partial - Cause must be determined by the Service is implied but the 6603
    row is split and truncated.'
---
