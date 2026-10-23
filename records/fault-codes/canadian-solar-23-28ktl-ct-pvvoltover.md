---
id: fc:canadian-solar-23-28ktl-ct-pvvoltover
type: FaultCode
name: Canadian Solar 23-28KTL-CT PVVoltOver
aliases:
- PVVoltOver
- pvvoltover
- Canadian Solar PVVoltOver
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: PVVoltOver
code_key: pvvoltover
vendor_severity: Protection
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  review: drafted
  review_note: 'support check: partial - It recommends checking whether PV voltage exceeds range, but
    does not explicitly state detection by DC voltage measurement.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general text says faults shut the inverter down, but the
    row does not explicitly state a trip; the connection…'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 30 minutes; then PV switch cycling, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r1
    h: f432f4633bf5
  review: drafted
---
