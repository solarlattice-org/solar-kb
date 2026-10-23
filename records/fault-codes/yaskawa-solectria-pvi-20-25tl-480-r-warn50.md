---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-warn50
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Warn0050
aliases:
- Warn0050
- warn50
- Yaskawa Solectria Warn0050
- TempSensorErr
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Warn0050
code_key: warn50
display_message: TempSensorErr
vendor_severity: Warning
page: 79
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:abnormal-temperature-reading
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Check the display, then power-cycle; contact after-sales service if it persists
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
  review_note: 'support check: partial - Power-cycle is recommended, but the passage doesn''t state that
    the warning clears by manual reset.'
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation step
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r3
    h: 1a288429d4be
  review: drafted
---
