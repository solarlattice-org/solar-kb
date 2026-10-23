---
id: fc:chint-sca-50-100k-t-pfault30
type: FaultCode
name: CPS SCA50-100K-T PFault0030
aliases:
- PFault0030
- pfault30
- CPS PFault0030
- Inv Relay Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0030
code_key: pfault30
display_message: Inv Relay Fault
page: 151
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r4
    h: e16428b5b3ff
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r4
    h: e16428b5b3ff
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: drafted
  review_note: 'support check: partial - The table lists a hardware ''Inv Relay Fault'', but it does not
    state the device''s behaviour.'
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r4
    h: e16428b5b3ff
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r4
    h: e16428b5b3ff
  review: drafted
  review_note: 'support check: partial - The row names an inverter relay but not a grid-tie relay specifically.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r4
    h: e16428b5b3ff
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r4
    h: e16428b5b3ff
  review: drafted
---
