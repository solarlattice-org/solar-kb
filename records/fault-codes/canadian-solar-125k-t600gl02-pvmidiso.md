---
id: fc:canadian-solar-125k-t600gl02-pvmidiso
type: FaultCode
name: Canadian Solar 125K-T600GL02 PV-MID-ISO
aliases:
- PV-MID-ISO
- pvmidiso
- Canadian Solar PV-MID-ISO
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 125k-t600gl02
family_name: CSI-125K-T600GL02-U
code: PV-MID-ISO
code_key: pvmidiso
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: drafted
  review_note: 'support check: partial - The external DC switch is only listed among items to physically
    check, not stated as the affected component.'
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: drafted
  review_note: 'support check: partial - Physical checking of connectors is the solution step, not stated
    as a detection method; the inverter detects it.'
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:external-fuse-check
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r6
    h: bb5d5cfa2d3d
  review: drafted
---
