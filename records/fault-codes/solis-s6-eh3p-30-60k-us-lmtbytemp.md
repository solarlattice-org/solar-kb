---
id: fc:solis-s6-eh3p-30-60k-us-lmtbytemp
type: FaultCode
name: Solis S6-EH3P30-60K LmtByTemp
aliases:
- LmtByTemp
- lmtbytemp
- Solis LmtByTemp
- Over temperature power l imi ted
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: LmtByTemp
code_key: lmtbytemp
display_message: Over temperature power l imi ted
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r4
    h: 5d632380355d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=25.r4
    h: 5d632380355d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r4
    h: 5d632380355d
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r4
    h: 5d632380355d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: No action needed; normal operation continues.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r4
    h: 5d632380355d
  review: drafted
  review_note: 'support check: partial - Normal operation with no action needed is stated, but self-clearing
    is not explicitly stated.'
- claim_id: c6
  rel: applies_to
  target: prod:solis-s6-eh3p-30-60k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r4
    h: 5d632380355d
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=25.r4
    h: 5d632380355d
  review: drafted
---
