---
id: fc:chint-sca-50-100k-t-fault5070
type: FaultCode
name: CPS SCA50-100K-T Fault5070
aliases:
- Fault5070
- fault5070
- CPS Fault5070
- DC Bulkhead Connector Abnormal
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5070
code_key: fault5070
display_message: DC Bulkhead Connector Abnormal
vendor_severity: Fault
page: 148
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:connector-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Protection fault; a restart by power cycling implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48
    h: 9cff980c7e47
  review: drafted
  review_note: 'support check: partial - No passage states Fault5070 stops production; the Protection
    table covers other codes and a restart instruction only weakly implies a trip.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle AC and DC first; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r1
    h: 36c9d9b316a5
  review: drafted
---
