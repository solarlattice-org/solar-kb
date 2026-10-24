---
id: fc:chint-sca-50-100k-t-pfault40
type: FaultCode
name: CPS SCA50-100K-T PFault0040
aliases:
- PFault0040
- pfault40
- CPS PFault0040
- Steady State GFCI Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0040
code_key: pfault40
display_message: Steady State GFCI Fault
page: 151
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - The table lists a hardware ''Steady State GFCI Fault'', but it
    does not state the device''s behaviour.'
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fault-localization
  note: Reconnect strings one at a time to isolate the string that leaks to ground.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
  review_note: 'support check: partial - The row says to check the PV and ground wires and trace the faulted
    string''s wiring, which only loosely points…'
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Trace the faulted string's wiring for leakage to earth; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r5
    h: bf96b5415e9b
  review: drafted
---
