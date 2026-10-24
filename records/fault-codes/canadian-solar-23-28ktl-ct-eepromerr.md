---
id: fc:canadian-solar-23-28ktl-ct-eepromerr
type: FaultCode
name: Canadian Solar 23-28KTL-CT EepromErr
aliases:
- EepromErr
- eepromerr
- Canadian Solar EepromErr
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: EepromErr
code_key: eepromerr
vendor_severity: Alarm
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:memory-error
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:memory-unit
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 5 minutes; otherwise service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:canadian-solar-23-28ktl-ct
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r3
    h: 465ea144bc19
  review: drafted
---
