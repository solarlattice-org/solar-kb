---
id: fc:canadian-solar-185-255k-ovbus
type: FaultCode
name: Canadian Solar 185-255K OV-BUS
aliases:
- OV-BUS
- ovbus
- Canadian Solar OV-BUS
- Over DC bus voltage
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: OV-BUS
code_key: ovbus
display_message: Over DC bus voltage
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r10
    h: 29b90f8a67cf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r4
    h: f41c6bb3523f
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r4
    h: d72ef23dec5b
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r4
    h: d72ef23dec5b
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r10
    h: 29b90f8a67cf
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r4
    h: f41c6bb3523f
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r4
    h: d72ef23dec5b
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r4
    h: d72ef23dec5b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:choke
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r10
    h: 29b90f8a67cf
  review: drafted
  review_note: 'support check: partial - Passage says check inverter inductor connection, which implies
    but does not state the choke is affected.'
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r10
    h: 29b90f8a67cf
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r4
    h: f41c6bb3523f
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r4
    h: d72ef23dec5b
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r4
    h: d72ef23dec5b
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  note: Internal damage or loose internal wiring assumed; inverter replacement.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r4
    h: f41c6bb3523f
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r4
    h: d72ef23dec5b
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r4
    h: d72ef23dec5b
  review: drafted
---
