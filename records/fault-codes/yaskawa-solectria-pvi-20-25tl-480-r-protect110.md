---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect110
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0110
aliases:
- Protect0110
- protect110
- Yaskawa Solectria Protect0110
- BUS over voltage (firmware)
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0110
code_key: protect110
display_message: BUS over voltage (firmware)
vendor_severity: Protection
page: 82
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r2
    h: 0c4fdd9197c2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r2
    h: 0c4fdd9197c2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r2
    h: 0c4fdd9197c2
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r2
    h: 0c4fdd9197c2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r2
    h: 0c4fdd9197c2
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replacement if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r2
    h: 0c4fdd9197c2
  review: drafted
  review_note: 'support check: partial - Restart by power-cycling is stated, but ''manual reset'' clearing
    classification is implied only; fairly reasonable though not explicit that the…'
---
