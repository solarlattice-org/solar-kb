---
id: fc:chint-sch-200-250k-t-protect0
type: FaultCode
name: CPS SCH200-250K-T Protect0000
aliases:
- Protect0000
- protect0
- CPS Protect0000
- Bus over voltage
category: Inverters
make: chint
make_name: CPS
model_family: sch-200-250k-t
family_name: CPS SCH200K-T-US-480 / SCH250K-T-US-600
code: Protect0000
code_key: protect0
display_message: Bus over voltage
vendor_severity: Protection
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r1
    h: a4f3b865db25
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r1
    h: a4f3b865db25
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r1
    h: b21c1bf340d0
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r1
    h: a4f3b865db25
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r1
    h: b21c1bf340d0
  review: drafted
  review_note: 'support check: partial - The passage says to measure the DC voltage as a check, not that
    the fault is detected by that measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r1
    h: a4f3b865db25
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the fault.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r1
    h: a4f3b865db25
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replace inverter or contact service if it persists.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r1
    h: a4f3b865db25
  review: drafted
---
