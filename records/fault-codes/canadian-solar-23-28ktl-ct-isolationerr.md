---
id: fc:canadian-solar-23-28ktl-ct-isolationerr
type: FaultCode
name: Canadian Solar 23-28KTL-CT IsolationErr
aliases:
- IsolationErr
- isolationerr
- Canadian Solar IsolationErr
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: IsolationErr
code_key: isolationerr
vendor_severity: Protection
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  review: drafted
  review_note: 'support check: partial - The row concerns insulation impedance and says to check PV system
    insulation, but does not name insulation resistance testing as…'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general text says the inverter shuts down on faults, but
    the row does not state production stops.'
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 10 minutes, e.g. humidity related; then insulation check, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r4
    h: c3524b17b912
  review: drafted
---
