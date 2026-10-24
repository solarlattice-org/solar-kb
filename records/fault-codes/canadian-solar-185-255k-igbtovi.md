---
id: fc:canadian-solar-185-255k-igbtovi
type: FaultCode
name: Canadian Solar 185-255K IGBT-OV-I
aliases:
- IGBT-OV-I
- igbtovi
- Canadian Solar IGBT-OV-I
- Over IGBT current
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: IGBT-OV-I
code_key: igbtovi
display_message: Over IGBT current
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:power-board
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=9
    h: 1773bd293847
  review: drafted
  review_note: 'support check: partial - Intervention is required, implying fault, but the class is not
    explicitly stated.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; power board replacement if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:canadian-solar-185-255k
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r14
    h: 674a8840593d
  review: drafted
---
