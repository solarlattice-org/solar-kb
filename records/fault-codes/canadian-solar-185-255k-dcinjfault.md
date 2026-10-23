---
id: fc:canadian-solar-185-255k-dcinjfault
type: FaultCode
name: Canadian Solar 185-255K DCinj-FAULT
aliases:
- DCinj-FAULT
- dcinjfault
- Canadian Solar DCinj-FAULT
- High DC injection current
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 185-255k
family_name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
code: DCinj-FAULT
code_key: dcinjfault
display_message: High DC injection current
page: 32
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r7
    h: b8dccd8805ed
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r7
    h: b8dccd8805ed
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r7
    h: b8dccd8805ed
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r7
    h: b8dccd8805ed
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r7
    h: b8dccd8805ed
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13
    h: 142f846b383e
  review: drafted
  review_note: 'support check: partial - The row is in a ''Fault message'' table, but it doesn''t say
    the device stops or needs intervention, so the…'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact installer if it persists.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r7
    h: b8dccd8805ed
  review: drafted
  review_note: 'support check: partial - A restart or contacting the installer is stated, but it doesn''t
    say the fault clears by manual reset; restart is…'
---
