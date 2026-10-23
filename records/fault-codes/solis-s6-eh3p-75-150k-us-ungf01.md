---
id: fc:solis-s6-eh3p-75-150k-us-ungf01
type: FaultCode
name: Solis S6-EH3P75-150K UN-G-F01
aliases:
- UN-G-F01
- ungf01
- Solis UN-G-F01
- Grid frequency exceeds the lower frequency range
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: UN-G-F01
code_key: ungf01
display_message: Grid frequency exceeds the lower frequency range
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
  review_note: 'support check: partial - Classification as fault isn''t explicitly stated in the row.'
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
  review_note: 'support check: partial - Frequency range exceedance implies measurement but detection
    method isn''t stated.'
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  note: Restart after grid and cabling checks.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r5
    h: 8f7ad95147b6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r5
    h: 8f7ad95147b6
  review: drafted
---
