---
id: fc:canadian-solar-23-28ktl-ct-arcboarderr
type: FaultCode
name: Canadian Solar 23-28KTL-CT Arcboard Err
aliases:
- Arcboard Err
- arcboarderr
- Canadian Solar Arcboard Err
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: Arcboard Err
code_key: arcboarderr
vendor_severity: Protection
page: 74
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-detector-failure
  note: Row names poor contact or damage of the arc board as the cause.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  note: Check the arc board's condition.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
  review_note: 'support check: partial - The row says to check whether the Arcboard is in good condition,
    which is close to a board check. It…'
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: The section says the inverter shuts down automatically when a listed fault occurs.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general section says the inverter shuts down automatically
    on faults, and the Arcboard row is in that table. The…'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Operator inspects the board and clears the arc fault from the menu; if that fails, contact service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
---
