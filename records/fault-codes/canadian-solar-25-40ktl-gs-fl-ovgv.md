---
id: fc:canadian-solar-25-40ktl-gs-fl-ovgv
type: FaultCode
name: Canadian Solar 25-40KTL-GS-FL OV-G-V
aliases:
- OV-G-V
- ovgv
- Canadian Solar OV-G-V
- Over Grid Voltage
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 25-40ktl-gs-fl
family_name: CSI-25/30/36/40KTL-GS-FL
code: OV-G-V
code_key: ovgv
display_message: Over Grid Voltage
page: 31
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r3
    h: cbb79c5de19e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r3
    h: cbb79c5de19e
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r3
    h: 8e9ca52aa724
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r3
    h: cbb79c5de19e
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r3
    h: 8e9ca52aa724
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise upper voltage limit only with utility approval.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r3
    h: cbb79c5de19e
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r3
    h: 8e9ca52aa724
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  note: When voltage reads high under full power, undersized AC cabling is suspected.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r3
    h: cbb79c5de19e
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r3
    h: 8e9ca52aa724
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:canadian-solar-25-40ktl-gs-fl
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r3
    h: cbb79c5de19e
  review: drafted
---
