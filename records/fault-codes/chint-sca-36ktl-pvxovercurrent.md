---
id: fc:chint-sca-36ktl-pvxovercurrent
type: FaultCode
name: CPS SCA36KTL PVx Over current
aliases:
- PVx Over current
- pvxovercurrent
- CPS PVx Over current
- PVx Over current x=1,2,3
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: PVx Over current
code_key: pvxovercurrent
display_message: PVx Over current x=1,2,3
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  review: drafted
  review_note: 'support check: partial - Row says check PV input current, but doesn''t explicitly say
    it is detected by string current measurement.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  note: Check PV input current first; restart; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Escalates to inverter replacement if a restart does not clear it.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-36ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  review: drafted
---
