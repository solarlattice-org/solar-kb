---
id: fc:solis-s6-eh2p-l-us-gridintf02
type: FaultCode
name: Solis S6-EH2P GRID-INTF02
aliases:
- GRID-INTF02
- gridintf02
- Solis GRID-INTF02
- Power grid disturbance 02
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: GRID-INTF02
code_key: gridintf02
display_message: Power grid disturbance 02
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r14
    h: 63b884f60708
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-interference
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r14
    h: 63b884f60708
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r14
    h: 0bde6f54f888
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r13
    h: 0bde6f54f888
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r14
    h: 63b884f60708
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r14
    h: 0bde6f54f888
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r13
    h: 0bde6f54f888
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:waveform-spectrum-analysis
  note: Check grid for severe waveform distortion.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r14
    h: 63b884f60708
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r14
    h: 0bde6f54f888
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r13
    h: 0bde6f54f888
  review: drafted
  review_note: 'support check: partial - Confirming whether the grid is seriously distorted is stated,
    but spectrum analysis as a method is not.'
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r14
    h: 63b884f60708
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r14
    h: 0bde6f54f888
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r13
    h: 0bde6f54f888
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r14
    h: 63b884f60708
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r14
    h: 0bde6f54f888
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r13
    h: 0bde6f54f888
  review: drafted
  review_note: 'support check: partial - Described as a ''disturbance'' with no stated device behavior;
    a fault classification is not clearly stated.'
---
