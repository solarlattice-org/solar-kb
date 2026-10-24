---
id: fc:canadian-solar-185-255k-gridintf0102
type: FaultCode
name: Canadian Solar 185-255K GRID-INTF01/02
aliases:
- GRID-INTF01/02
- gridintf0102
- Canadian Solar GRID-INTF01/02
- Grid interference
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: GRID-INTF01/02
code_key: gridintf0102
display_message: Grid interference
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-instability
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:power-board
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  note: Troubleshooting entry requiring operator intervention.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=9
    h: 1773bd293847
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Row requires intervention (restart, board replacement) implying
    fault, but the class is not explicitly stated.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; power board replacement if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:canadian-solar-185-255k
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  review: drafted
---
