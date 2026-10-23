---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-fault110
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Fault0110
aliases:
- Fault0110
- fault110
- Yaskawa Solectria Fault0110
- Bus imbalance
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Fault0110
code_key: fault110
display_message: Bus imbalance
vendor_severity: Fault
page: 83
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r2
    h: 93045c3d2bf3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r2
    h: 93045c3d2bf3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-imbalance
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r2
    h: 93045c3d2bf3
  review: drafted
  review_note: 'review: partial - The row says only ''Bus imbalance'' and links it to impedance and voltage
    imbalance between grid phases, so ''DC bus voltage'' adds…'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise the current limit first; replace inverter if alarm recurs.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r2
    h: 93045c3d2bf3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Escalation after adjustment fails.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r2
    h: 93045c3d2bf3
  review: drafted
---
