---
id: fc:chint-sca-36ktl-warn50
type: FaultCode
name: CPS SCA36KTL Warn0050
aliases:
- Warn0050
- warn50
- CPS Warn0050
- TempSensorErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Warn0050
code_key: warn50
display_message: TempSensorErr
vendor_severity: Warning
page: 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Check temperature display, power-cycle via AC disconnect, then service if persistent.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  review: drafted
---
