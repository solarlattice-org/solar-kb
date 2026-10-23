---
id: fc:canadian-solar-23-28ktl-ct-arcprotect
type: FaultCode
name: Canadian Solar 23-28KTL-CT ARC Protect
aliases:
- ARC Protect
- arcprotect
- Canadian Solar ARC Protect
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: ARC Protect
code_key: arcprotect
vendor_severity: Protection
page: 74
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general text says the inverter shuts down on faults, but
    the row does not explicitly state production stops.'
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Operator clears the arc fault via menu command; inspect PV wiring, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r1
    h: 130d15b275c1
  review: drafted
---
