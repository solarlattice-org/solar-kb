---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect150
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0150
aliases:
- Protect0150
- protect150
- Yaskawa Solectria Protect0150
- Mini MCU Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0150
code_key: protect150
display_message: Mini MCU Fault
vendor_severity: Protection
page: 81
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r1
    h: 2a1311d47c69
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r1
    h: 2a1311d47c69
  review: drafted
  review_note: 'support check: partial - Mini MCU Fault is an internal device fault, but the generic wording
    is an interpretation.'
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r1
    h: 2a1311d47c69
  review: drafted
  review_note: 'support check: partial - An MCU fault implies the control board, but the passage doesn''t
    state this.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r1
    h: 2a1311d47c69
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r1
    h: 2a1311d47c69
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; replacement if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r6
    h: fc8a58ace8ab
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r1
    h: 2a1311d47c69
  review: drafted
---
