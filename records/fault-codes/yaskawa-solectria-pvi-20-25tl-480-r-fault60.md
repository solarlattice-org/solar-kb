---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-fault60
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Fault0060
aliases:
- Fault0060
- fault60
- Yaskawa Solectria Fault0060
- CPLD Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Fault0060
code_key: fault60
display_message: CPLD Fault
vendor_severity: Fault
page: 84
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r2
    h: a2eaee3a693f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r2
    h: a2eaee3a693f
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:control-board
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r2
    h: a2eaee3a693f
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r2
    h: a2eaee3a693f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:control-board-replacement
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r2
    h: a2eaee3a693f
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle AC and DC first; replace control board or inverter if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r2
    h: a2eaee3a693f
  review: drafted
  review_note: 'support check: partial - Power cycle is a manual restart, but the passage doesn''t say
    the fault clears by it; only that replacement is…'
---
