---
id: fc:chint-sca-50-100k-t-protect190
type: FaultCode
name: CPS SCA50-100K-T Protect0190
aliases:
- Protect0190
- protect190
- CPS Protect0190
- ISO Low
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0190
code_key: protect190
display_message: ISO Low
vendor_severity: Protection
page: 134
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
  review_note: 'support check: partial - ''Isolation Voltage Low'' with leakage-to-earth tracing implies
    low insulation, but the passage doesn''t say insulation resistance explicitly.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
  review_note: 'support check: partial - The procedure traces the wiring of the faulted string for leakage,
    which implies the DC cabling, but cables aren''t named explicitly.'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  note: Reconnect strings one at a time to find the string that triggers the alarm.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r3
    h: f29a32afae43
  review: drafted
---
