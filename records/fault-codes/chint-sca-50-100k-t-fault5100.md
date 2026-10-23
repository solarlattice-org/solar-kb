---
id: fc:chint-sca-50-100k-t-fault5100
type: FaultCode
name: CPS SCA50-100K-T Fault5100
aliases:
- Fault5100
- fault5100
- CPS Fault5100
- Bulkhead Connector and Junction Box Abnormal
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5100
code_key: fault5100
display_message: Bulkhead Connector and Junction Box Abnormal
vendor_severity: Fault
page: 147
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:connector-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Protection fault; restart required after the alarm clears implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48
    h: 9cff980c7e47
  review: drafted
  review_note: 'support check: partial - No passage states Fault5100 stops production; the Protection
    table covers other codes and a restart instruction only weakly implies a trip.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Wait for alarm to clear, then restart; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r2
    h: 609cd94f72f0
  review: drafted
  review_note: 'support check: partial - Row says wait for auto-clearing, then restart the inverter and
    call service if it persists; the classification as manual reset…'
---
