---
id: fc:canadian-solar-75-100k-t480gl02-pvisopro0102
type: FaultCode
name: Canadian Solar 75-100K-T480GL02 PV ISO-PRO 01/02
aliases:
- PV ISO-PRO 01/02
- pvisopro0102
- Canadian Solar PV ISO-PRO 01/02
- Ground Protect ion
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 75-100k-t480gl02
family_name: CSI-75/80/90/100K-T480GL02-U
code: PV ISO-PRO 01/02
code_key: pvisopro0102
display_message: Ground Protect ion
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r4
    h: 88d1079d14c4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r4
    h: 94307fcd8bf8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r4
    h: 88d1079d14c4
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r4
    h: 94307fcd8bf8
  review: drafted
  review_note: 'support check: partial - Passage says to identify which string causes the isolation fault,
    implying PV strings, but the PV array isn''t named.'
- claim_id: c5
  rel: detected_by
  target: method:insulation-resistance-test
  note: Repeat measurement under the same weather conditions as the alarm if first result is normal.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r4
    h: 88d1079d14c4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r4
    h: 94307fcd8bf8
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r4
    h: 94307fcd8bf8
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r4
    h: 88d1079d14c4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r4
    h: 94307fcd8bf8
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Last step when insulation and cables are found normal.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r4
    h: 7ee4aa6d1521
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:canadian-solar-75-100k-t480gl02
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r3
    h: 7ee4aa6d1521
  review: drafted
---
