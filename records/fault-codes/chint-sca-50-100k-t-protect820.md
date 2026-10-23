---
id: fc:chint-sca-50-100k-t-protect820
type: FaultCode
name: CPS SCA50-100K-T Protect0820
aliases:
- Protect0820
- protect820
- CPS Protect0820
- MPPT4 CurrHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0820
code_key: protect820
display_message: MPPT4 CurrHigh
vendor_severity: Protection
page: 142
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r2
    h: f902dbc1b80b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r2
    h: f902dbc1b80b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r2
    h: f902dbc1b80b
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm does not clear by itself.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r2
    h: f902dbc1b80b
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r2
    h: f902dbc1b80b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
