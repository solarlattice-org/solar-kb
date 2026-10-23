---
id: fc:canadian-solar-23-28ktl-ct-commerr
type: FaultCode
name: Canadian Solar 23-28KTL-CT CommErr
aliases:
- CommErr
- commerr
- Canadian Solar CommErr
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: CommErr
code_key: commerr
vendor_severity: Alarm
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:internal-communication-cable
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - The cause is poor contact at the terminal block connectors of
    the internal communication wires, which only loosely maps to…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: May clear by itself within 5 minutes; otherwise power-cycle, then service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r1
    h: d52a5f9167e8
  review: drafted
---
