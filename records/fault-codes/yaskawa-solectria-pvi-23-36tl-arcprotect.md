---
id: fc:yaskawa-solectria-pvi-23-36tl-arcprotect
type: FaultCode
name: Yaskawa Solectria PVI-TL Arc Protect
aliases:
- Arc Protect
- arcprotect
- Yaskawa Solectria Arc Protect
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: Arc Protect
code_key: arcprotect
vendor_severity: Protection
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r5
    h: 0a7c5910d375
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: indicates
  target: fm:arc-fault
  note: Internal DC-side arc is the first listed cause
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r5
    h: 0a7c5910d375
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c5
  rel: indicates
  target: fm:arc-detector-failure
  note: 'Second listed cause: the arc board itself is faulty'
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r6
    h: fcb0d94e792e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r6
    h: fcb0d94e792e
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r8
    h: 1a1e65fc9473
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r8
    h: 1a1e65fc9473
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists or inspection finds nothing
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r5
    h: 0a7c5910d375
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: has_recovery
  target: ec:auto-reset
  note: Can clear on its own within 10 minutes; if not, wiring inspection and then service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r5
    h: 0a7c5910d375
  review: drafted
---
