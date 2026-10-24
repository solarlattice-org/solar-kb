---
id: fc:solis-s6-eh2p-l-us-canfail
type: FaultCode
name: Solis S6-EH2P CAN Fail
aliases:
- CAN Fail
- canfail
- Solis CAN Fail
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: CAN Fail
code_key: canfail
display_message: CAN Fail
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r2
    h: c166314b1746
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  note: Between inverter and battery
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r2
    h: c166314b1746
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r2
    h: c166314b1746
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r2
    h: c166314b1746
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r2
    h: c166314b1746
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r2
    h: c166314b1746
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r2
    h: c166314b1746
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r2
    h: c166314b1746
  review: drafted
---
