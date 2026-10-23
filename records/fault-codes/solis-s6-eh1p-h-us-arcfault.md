---
id: fc:solis-s6-eh1p-h-us-arcfault
type: FaultCode
name: Solis S6-EH1P ARC-FAULT
aliases:
- ARC-FAULT
- arcfault
- Solis ARC-FAULT
- ARC detected in DC circuit
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: ARC-FAULT
code_key: arcfault
display_message: ARC detected in DC circuit
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after the PV connection has been checked for arcing.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
---
