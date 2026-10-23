---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-fault150
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Fault0150
aliases:
- Fault0150
- fault150
- Yaskawa Solectria Fault0150
- Open-loop self-check failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Fault0150
code_key: fault150
display_message: Open-loop self-check failure
vendor_severity: Fault
page: 84
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r4
    h: 6424449c71ad
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r4
    h: 6424449c71ad
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r4
    h: 6424449c71ad
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r4
    h: 6424449c71ad
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r4
    h: 6424449c71ad
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if fault persists.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r4
    h: 6424449c71ad
  review: drafted
  review_note: 'support check: partial - Restart is recommended, but clearing by manual reset is not explicitly
    stated.'
---
