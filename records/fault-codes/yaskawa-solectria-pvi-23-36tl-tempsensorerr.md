---
id: fc:yaskawa-solectria-pvi-23-36tl-tempsensorerr
type: FaultCode
name: Yaskawa Solectria PVI-TL TempSensorErr
aliases:
- TempSensorErr
- tempsensorerr
- Yaskawa Solectria TempSensorErr
- Abnormal temperature reading
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: TempSensorErr
code_key: tempsensorerr
display_message: Abnormal temperature reading
vendor_severity: Alarm
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:abnormal-temperature-reading
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart via internal disconnects first; contact customer service if the error persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
  review_note: 'support check: partial - The restart via disconnects and the contact-service steps are
    present, but the passages don''t state a manual reset classification.'
---
