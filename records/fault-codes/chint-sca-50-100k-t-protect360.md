---
id: fc:chint-sca-50-100k-t-protect360
type: FaultCode
name: CPS SCA50-100K-T Protect0360
aliases:
- Protect0360
- protect360
- CPS Protect0360
- MPPT2 CurrHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0360
code_key: protect360
display_message: MPPT2 CurrHigh
vendor_severity: Protection
page: 137
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r3
    h: 2653baceb157
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r3
    h: 2653baceb157
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r3
    h: 2653baceb157
  review: drafted
  review_note: 'support check: partial - MPPT2 Current High is high current, but passage doesn''t say
    DC overcurrent explicitly; reasonable paraphrase though.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear within about 5 minutes; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r3
    h: 2653baceb157
  review: drafted
---
