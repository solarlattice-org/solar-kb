---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect180
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0180
aliases:
- Protect0180
- protect180
- Yaskawa Solectria Protect0180
- The sampling offset of DCI
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0180
code_key: protect180
display_message: The sampling offset of DCI
vendor_severity: Protection
page: 81
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-injection-monitoring-error
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
  review_note: 'support check: partial - The sampling offset of DCI is a DC injection sampling issue,
    but ''monitoring error'' is a looser characterization.'
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
  review_note: 'support check: partial - A sampling offset implies a sensor, but a current sensor is not
    named.'
- claim_id: c5
  rel: mitigated_by
  target: mit:sensor-recalibration
  note: Applies when the inverter can still start up.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only when the alarm persists and the inverter cannot start.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-20-25tl-480-r
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r2
    h: eb77817575ec
  review: drafted
---
