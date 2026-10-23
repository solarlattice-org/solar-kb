---
id: fc:chint-sca-50-100k-t-protect240
type: FaultCode
name: CPS SCA50-100K-T Protect0240
aliases:
- Protect0240
- protect240
- CPS Protect0240
- Inv HW Overcurr
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0240
code_key: protect240
display_message: Inv HW Overcurr
vendor_severity: Protection
page: 136
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r1
    h: 6acb07e190e3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r1
    h: 6acb07e190e3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r1
    h: 6acb07e190e3
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r2
    h: 942a5485e959
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: One manual says to observe first; the other starts with a restart and then replacement.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r1
    h: 6acb07e190e3
  review: drafted
  review_note: 'support check: partial - u12 supports observing for auto-clearing, but the note''s claim
    about the other manual (u13) is not in the cited passage.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r2
    h: 942a5485e959
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r2
    h: 942a5485e959
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r1
    h: 6acb07e190e3
  review: drafted
---
