---
id: fc:canadian-solar-185-255k-ovdcai
type: FaultCode
name: Canadian Solar 185-255K OV-DCA-I
aliases:
- OV-DCA-I
- ovdcai
- Canadian Solar OV-DCA-I
- DC input overcurrent
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: OV-DCA-I
code_key: ovdcai
display_message: DC input overcurrent
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:power-board
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=9
    h: 1773bd293847
  review: drafted
  review_note: 'support check: partial - Row is in a fault message table and implies a fault (overcurrent,
    intervention needed), but classification isn''t explicitly stated for…'
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; then isolate the faulty MPPT string, then replace power board.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r15
    h: eae16f7d5f0f
  review: drafted
  review_note: 'support check: partial - Restart inverter is listed first, then string removal, then power
    board change; but calling it manual-reset clearing is an inference,…'
---
