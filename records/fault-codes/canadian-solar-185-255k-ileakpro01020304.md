---
id: fc:canadian-solar-185-255k-ileakpro01020304
type: FaultCode
name: Canadian Solar 185-255K ILeak-PRO 01/02/03/04
aliases:
- ILeak-PRO 01/02/03/04
- ileakpro01020304
- Canadian Solar ILeak-PRO 01/02/03/04
- Leakage current protection
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: ILeak-PRO 01/02/03/04
code_key: ileakpro01020304
display_message: Leakage current protection
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Covers the internal inverter cable connections.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13
    h: 142f846b383e
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:canadian-solar-185-255k
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r5
    h: dcb57b87715b
  review: drafted
---
