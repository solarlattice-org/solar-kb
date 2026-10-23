---
id: fc:chint-sca-50-100k-t-protect830
type: FaultCode
name: CPS SCA50-100K-T Protect0830
aliases:
- Protect0830
- protect830
- CPS Protect0830
- MPPT5 VoltHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0830
code_key: protect830
display_message: MPPT5 VoltHigh
vendor_severity: Protection
page: 142
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r3
    h: 14fe271898ae
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r3
    h: 14fe271898ae
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r3
    h: 14fe271898ae
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r3
    h: 14fe271898ae
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Open-circuit PV voltage compared against displayed value and the 1000 V limit.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r3
    h: 14fe271898ae
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Adjust array so open-circuit voltage stays below limit; service if alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=60.r3
    h: 14fe271898ae
  review: drafted
  review_note: 'support check: partial - Passage says voltage must be under 1000 V and adjust, but doesn''t
    explicitly say string configuration correction.'
---
