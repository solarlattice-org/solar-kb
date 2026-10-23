---
id: fc:chint-sch-200-250k-t-protect630
type: FaultCode
name: CPS SCH200-250K-T Protect0630
aliases:
- Protect0630
- protect630
- CPS Protect0630
- ARC Fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-200-250k-t
family_name: CPS SCH200K-T-US-480 / SCH250K-T-US-600
code: Protect0630
code_key: protect630
display_message: ARC Fault
vendor_severity: Protection
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r3
    h: 7586abf681e2
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:fault-localization
  note: Use this when inspection finds no defect and the fault comes back.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c8
  rel: mitigated_by
  target: mit:cable-replacement
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:connector-replacement
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: 'SCH manual: clear the fault by hand from the menu. Older manual: wait 5 minutes first. Contact
    service if all strings fault.'
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r6
    h: 6ba69e5e3533
  review: drafted
  review_note: 'support check: partial - u17 supports manual clearing via menu and contacting service
    if all strings fault, but the ''older manual: wait 5 minutes…'
---
