---
id: fc:canadian-solar-23-28ktl-ct-intfault10-150
type: FaultCode
name: Canadian Solar 23-28KTL-CT IntFault0010-0150
aliases:
- IntFault0010-0150
- intfault10-150
- Canadian Solar IntFault0010-0150
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: IntFault0010-0150
code_key: intfault10-150
code_from: 10
code_to: 150
vendor_severity: Fault
page: 74
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: The section says the inverter shuts down automatically when a listed fault occurs.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general text says the inverter shuts down automatically on
    failure and lists faults in the table. The row itself…'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: One forced restart once other problems are ruled out; if the fault remains, contact service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:canadian-solar-23-28ktl-ct
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r4
    h: 826a97abe382
  review: drafted
---
