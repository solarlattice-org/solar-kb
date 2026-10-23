---
id: fc:canadian-solar-50-66k-t480gl01-ovtem
type: FaultCode
name: Canadian Solar 50-66K-T480GL01 OV-TEM
aliases:
- OV-TEM
- ovtem
- Canadian Solar OV-TEM
- Temperature Protect ion
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 50-66k-t480gl01
family_name: CSI-50/60/66K-T480GL01-UB
code: OV-TEM
code_key: ovtem
display_message: Temperature Protect ion
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r18
    h: 828829faa49d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-ambient-temperature
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r18
    h: 828829faa49d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r18
    h: 828829faa49d
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only when measured ambient temperature is within range.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r3
    h: 98bb900b2b7d
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r2
    h: 98bb900b2b7d
  review: drafted
---
