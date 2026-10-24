---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-arcprotect
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Arc Protect
aliases:
- Arc Protect
- arcprotect
- Yaskawa Solectria Arc Protect
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Arc Protect
code_key: arcprotect
page: 82
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r8
    h: 1a1e65fc9473
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r5
    h: 0a7c5910d375
  review: drafted
  review_note: 'review: partial - The cited rows do describe a shutdown over a possible arc fault, but
    they are the PVI-14-20TL table rows (tbl=20.r1, tbl=14.r5), while…'
- claim_id: c3
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
  review: drafted
- claim_id: c4
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
  review: drafted
- claim_id: c5
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
- claim_id: c6
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r8
    h: 1a1e65fc9473
  review: drafted
- claim_id: c7
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
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r5
    h: 0a7c5910d375
  review: drafted
- claim_id: c9
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
- claim_id: c10
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-20-25tl-480-r
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r8
    h: 1a1e65fc9473
  review: drafted
---
