---
id: fc:canadian-solar-185-255k-igad
type: FaultCode
name: Canadian Solar 185-255K IG-AD
aliases:
- IG-AD
- igad
- Canadian Solar IG-AD
- Grid current sampling fail
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: IG-AD
code_key: igad
display_message: Grid current sampling fail
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:measurement-signal-error
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=9
    h: 1773bd293847
  review: drafted
  review_note: 'support check: partial - Listed in the Fault message table, but the row doesn''t state
    the class explicitly.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact installer if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c8
  rel: applies_to
  target: prod:canadian-solar-185-255k
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r17
    h: 966b32ee97bb
  review: drafted
---
