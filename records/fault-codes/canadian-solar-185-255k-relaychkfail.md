---
id: fc:canadian-solar-185-255k-relaychkfail
type: FaultCode
name: Canadian Solar 185-255K RelayChk-FAIL
aliases:
- RelayChk-FAIL
- relaychkfail
- Canadian Solar RelayChk-FAIL
- Relay check fail
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: RelayChk-FAIL
code_key: relaychkfail
display_message: Relay check fail
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13
    h: 142f846b383e
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact installer if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r6
    h: 6a6a0bad6c85
  review: drafted
---
