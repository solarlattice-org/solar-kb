---
id: fc:chint-sca-36ktl-pv2voltover
type: FaultCode
name: CPS SCA36KTL PV2VoltOver
aliases:
- PV2VoltOver
- pv2voltover
- CPS PV2VoltOver
- PVx Over Volt x=1,2,3
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: PV2VoltOver
code_key: pv2voltover
display_message: PVx Over Volt x=1,2,3
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r5
    h: eaece40dc7e2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r5
    h: eaece40dc7e2
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Overvoltage is implied by the name and 1000V limit, but the passage
    doesn''t explicitly say it reports DC overvoltage; reasonably implied.'
- claim_id: c3
  rel: detected_by
  target: method:voc-measurement
  note: Compare the meter reading at the DC terminals with the displayed value.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r5
    h: eaece40dc7e2
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-voltage-margin-design
  note: Applies when display matches meter within 2%.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r5
    h: eaece40dc7e2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Applies when display deviates from meter by more than 2%.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r5
    h: eaece40dc7e2
  review: drafted
---
