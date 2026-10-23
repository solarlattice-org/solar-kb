---
id: fc:canadian-solar-75-100k-t480gl02-ungv
type: FaultCode
name: Canadian Solar 75-100K-T480GL02 UN-G-V
aliases:
- UN-G-V
- ungv
- Canadian Solar UN-G-V
- Under Grid Voltage
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 75-100k-t480gl02
family_name: CSI-75/80/90/100K-T480GL02-U
code: UN-G-V
code_key: ungv
display_message: Under Grid Voltage
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r4
    h: 56652641b6cd
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r4
    h: 27e8f024f37e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r4
    h: cab3a7061bcd
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r4
    h: 56652641b6cd
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r4
    h: 27e8f024f37e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Lower limit adjusted only with utility approval.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r4
    h: 56652641b6cd
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r4
    h: 27e8f024f37e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:voltage-sensor
  note: Applies when display reading disagrees with measured voltage.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r4
    h: 56652641b6cd
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r4
    h: 27e8f024f37e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Escalation after measurement and grid standard checks.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=6.r4
    h: 56652641b6cd
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r4
    h: 27e8f024f37e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=10.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r4
    h: cab3a7061bcd
  review: drafted
---
