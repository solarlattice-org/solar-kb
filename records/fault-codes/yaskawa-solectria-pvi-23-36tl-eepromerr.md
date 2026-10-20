---
id: fc:yaskawa-solectria-pvi-23-36tl-eepromerr
type: FaultCode
name: Yaskawa Solectria PVI-TL EepromErr
aliases:
- EepromErr
- eepromerr
- Yaskawa Solectria EepromErr
- Incorrect memory reading
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: EepromErr
code_key: eepromerr
display_message: Incorrect memory reading
vendor_severity: Alarm
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:data-storage-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm does not clear by itself
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; escalate to service if persistent
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  review: drafted
  review_note: 'support check: partial - Observing for 5 min for automatic clearing and escalating to
    service are stated, but ''normally clears'' is implied.'
---
