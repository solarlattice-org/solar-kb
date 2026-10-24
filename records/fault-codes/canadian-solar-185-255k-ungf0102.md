---
id: fc:canadian-solar-185-255k-ungf0102
type: FaultCode
name: Canadian Solar 185-255K UN-G-F01/02
aliases:
- UN-G-F01/02
- ungf0102
- Canadian Solar UN-G-F01/02
- Under grid frequency
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: UN-G-F01/02
code_key: ungf0102
display_message: Under grid frequency
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r6
    h: 014bb367b27e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r6
    h: 014bb367b27e
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only if the utility permits changing the protection limit.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r6
    h: 014bb367b27e
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:canadian-solar-185-255k
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r6
    h: 014bb367b27e
  review: drafted
---
