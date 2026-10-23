---
id: fc:canadian-solar-50-66ktl-gs-fl-ovgf
type: FaultCode
name: Canadian Solar 50-66KTL-GS-FL OV-G-F
aliases:
- OV-G-F
- ovgf
- Canadian Solar OV-G-F
- Over Grid Frequency
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 50-66ktl-gs-fl
family_name: CSI-50/60/66KTL-GS-FL
code: OV-G-F
code_key: ovgf
display_message: Over Grid Frequency
page: 26
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r1
    h: 50f760e81627
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r1
    h: 50f760e81627
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r1
    h: 50f760e81627
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r1
    h: 50f760e81627
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r1
    h: 50f760e81627
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Upper frequency limit adjusted only with utility approval.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r1
    h: 50f760e81627
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r1
    h: 50f760e81627
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Escalation if measurement circuit is suspected faulty.
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=7.r1
    h: 50f760e81627
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r1
    h: 50f760e81627
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r1
    h: 5f4341ada0d6
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=10.r1
    h: 5f4341ada0d6
  review: drafted
---
