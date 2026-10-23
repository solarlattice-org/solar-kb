---
id: fc:solis-s6-eh2p-l-us-fanalarm
type: FaultCode
name: Solis S6-EH2P Fan Alarm
aliases:
- Fan Alarm
- fanalarm
- Solis Fan Alarm
- Fan alarm
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: Fan Alarm
code_key: fanalarm
display_message: Fan alarm
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r5
    h: e40e27f5f9bb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r5
    h: e40e27f5f9bb
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r5
    h: e40e27f5f9bb
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r5
    h: e40e27f5f9bb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r5
    h: e40e27f5f9bb
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r5
    h: e40e27f5f9bb
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r5
    h: e40e27f5f9bb
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r5
    h: e40e27f5f9bb
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r5
    h: e40e27f5f9bb
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r5
    h: e40e27f5f9bb
  review: drafted
---
