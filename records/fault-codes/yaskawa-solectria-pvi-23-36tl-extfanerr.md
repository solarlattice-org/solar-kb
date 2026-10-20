---
id: fc:yaskawa-solectria-pvi-23-36tl-extfanerr
type: FaultCode
name: Yaskawa Solectria PVI-TL ExtFanErr
aliases:
- ExtFanErr
- extfanerr
- Yaskawa Solectria ExtFanErr
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: ExtFanErr
code_key: extfanerr
vendor_severity: Alarm
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18
    h: 97b941dabf7a
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18
    h: 97b941dabf7a
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
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Inspect fan blades for debris
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: When the fan is blocked
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; otherwise power cycle and debris check, then service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r6
    h: 3c88374b8f57
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18
    h: 97b941dabf7a
  review: drafted
  review_note: 'support check: partial - Auto-clear observation within 5 min and then power cycle, debris
    check and contact service are given, but ''normally clears'' is…'
---
