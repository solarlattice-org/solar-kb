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
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Qualified personnel inspect the inverter wiring section.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists after the observation period or no wiring issue is found.
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
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset
  note: Observe about 10 min for automatic clearing; escalate to service if it persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r1
    h: 785c73630b0d
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r2
    h: 437dc3430b87
  review: drafted
---
