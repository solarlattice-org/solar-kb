---
id: fc:canadian-solar-25-40k-t480gl01-gridintf
type: FaultCode
name: Canadian Solar 25-40K-T480GL01 GRID-INTF
aliases:
- GRID-INTF
- gridintf
- Canadian Solar GRID-INTF
- Grid unstable
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 25-40k-t480gl01
family_name: CSI-25/30/36/40K-T480GL01-UB
code: GRID-INTF
code_key: gridintf
display_message: Grid unstable
page: 42
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r1
    h: dc004aa7f58f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-instability
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r1
    h: 9305ab247836
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r1
    h: dc004aa7f58f
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r1
    h: dc004aa7f58f
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:waveform-spectrum-analysis
  note: Harmonic distortion test on AC line.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r1
    h: 9305ab247836
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r1
    h: dc004aa7f58f
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r1
    h: dc004aa7f58f
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r1
    h: 9305ab247836
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r1
    h: dc004aa7f58f
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r1
    h: dc004aa7f58f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:impedance-matching
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r1
    h: 9305ab247836
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r1
    h: dc004aa7f58f
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r1
    h: dc004aa7f58f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r1
    h: 9305ab247836
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8
    h: b80e6cf9a87a
  review: drafted
  review_note: 'support check: partial - It is in the Table 8.1 Fault messages, but the passage does not
    state the device behavior (stops or needs…'
---
