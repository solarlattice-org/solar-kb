---
id: fc:canadian-solar-23-28ktl-ct-tempover
type: FaultCode
name: Canadian Solar 23-28KTL-CT TempOver
aliases:
- TempOver
- tempover
- Canadian Solar TempOver
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: TempOver
code_key: tempover
vendor_severity: Protection
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
  review_note: 'support check: partial - A blocked fan is a cause and checking the fan is a solution,
    but the passages don''t say the cooling…'
- claim_id: c5
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:proper-installation
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  note: Protection-type code; section states the inverter shuts down automatically on such failures.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The inverter shuts down automatically on failures in general,
    but TempOver itself isn''t explicitly tied to shutdown.'
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset
  note: After checks, may clear by itself within 30 minutes; otherwise service.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:canadian-solar-23-28ktl-ct
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=28.r4
    h: 70d67883e813
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=29
    h: 8dba70b44933
  review: drafted
---
