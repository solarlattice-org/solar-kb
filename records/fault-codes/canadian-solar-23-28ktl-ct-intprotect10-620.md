---
id: fc:canadian-solar-23-28ktl-ct-intprotect10-620
type: FaultCode
name: Canadian Solar 23-28KTL-CT IntProtect0010-0620
aliases:
- IntProtect0010-0620
- intprotect10-620
- Canadian Solar IntProtect0010-0620
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: IntProtect0010-0620
code_key: intprotect10-620
code_from: 10
code_to: 620
vendor_severity: Protection
page: 74
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r3
    h: 59a050772ba7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r3
    h: 59a050772ba7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r3
    h: 59a050772ba7
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r3
    h: 59a050772ba7
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: The section says the inverter shuts down automatically when a listed fault occurs.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r3
    h: 59a050772ba7
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general text says the inverter shuts down automatically on
    failure and the row is a protection-type fault. The row…'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears by itself within about ten minutes; if it persists, contact service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r3
    h: 59a050772ba7
  review: drafted
---
