---
id: fc:solis-s6-eh2p-l-us-ovgv03
type: FaultCode
name: Solis S6-EH2P OV-G-V03
aliases:
- OV-G-V03
- ovgv03
- Solis OV-G-V03
- Grid transient overvoltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: OV-G-V03
code_key: ovgv03
display_message: Grid transient overvoltage
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r10
    h: 3f71b14c7283
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Transient overvoltage on the grid.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r10
    h: 3f71b14c7283
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r10
    h: 3f71b14c7283
  review: drafted
  review_note: 'support check: partial - The row doesn''t state a classification; it only says restart
    and check whether the fault continues.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r10
    h: 3f71b14c7283
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Only action given is a system restart, then check persistence.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r10
    h: 3f71b14c7283
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r10
    h: 3f71b14c7283
  review: drafted
  review_note: 'support check: partial - A restart is suggested, which is an operator action, but the
    row doesn''t say it clears the fault.'
- claim_id: c6
  rel: applies_to
  target: prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r10
    h: 3f71b14c7283
  review: drafted
---
