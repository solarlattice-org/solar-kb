---
id: fc:chint-sca-50-100k-t-protect480
type: FaultCode
name: CPS SCA50-100K-T Protect0480
aliases:
- Protect0480
- protect480
- CPS Protect0480
- TZ Shutdown Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0480
code_key: protect480
display_message: TZ Shutdown Fault
vendor_severity: Protection
page: 139
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r2
    h: db7fd8061ec3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r2
    h: db7fd8061ec3
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r2
    h: db7fd8061ec3
  review: drafted
  review_note: 'support check: partial - The ''Shutdown Fault'' name implies stopping, but the row does
    not clearly state production stops.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear within about 5 minutes; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r2
    h: db7fd8061ec3
  review: drafted
---
