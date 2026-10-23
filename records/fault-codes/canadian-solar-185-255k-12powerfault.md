---
id: fc:canadian-solar-185-255k-12powerfault
type: FaultCode
name: Canadian Solar 185-255K 12Power-FAULT
aliases:
- 12Power-FAULT
- 12powerfault
- Canadian Solar 12Power-FAULT
- 12V power supply fault
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: 12Power-FAULT
code_key: 12powerfault
display_message: 12V power supply fault
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r3
    h: b620d3902110
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:internal-power-supply-fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r3
    h: b620d3902110
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r3
    h: b620d3902110
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r3
    h: b620d3902110
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r3
    h: b620d3902110
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13
    h: 142f846b383e
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact installer if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r3
    h: b620d3902110
  review: drafted
---
