---
id: fc:canadian-solar-185-255k-gimp
type: FaultCode
name: Canadian Solar 185-255K G-IMP
aliases:
- G-IMP
- gimp
- Canadian Solar G-IMP
- High grid impedance
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: G-IMP
code_key: gimp
display_message: High grid impedance
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r7
    h: a71ef8fdaeaf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r7
    h: a71ef8fdaeaf
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only if the utility permits changing the protection limit.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r7
    h: a71ef8fdaeaf
  review: drafted
---
