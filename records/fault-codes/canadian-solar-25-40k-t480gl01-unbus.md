---
id: fc:canadian-solar-25-40k-t480gl01-unbus
type: FaultCode
name: Canadian Solar 25-40K-T480GL01 UN-BUS
aliases:
- UN-BUS
- unbus
- Canadian Solar UN-BUS
- DC BUS voltage is too low
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 25-40k-t480gl01
family_name: CSI-25/30/36/40K-T480GL01-UB
code: UN-BUS
code_key: unbus
display_message: DC BUS voltage is too low
page: 41
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r5
    h: 64c271c4d289
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r5
    h: 7868f947bd08
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r5
    h: 7868f947bd08
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r5
    h: 7868f947bd08
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  note: Internal damage or loose internal wiring assumed; inverter replacement.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r5
    h: 7868f947bd08
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r5
    h: 64c271c4d289
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=9.r5
    h: 7868f947bd08
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:canadian-solar-25-40k-t480gl01
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r5
    h: 64c271c4d289
  review: drafted
---
