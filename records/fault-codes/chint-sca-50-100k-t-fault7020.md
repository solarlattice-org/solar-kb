---
id: fc:chint-sca-50-100k-t-fault7020
type: FaultCode
name: CPS SCA50-100K-T Fault7020
aliases:
- Fault7020
- fault7020
- CPS Fault7020
- SVG voltage stability alarm
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault7020
code_key: fault7020
display_message: SVG voltage stability alarm
vendor_severity: Fault
page: 150
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r5
    h: 698eb7c22fe3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r5
    h: 698eb7c22fe3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:svg-voltage-instability
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r5
    h: 698eb7c22fe3
  review: drafted
  review_note: 'review: partial - The row supports an SVG voltage stability alarm, but nothing in the
    quoted passages says SVG means reactive compensation, so that reading…'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; if it persists, contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r5
    h: 698eb7c22fe3
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r5
    h: 698eb7c22fe3
  review: drafted
---
