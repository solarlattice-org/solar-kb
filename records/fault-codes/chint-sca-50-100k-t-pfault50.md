---
id: fc:chint-sca-50-100k-t-pfault50
type: FaultCode
name: CPS SCA50-100K-T PFault0050
aliases:
- PFault0050
- pfault50
- CPS PFault0050
- Bst hardware overcurrent fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0050
code_key: pfault50
display_message: Bst hardware overcurrent fault
page: 152
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r1
    h: eb8005ab1ad3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r1
    h: eb8005ab1ad3
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Row is in a Hardware Faults table and requires intervention (restart),
    implying fault, but no explicit classification is stated.'
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r1
    h: eb8005ab1ad3
  review: drafted
  review_note: 'review: partial - The row states a boost hardware overcurrent, but nothing in the passages
    says the current is on the DC side, so ''DC…'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r1
    h: eb8005ab1ad3
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r1
    h: eb8005ab1ad3
  review: drafted
---
