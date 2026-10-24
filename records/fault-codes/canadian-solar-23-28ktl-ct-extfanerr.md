---
id: fc:canadian-solar-23-28ktl-ct-extfanerr
type: FaultCode
name: Canadian Solar 23-28KTL-CT ExtFanErr
aliases:
- ExtFanErr
- extfanerr
- Canadian Solar ExtFanErr
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: ExtFanErr
code_key: extfanerr
vendor_severity: Alarm
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 5 minutes; then clear fan blades, power-cycle, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:canadian-solar-23-28ktl-ct
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r2
    h: e78f60f9726b
  review: drafted
---
