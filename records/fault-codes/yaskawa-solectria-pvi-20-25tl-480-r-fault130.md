---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-fault130
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Fault0130
aliases:
- Fault0130
- fault130
- Yaskawa Solectria Fault0130
- Bus over total voltage
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Fault0130
code_key: fault130
display_message: Bus over total voltage
vendor_severity: Fault
page: 83
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r1
    h: 36341e51ab53
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r1
    h: 36341e51ab53
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r1
    h: 36341e51ab53
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r1
    h: 36341e51ab53
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r1
    h: 36341e51ab53
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replacement if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r1
    h: 36341e51ab53
  review: drafted
  review_note: 'support check: partial - Power-cycle then replace stated; manual-reset clearing only implied.'
---
