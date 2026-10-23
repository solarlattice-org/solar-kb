---
id: fc:canadian-solar-185-255k-ovgf0102
type: FaultCode
name: Canadian Solar 185-255K OV-G-F01/02
aliases:
- OV-G-F01/02
- ovgf0102
- Canadian Solar OV-G-F01/02
- Over grid frequency
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: OV-G-F01/02
code_key: ovgf0102
display_message: Over grid frequency
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r5
    h: 1ac98be7c247
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r5
    h: 1ac98be7c247
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only if the utility permits changing the protection limit.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r5
    h: 1ac98be7c247
  review: drafted
---
