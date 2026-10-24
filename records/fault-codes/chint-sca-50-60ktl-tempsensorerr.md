---
id: fc:chint-sca-50-60ktl-tempsensorerr
type: FaultCode
name: CPS SCA50-60KTL TempSensorErr
aliases:
- TempSensorErr
- tempsensorerr
- CPS TempSensorErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: TempSensorErr
code_key: tempsensorerr
vendor_severity: ALARM
page: 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  note: Damaged sensor or poor connector contact.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Check temperature display, then power-cycle via AC disconnect.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  review: drafted
---
