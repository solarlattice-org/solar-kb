---
id: fc:yaskawa-solectria-pvi-14-20tl-extfanerr
type: FaultCode
name: Yaskawa Solectria PVI-14-20TL ExtFanErr
aliases:
- ExtFanErr
- extfanerr
- Yaskawa Solectria ExtFanErr
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-14-20tl
family_name: Solectria PVI 14/20TL
code: ExtFanErr
code_key: extfanerr
vendor_severity: Alarm
page: 48
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r2
    h: 8528aeb9c303
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r2
    h: 8528aeb9c303
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18
    h: 97b941dabf7a
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: Applies when the fan is blocked by debris.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  review: drafted
  review_note: 'support check: partial - The row says to check the fan blades for debris because the fan
    is blocked, but it does not say…'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then debris check and restart; then contact service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r1
    h: 9e7339704f3a
  review: drafted
  review_note: 'support check: partial - Passages say observe 5 min for automatic clearing, then check
    debris, but no contact-service step appears and auto-reset is only implied.'
---
