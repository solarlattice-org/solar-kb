---
id: fc:yaskawa-solectria-pvi-23-36tl-intfanerr
type: FaultCode
name: Yaskawa Solectria PVI-TL IntFanErr
aliases:
- IntFanErr
- intfanerr
- Yaskawa Solectria IntFanErr
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: IntFanErr
code_key: intfanerr
vendor_severity: Alarm
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r9
    h: dd6e1c42439a
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r9
    h: dd6e1c42439a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r9
    h: dd6e1c42439a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  note: Used when the alarm does not clear on its own.
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r10
    h: 723ace76c015
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r11
    h: 2bf91b0d7393
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=33.r1
    h: 563a1dce28e0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation if the alarm persists after restart.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r12
    h: de62313dc809
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=33.r1
    h: 563a1dce28e0
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then power cycle; then contact service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r9
    h: dd6e1c42439a
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=33.r1
    h: 563a1dce28e0
  review: drafted
  review_note: 'support check: partial - The row says to observe for automatic clearing first, but power
    cycling and service are also required if it does…'
- claim_id: c9
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-23-36tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
---
