---
id: fc:canadian-solar-75-100k-t480gl02-revedc
type: FaultCode
name: Canadian Solar 75-100K-T480GL02 Reve-DC
aliases:
- Reve-DC
- revedc
- Canadian Solar Reve-DC
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 75-100k-t480gl02
family_name: CSI-75/80/90/100K-T480GL02-U
code: Reve-DC
code_key: revedc
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r10
    h: 8b1a0c30407d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r10
    h: 8b1a0c30407d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r10
    h: 8b1a0c30407d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only at low irradiance with string current below the stated limit and DC switches off.
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r10
    h: 8b1a0c30407d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when polarity is correct but strings have unequal module counts.
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:canadian-solar-75-100k-t480gl02
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r6
    h: b997e3ed88b8
  review: drafted
---
