---
id: fc:chint-sca-50-100k-t-fault5080
type: FaultCode
name: CPS SCA50-100K-T Fault5080
aliases:
- Fault5080
- fault5080
- CPS Fault5080
- AC Bulkhead Connector Warning
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5080
code_key: fault5080
display_message: AC Bulkhead Connector Warning
vendor_severity: Fault
page: 147
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r4
    h: 2f7ebe2a4688
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r4
    h: 2f7ebe2a4688
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:connector-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r4
    h: 2f7ebe2a4688
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:ac-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r4
    h: 2f7ebe2a4688
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r4
    h: 2f7ebe2a4688
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r4
    h: 2f7ebe2a4688
  review: drafted
---
