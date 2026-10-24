---
id: fc:chint-sca-50-100k-t-protect860
type: FaultCode
name: CPS SCA50-100K-T Protect0860
aliases:
- Protect0860
- protect860
- CPS Protect0860
- MPPT6 VoltHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0860
code_key: protect860
display_message: MPPT6 VoltHigh
vendor_severity: Protection
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Open-circuit PV voltage compared against displayed value and the 1000 V limit.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Adjust array so open-circuit voltage stays below limit; service if alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
  review_note: 'support check: partial - Passage says voltage must be under 1000 V and adjust, but doesn''t
    explicitly say string configuration correction.'
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r2
    h: bb55a73e252a
  review: drafted
---
