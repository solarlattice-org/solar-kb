---
id: fc:solis-s6-eh2p-l-us-ovvbatt
type: FaultCode
name: Solis S6-EH2P OV-Vbatt
aliases:
- OV-Vbatt
- ovvbatt
- Solis OV-Vbatt
- Battery undervoltage detected
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: OV-Vbatt
code_key: ovvbatt
display_message: Battery undervoltage detected
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r3
    h: 06c38a9cbc87
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-voltage-out-of-range
  note: Sources disagree on under- versus overvoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r3
    h: 06c38a9cbc87
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r3
    h: 06c38a9cbc87
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r3
    h: 9c503f9f2a3f
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Battery voltage at inverter terminals
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r3
    h: 06c38a9cbc87
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r3
    h: 06c38a9cbc87
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r3
    h: 9c503f9f2a3f
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r3
    h: 06c38a9cbc87
  review: drafted
---
