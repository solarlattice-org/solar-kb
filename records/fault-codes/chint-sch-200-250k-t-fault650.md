---
id: fc:chint-sch-200-250k-t-fault650
type: FaultCode
name: CPS SCH200-250K-T Fault0650
aliases:
- Fault0650
- fault650
- CPS Fault0650
- Static leakage current high
category: Inverters
make: chint
make_name: CPS
model_family: sch-200-250k-t
family_name: CPS SCH200K-T-US-480 / SCH250K-T-US-600
code: Fault0650
code_key: fault650
display_message: Static leakage current high
vendor_severity: Fault
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  note: Strings are added back one at a time until the faulty string is found
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sch-200-250k-t
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r6
    h: 9077abf83d90
  review: drafted
---
