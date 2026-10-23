---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect230
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0230
aliases:
- Protect0230
- protect230
- Yaskawa Solectria Protect0230
- Inverter open-loop self-test fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0230
code_key: protect230
display_message: Inverter open-loop self-test fault
vendor_severity: Protection
page: 82
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r6
    h: 881719b38210
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r7
    h: 28f6dfb6f638
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r6
    h: 881719b38210
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r6
    h: 881719b38210
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r7
    h: 28f6dfb6f638
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r6
    h: 881719b38210
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r7
    h: 28f6dfb6f638
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r6
    h: 881719b38210
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r7
    h: 28f6dfb6f638
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replacement if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r6
    h: 881719b38210
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r7
    h: 28f6dfb6f638
  review: drafted
  review_note: 'support check: partial - Power-cycle then replace stated; manual-reset clearing only implied.'
---
