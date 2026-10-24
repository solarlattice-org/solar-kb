---
id: fc:solis-s6-eh2p-l-us-ovdc02
type: FaultCode
name: Solis S6-EH2P OV-DC02
aliases:
- OV-DC02
- ovdc02
- Solis OV-DC02
- DC 2 input overvoltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: OV-DC02
code_key: ovdc02
display_message: DC 2 input overvoltage
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r7
    h: 9f0f16415f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r7
    h: 9f0f16415f68
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r7
    h: 9f0f16415f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r7
    h: 9f0f16415f68
  review: drafted
  review_note: 'support check: partial - The passages say to check PV voltage, which implies PV input,
    but the PV array is not named.'
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r7
    h: 9f0f16415f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r7
    h: 9f0f16415f68
  review: drafted
  review_note: 'support check: partial - The passages say to check whether PV voltage is abnormal, but
    do not name DC voltage measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r7
    h: 9f0f16415f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r7
    h: 9f0f16415f68
  review: drafted
  review_note: 'support check: partial - Restart is suggested only to confirm whether the fault continues,
    not as a mitigation.'
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r7
    h: 9f0f16415f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r7
    h: 9f0f16415f68
  review: drafted
  review_note: 'support check: partial - Row describes an overvoltage fault with restart advice, but doesn''t
    explicitly classify it as fault vs warning; fault is plausible…'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Check PV voltage first, then restart; persistence after restart is checked.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r7
    h: 9f0f16415f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r7
    h: 9f0f16415f68
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r7
    h: 8a31f6a124c8
  review: drafted
---
