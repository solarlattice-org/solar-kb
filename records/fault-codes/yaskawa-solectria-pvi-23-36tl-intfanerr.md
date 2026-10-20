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
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
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
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm persists after a power cycle
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
  review_note: 'support check: partial - Contact Customer Service if the error does not clear is stated,
    but the passages do not say it applies specifically…'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears within minutes on its own; otherwise power cycle, then call service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r4
    h: a7eb1991dfd5
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r5
    h: 820d5c711ec3
  review: drafted
  review_note: 'support check: partial - Passages say observe 5 min to see if it clears automatically,
    implying auto-clear, but ''normally'' and the power cycle then…'
---
