---
id: fc:solis-s6-eh3p-30-60k-us-ileakpro01
type: FaultCode
name: Solis S6-EH3P30-60K ILeak-PRO01
aliases:
- ILeak-PRO01
- ileakpro01
- Solis ILeak-PRO01
- Leakage current failure 01 (30mA)
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: ILeak-PRO01
code_key: ileakpro01
display_message: Leakage current failure 01 (30mA)
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r9
    h: 49a37fe05fe9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r9
    h: 49a37fe05fe9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  note: 30 mA leakage threshold level.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r9
    h: 6a936388a819
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r9
    h: 49a37fe05fe9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r8
    h: 49a37fe05fe9
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r9
    h: 6a936388a819
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r9
    h: 49a37fe05fe9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r8
    h: 49a37fe05fe9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r9
    h: 6a936388a819
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r9
    h: 49a37fe05fe9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r8
    h: 49a37fe05fe9
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r9
    h: 6a936388a819
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r9
    h: 49a37fe05fe9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r8
    h: 49a37fe05fe9
  review: drafted
  review_note: 'support check: partial - Described as a ''failure'' but the row doesn''t state device
    behavior; fault is only implied.'
---
