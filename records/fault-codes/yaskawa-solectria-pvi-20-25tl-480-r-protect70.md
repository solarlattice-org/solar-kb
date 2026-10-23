---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect70
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0070
aliases:
- Protect0070
- protect70
- Yaskawa Solectria Protect0070
- Bus imbalance
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0070
code_key: protect70
display_message: Bus imbalance
vendor_severity: Protection
page: 80
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r2
    h: 2f120d311abe
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r2
    h: 2f120d311abe
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-imbalance
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r2
    h: 2f120d311abe
  review: drafted
  review_note: 'review: partial - The row names the code ''Bus imbalance'' but never says DC bus voltage;
    it only mentions impedance and voltage imbalance between grid…'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise the DC current limit so the inverter can handle grid phase imbalance
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r2
    h: 2f120d311abe
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the alarm continues after the parameter change
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r2
    h: 2f120d311abe
  review: drafted
---
