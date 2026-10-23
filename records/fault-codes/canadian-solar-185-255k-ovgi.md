---
id: fc:canadian-solar-185-255k-ovgi
type: FaultCode
name: Canadian Solar 185-255K OV-G-I
aliases:
- OV-G-I
- ovgi
- Canadian Solar OV-G-I
- Over grid current
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: OV-G-I
code_key: ovgi
display_message: Over grid current
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:power-board
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=9
    h: 1773bd293847
  review: drafted
  review_note: 'support check: partial - Intervention is required, implying fault, but the class is not
    explicitly stated.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; power board replacement if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r13
    h: da3a0c0f5b8d
  review: drafted
---
