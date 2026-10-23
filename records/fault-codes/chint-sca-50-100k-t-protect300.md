---
id: fc:chint-sca-50-100k-t-protect300
type: FaultCode
name: CPS SCA50-100K-T Protect0300
aliases:
- Protect0300
- protect300
- CPS Protect0300
- Bus HW Overvolt
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0300
code_key: protect300
display_message: Bus HW Overvolt
vendor_severity: Protection
page: 136
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r4
    h: 095a9c6afb69
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r4
    h: 095a9c6afb69
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r4
    h: 095a9c6afb69
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r5
    h: f3ad5d61de4e
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then restart; persistent case needs service or inverter replacement.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r4
    h: 095a9c6afb69
  review: drafted
  review_note: 'support check: partial - u16 supports observe then restart then service, but the inverter
    replacement part of the note is only in u17, which…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r4
    h: 095a9c6afb69
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r5
    h: f3ad5d61de4e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r5
    h: f3ad5d61de4e
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r4
    h: 095a9c6afb69
  review: drafted
---
