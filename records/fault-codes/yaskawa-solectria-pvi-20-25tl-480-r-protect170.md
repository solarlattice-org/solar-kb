---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect170
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0170
aliases:
- Protect0170
- protect170
- Yaskawa Solectria Protect0170
- DCI high
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0170
code_key: protect170
display_message: DCI high
vendor_severity: Protection
page: 81
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r3
    h: 926ae22c5f70
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r3
    h: 926ae22c5f70
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r3
    h: 926ae22c5f70
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise the DC injection limit first; replace inverter if fault remains.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r3
    h: 926ae22c5f70
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Escalation after limit adjustment fails.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r3
    h: 926ae22c5f70
  review: drafted
---
