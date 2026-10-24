---
id: fc:chint-sca-36ktl-pvxreverse
type: FaultCode
name: CPS SCA36KTL PVxReverse
aliases:
- PVxReverse
- pvxreverse
- CPS PVxReverse
- PVx input reverse connection x=1,2,3
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: PVxReverse
code_key: pvxreverse
display_message: PVx input reverse connection x=1,2,3
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  review: drafted
  review_note: 'support check: partial - PV string connection is corrected, but DC cable is not explicitly
    named.'
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct the reversed string connection.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  note: Requires operator intervention to correct wiring.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8
    h: ceb3e766d6c1
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-36ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  review: drafted
---
