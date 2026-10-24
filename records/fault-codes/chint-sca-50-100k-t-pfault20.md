---
id: fc:chint-sca-50-100k-t-pfault20
type: FaultCode
name: CPS SCA50-100K-T PFault0020
aliases:
- PFault0020
- pfault20
- CPS PFault0020
- Bus Different High Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0020
code_key: pfault20
display_message: Bus Different High Fault
page: 151
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r3
    h: 5b1a1b008279
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r3
    h: 5b1a1b008279
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: drafted
  review_note: 'support check: partial - The table lists a hardware ''Bus Different High Fault'', but
    it does not state the device''s behaviour.'
- claim_id: c3
  rel: reports
  target: symptom:neutral-point-voltage-imbalance
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r3
    h: 5b1a1b008279
  review: drafted
  review_note: 'support check: partial - ''Bus Different High'' suggests an imbalance between the bus
    halves, but the row does not mention a neutral point.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r3
    h: 5b1a1b008279
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r3
    h: 5b1a1b008279
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r3
    h: 5b1a1b008279
  review: drafted
---
