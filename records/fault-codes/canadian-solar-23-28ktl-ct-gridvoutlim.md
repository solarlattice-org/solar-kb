---
id: fc:canadian-solar-23-28ktl-ct-gridvoutlim
type: FaultCode
name: Canadian Solar 23-28KTL-CT GridV.OutLim
aliases:
- GridV.OutLim
- gridvoutlim
- Canadian Solar GridV.OutLim
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: GridV.OutLim
code_key: gridvoutlim
vendor_severity: Protection
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The inverter shuts down on faults such as grid overvoltage/undervoltage,
    which implies a trip, but the row itself doesn''t say…'
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 10 minutes; then check grid and cable, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r1
    h: 8f7cb9b0424a
  review: drafted
  review_note: 'support check: partial - Passage says observe 10 minutes to see if the alarm clears automatically,
    then check grid/cable, then contact service; auto-clearing is…'
---
