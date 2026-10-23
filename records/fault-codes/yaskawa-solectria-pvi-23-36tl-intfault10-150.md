---
id: fc:yaskawa-solectria-pvi-23-36tl-intfault10-150
type: FaultCode
name: Yaskawa Solectria PVI-TL IntFault0010-150
aliases:
- IntFault0010-150
- intfault10-150
- Yaskawa Solectria IntFault0010-150
- Internal non-critical fault within the inverter
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: IntFault0010-150
code_key: intfault10-150
code_from: 10
code_to: 150
display_message: Internal non-critical fault within the inverter
vendor_severity: Fault
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
  review_note: 'support check: partial - The row calls it a non-critical fault and says the inverter will
    restart, but it does not clearly state production…'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Restarts once the fault clears; if it persists, contact service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the fault does not clear
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20.r3
    h: f0aa059080d1
  review: drafted
---
