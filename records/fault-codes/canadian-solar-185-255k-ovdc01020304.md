---
id: fc:canadian-solar-185-255k-ovdc01020304
type: FaultCode
name: Canadian Solar 185-255K OV-DC01/02/03/04
aliases:
- OV-DC01/02/03/04
- ovdc01020304
- Canadian Solar OV-DC01/02/03/04
- Over DC voltage
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: OV-DC01/02/03/04
code_key: ovdc01020304
display_message: Over DC voltage
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r9
    h: 1f836cab2884
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r9
    h: 1f836cab2884
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r9
    h: 1f836cab2884
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r9
    h: 1f836cab2884
  review: drafted
---
