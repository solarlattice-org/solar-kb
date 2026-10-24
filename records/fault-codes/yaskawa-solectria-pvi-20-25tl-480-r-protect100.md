---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect100
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0100
aliases:
- Protect0100
- protect100
- Yaskawa Solectria Protect0100
- The sensor fault of leakage current
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0100
code_key: protect100
display_message: The sensor fault of leakage current
vendor_severity: Protection
page: 82
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:current-sensor-fault
  note: Leakage current sensor.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:filter-board
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:filter-board-replacement
  note: If restart does not clear the fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Alternative to filter board replacement if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; board or inverter replacement if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
  review_note: 'support check: partial - Power-cycle then replacement is stated, but clearing by manual
    reset is only implied.'
- claim_id: c9
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-20-25tl-480-r
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: drafted
---
