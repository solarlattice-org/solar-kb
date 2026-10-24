---
id: fc:canadian-solar-23-28ktl-ct-tempsensorerr
type: FaultCode
name: Canadian Solar 23-28KTL-CT TempSensorErr
aliases:
- TempSensorErr
- tempsensorerr
- Canadian Solar TempSensorErr
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: TempSensorErr
code_key: tempsensorerr
vendor_severity: Alarm
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:abnormal-temperature-reading
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Check displayed temperature first, then power-cycle; service if it persists.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
  review_note: 'support check: partial - Power-cycling is recommended, but the passage doesn''t say it
    clears the alarm; a manual reset is implied.'
- claim_id: c10
  rel: applies_to
  target: prod:canadian-solar-23-28ktl-ct
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=27.r1
    h: '769445e39817'
  review: drafted
---
