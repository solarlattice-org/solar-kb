---
id: fc:yaskawa-solectria-pvi-23-36tl-arcboarderror
type: FaultCode
name: Yaskawa Solectria PVI-TL Arc Board Error
aliases:
- Arc Board Error
- arcboarderror
- Yaskawa Solectria Arc Board Error
- Internal Arc board self-check error
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: Arc Board Error
code_key: arcboarderror
display_message: Internal Arc board self-check error
vendor_severity: Protection
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r2
    h: 2c2e1fd47e9b
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r2
    h: 2c2e1fd47e9b
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r2
    h: 2c2e1fd47e9b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r6
    h: b80bdc9bc5ba
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r7
    h: 8333325a5a17
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r2
    h: 2c2e1fd47e9b
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r6
    h: b80bdc9bc5ba
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r7
    h: 8333325a5a17
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the error does not clear automatically.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r2
    h: 2c2e1fd47e9b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r7
    h: 8333325a5a17
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then contact service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r2
    h: 2c2e1fd47e9b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r6
    h: b80bdc9bc5ba
  review: drafted
---
