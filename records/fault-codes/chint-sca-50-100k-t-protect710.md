---
id: fc:chint-sca-50-100k-t-protect710
type: FaultCode
name: CPS SCA50-100K-T Protect0710
aliases:
- Protect0710
- protect710
- CPS Protect0710
- Bst Hardware overcurrent
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0710
code_key: protect710
display_message: Bst Hardware overcurrent
vendor_severity: Protection
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r4
    h: 416427fce214
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r4
    h: 416427fce214
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-overcurrent-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r4
    h: 416427fce214
  review: drafted
  review_note: 'support check: partial - Boost hardware overcurrent is an internal overcurrent, but overvoltage
    isn''t mentioned.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm does not clear by itself.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r4
    h: 416427fce214
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r4
    h: 416427fce214
  review: drafted
---
