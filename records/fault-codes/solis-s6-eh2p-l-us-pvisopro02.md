---
id: fc:solis-s6-eh2p-l-us-pvisopro02
type: FaultCode
name: Solis S6-EH2P PV ISO-PRO02
aliases:
- PV ISO-PRO02
- pvisopro02
- Solis PV ISO-PRO02
- PV positive ground fault
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: PV ISO-PRO02
code_key: pvisopro02
display_message: PV positive ground fault
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  note: Positive pole to ground.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Inspect PV cable for damage.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r7
    h: 873d0b209293
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r7
    h: 891edc978a3d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r6
    h: 891edc978a3d
  review: drafted
  review_note: 'support check: partial - Called a ''PV positive ground fault'' but the row doesn''t state
    device behavior; fault is only implied.'
---
