---
id: fc:chint-sca-50-100k-t-warn20
type: FaultCode
name: CPS SCA50-100K-T Warn0020
aliases:
- Warn0020
- warn20
- CPS Warn0020
- CAN Comm Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Warn0020
code_key: warn20
display_message: CAN Comm Abn
vendor_severity: Warning
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r1
    h: f41c5a6846da
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r1
    h: f41c5a6846da
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r1
    h: f41c5a6846da
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r1
    h: f41c5a6846da
  review: drafted
  review_note: 'support check: partial - The cause is poor contact of the internal communication wire
    terminals, but the solutions don''t list a communication cable check.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; if it persists, restart, then contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r1
    h: f41c5a6846da
  review: drafted
---
