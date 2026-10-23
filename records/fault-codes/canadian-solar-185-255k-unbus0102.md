---
id: fc:canadian-solar-185-255k-unbus0102
type: FaultCode
name: Canadian Solar 185-255K UN-BUS01/02
aliases:
- UN-BUS01/02
- unbus0102
- Canadian Solar UN-BUS01/02
- Under DC bus voltage
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: UN-BUS01/02
code_key: unbus0102
display_message: Under DC bus voltage
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r11
    h: f45a9c4d23db
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r11
    h: f45a9c4d23db
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:choke
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r11
    h: f45a9c4d23db
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r11
    h: f45a9c4d23db
  review: drafted
---
