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
  target: symptom:memory-error
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r4
    h: 3ae09badb452
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:memory-unit
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r4
    h: 3ae09badb452
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm does not clear automatically.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r5
    h: 7dcca451f1c1
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then contact service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r1
    h: d226490d0b40
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r4
    h: 3ae09badb452
  review: drafted
---
