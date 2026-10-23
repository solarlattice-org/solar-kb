---
id: fc:canadian-solar-185-255k-igfolf
type: FaultCode
name: Canadian Solar 185-255K IGFOL-F
aliases:
- IGFOL-F
- igfolf
- Canadian Solar IGFOL-F
- Grid current tracking fail
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: IGFOL-F
code_key: igfolf
display_message: Grid current tracking fail
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-current-tracking-failure
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=9
    h: 1773bd293847
  review: drafted
  review_note: 'support check: partial - Appears in the Fault message table, but the row doesn''t state
    its class explicitly.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact installer if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  review: drafted
---
