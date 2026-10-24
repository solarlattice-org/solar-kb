---
id: fc:canadian-solar-23-28ktl-ct-gfcierr
type: FaultCode
name: Canadian Solar 23-28KTL-CT GFCIErr
aliases:
- GFCIErr
- gfcierr
- Canadian Solar GFCIErr
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: GFCIErr
code_key: gfcierr
vendor_severity: Protection
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
  review_note: 'support check: partial - PV module parasitic capacitance is listed as a cause, but the
    row does not directly say the PV array is affected.'
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'review: partial - Section 7.1.2 says the inverter shuts down automatically on system faults,
    and protection is one of the fault types, but the GFCIErr…'
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 10 minutes; then check connections, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:canadian-solar-23-28ktl-ct
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r3
    h: 5c24e1c588bd
  review: drafted
---
