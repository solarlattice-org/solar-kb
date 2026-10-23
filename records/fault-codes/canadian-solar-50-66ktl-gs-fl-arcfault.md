---
id: fc:canadian-solar-50-66ktl-gs-fl-arcfault
type: FaultCode
name: Canadian Solar 50-66KTL-GS-FL ARC-FAULT
aliases:
- ARC-FAULT
- arcfault
- Canadian Solar ARC-FAULT
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 50-66ktl-gs-fl
family_name: CSI-50/60/66KTL-GS-FL
code: ARC-FAULT
code_key: arcfault
page: 27
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
  review_note: 'support check: partial - Solution says to inspect cable connections, which only loosely
    implies DC connectors; connectors are not named.'
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Reset after inspecting DC wiring; replace inverter if it persists.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r5
    h: b4f347f61cee
  review: drafted
- claim_id: c10
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r5
    h: b4f347f61cee
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8
    h: b80e6cf9a87a
  review: drafted
  review_note: 'support check: partial - Row appears in the table titled Fault messages but doesn''t state
    device behavior; fault class only implied by table title.'
---
