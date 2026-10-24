---
id: fc:enphase-m215-m250-gfitripped
type: FaultCode
name: Enphase M215-M250 GFI Tripped
aliases:
- GFI Tripped
- gfitripped
- Enphase GFI Tripped
category: Inverters
make: enphase
make_name: Enphase
model_family: m215-m250
family_name: Enphase M215 / M250 Microinverters
code: GFI Tripped
code_key: gfitripped
page: 28
claims:
- claim_id: c1
  rel: defined_in
  target: src:enphase-enphase-m250-installation-and-operation-manual-60hz
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: sec=h50
    h: 95c0f95a942c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:enphase-enphase-envoy-s-installation-and-operation-manual
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h103
    h: 04a54f598668
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h103
    h: 04a54f598668
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h103
    h: 04a54f598668
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Clear message sent via Envoy resets GFI sensor; contact support if it does not clear
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h103
    h: 04a54f598668
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h104
    h: 5b2e22579115
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: applies_to
  target: prod:enphase-m215-m250
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: sec=h50
    h: 95c0f95a942c
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h103
    h: 04a54f598668
  review: drafted
---
