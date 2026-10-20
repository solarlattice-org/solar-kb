---
id: fc:yaskawa-solectria-pvi-23-36tl-pv12voltover
type: FaultCode
name: Yaskawa Solectria PVI-TL PV1 (2) VoltOver
aliases:
- PV1 (2) VoltOver
- pv12voltover
- Yaskawa Solectria PV1 (2) VoltOver
- DC input voltage exceeds the specified value
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: PV1 (2) VoltOver
code_key: pv12voltover
display_message: DC input voltage exceeds the specified value
vendor_severity: Protection
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  review: drafted
  review_note: 'support check: partial - The solution says to verify DC open circuit input voltage, but
    detection by Voc measurement is not stated.'
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  review: drafted
  review_note: 'support check: partial - DC input over-voltage implies the PV input, but the PV array
    is not explicitly named.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; then voltage check, power cycle, service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  review: drafted
  review_note: 'support check: partial - Observe 30 min for auto-clear, then voltage check, power cycle
    and service; ''normally'' is implied.'
---
