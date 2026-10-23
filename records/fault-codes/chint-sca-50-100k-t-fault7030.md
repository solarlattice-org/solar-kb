---
id: fc:chint-sca-50-100k-t-fault7030
type: FaultCode
name: CPS SCA50-100K-T Fault7030
aliases:
- Fault7030
- fault7030
- CPS Fault7030
- N-line abnormal alarm
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault7030
code_key: fault7030
display_message: N-line abnormal alarm
vendor_severity: Fault
page: 150
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r4
    h: d67490bafd31
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r4
    h: d67490bafd31
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-line-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r4
    h: d67490bafd31
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r4
    h: d67490bafd31
  review: drafted
  review_note: 'support check: partial - The row says to check the inverter''s N-line setting against
    the actual wiring. That is a remedy step, and it…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Match the neutral configuration setting to the actual wiring; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r4
    h: d67490bafd31
  review: drafted
---
