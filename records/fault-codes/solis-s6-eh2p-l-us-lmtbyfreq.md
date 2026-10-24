---
id: fc:solis-s6-eh2p-l-us-lmtbyfreq
type: FaultCode
name: Solis S6-EH2P LmtByFreq
aliases:
- LmtByFreq
- lmtbyfreq
- Solis LmtByFreq
- Frequency power limited
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: LmtByFreq
code_key: lmtbyfreq
display_message: Frequency power limited
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r5
    h: 8899000c3172
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r5
    h: 8899000c3172
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r5
    h: 8899000c3172
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r5
    h: 8899000c3172
  review: drafted
  review_note: 'support check: partial - Frequency power limited, but the passages don''t say the grid
    frequency is out of range.'
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r5
    h: 8899000c3172
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r5
    h: 8899000c3172
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r5
    h: 8899000c3172
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: No action needed; normal operation continues.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r5
    h: 8899000c3172
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r5
    h: 8899000c3172
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r5
    h: 8899000c3172
  review: drafted
  review_note: 'support check: partial - No action needed is stated, but auto-clearing is not explicitly
    stated.'
- claim_id: c5
  rel: applies_to
  target: prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r5
    h: 8899000c3172
  review: drafted
---
