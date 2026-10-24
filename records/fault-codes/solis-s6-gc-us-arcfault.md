---
id: fc:solis-s6-gc-us-arcfault
type: FaultCode
name: Solis S6-GC ARC-FAULT
aliases:
- ARC-FAULT
- arcfault
- Solis ARC-FAULT
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: ARC-FAULT
code_key: arcfault
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r4
    h: b4f347f61cee
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r4
    h: 2517898b8bdf
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r5
    h: 7fd24b969497
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=29.r4
    h: ce5381fca1c5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r19
    h: ce5381fca1c5
  review: drafted
  review_note: 'support check: partial - PV connection arcing and tight connections are mentioned, but
    DC connector is not named specifically.'
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r5
    h: 7fd24b969497
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=29.r4
    h: ce5381fca1c5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r19
    h: ce5381fca1c5
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after the PV connection has been checked for arcing.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:solis-s6-gc-us
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r4
    h: b4f347f61cee
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r4
    h: 2517898b8bdf
  review: drafted
---
