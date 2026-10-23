---
id: fc:solis-s6-eh2p-l-us-gfglu
type: FaultCode
name: Solis S6-EH2P G-F-GLU
aliases:
- G-F-GLU
- gfglu
- Solis G-F-GLU
- Grid voltage frequency f luctuat ion
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: G-F-GLU
code_key: gfglu
display_message: Grid voltage frequency f luctuat ion
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-instability
  note: Grid voltage frequency fluctuation.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r7
    h: e2899bbbbca0
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r7
    h: e2899bbbbca0
  review: drafted
  review_note: 'support check: partial - Classification as fault isn''t explicitly stated in the row.'
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r7
    h: e2899bbbbca0
  review: drafted
  review_note: 'support check: partial - Frequency fluctuation implies frequency monitoring but the detection
    method isn''t stated.'
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r7
    h: e2899bbbbca0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r7
    h: e2899bbbbca0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  note: Restart after grid and cabling checks.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r7
    h: e2899bbbbca0
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r7
    h: e2899bbbbca0
  review: drafted
---
