---
id: fc:solis-s6-eh3p-75-150k-us-ileakpro02
type: FaultCode
name: Solis S6-EH3P75-150K ILeak-PRO02
aliases:
- ILeak-PRO02
- ileakpro02
- Solis ILeak-PRO02
- Leakage current failure 02 (60mA)
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: ILeak-PRO02
code_key: ileakpro02
display_message: Leakage current failure 02 (60mA)
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r9
    h: ac654874cb8d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  note: 60 mA leakage threshold level.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r10
    h: bbb4ba3682d4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r10
    h: ac654874cb8d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r9
    h: ac654874cb8d
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r10
    h: bbb4ba3682d4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r10
    h: ac654874cb8d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r9
    h: ac654874cb8d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r10
    h: bbb4ba3682d4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r10
    h: ac654874cb8d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r9
    h: ac654874cb8d
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r10
    h: bbb4ba3682d4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r10
    h: ac654874cb8d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r9
    h: ac654874cb8d
  review: drafted
  review_note: 'support check: partial - Described as a ''failure'' but the row doesn''t state device
    behavior; fault is only implied.'
- claim_id: c6
  rel: applies_to
  target: prod:solis-s6-eh3p-75-150k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r9
    h: ac654874cb8d
  review: drafted
---
