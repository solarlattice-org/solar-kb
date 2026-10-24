---
id: fc:chint-sca-25ktl-208-tempsensorerr
type: FaultCode
name: CPS SCA25KTL-208 TempSensorErr
aliases:
- TempSensorErr
- tempsensorerr
- CPS TempSensorErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: TempSensorErr
code_key: tempsensorerr
vendor_severity: Alarm
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r1
    h: d88196828df8
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r1
    h: d88196828df8
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:abnormal-temperature-reading
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r1
    h: d88196828df8
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:temperature-sensor-fault
  note: Damaged sensor or poorly seated sensor connector
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Reboot via AC disconnect; service if not corrected
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
  review_note: 'support check: partial - Reboot via AC disconnect is stated, but the passage doesn''t
    say it clears the alarm and has no service step.'
- claim_id: c9
  rel: applies_to
  target: prod:chint-sca-25ktl-208
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r1
    h: d88196828df8
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r2
    h: ba478906563a
  review: drafted
---
