---
id: fc:canadian-solar-23-28ktl-ct-gridfoutlim
type: FaultCode
name: Canadian Solar 23-28KTL-CT GridF.OutLim
aliases:
- GridF.OutLim
- gridfoutlim
- Canadian Solar GridF.OutLim
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: GridF.OutLim
code_key: gridfoutlim
vendor_severity: Protection
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
  review_note: 'support check: partial - The fault concerns grid frequency and recommends checking it,
    but detection by frequency measurement is not explicitly stated.'
- claim_id: c7
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - The general text says the inverter shuts down automatically on
    faults like grid malfunction, but the row does not explicitly…'
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 10 minutes; then check grid and cable, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29.r2
    h: 104b0540aea5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
