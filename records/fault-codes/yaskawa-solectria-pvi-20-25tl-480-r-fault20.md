---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-fault20
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Fault0020
aliases:
- Fault0020
- fault20
- Yaskawa Solectria Fault0020
- Bus over volt Hardware
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Fault0020
code_key: fault20
display_message: Bus over volt Hardware
vendor_severity: Fault
page: 84
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
  review_note: 'support check: partial - Restart is recommended, but the passage doesn''t state the fault
    clears by manual reset.'
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-20-25tl-480-r
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r3
    h: adb47939f934
  review: drafted
---
