---
id: fc:solis-s6-eh3p-30-60k-us-ovbush
type: FaultCode
name: Solis S6-EH3P30-60K OV-BUS-H
aliases:
- OV-BUS-H
- ovbush
- Solis OV-BUS-H
- Battery overvoltage hardware failure / VBUS
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: OV-BUS-H
code_key: ovbush
display_message: Battery overvoltage hardware failure / VBUS
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r15
    h: 967a5dcdb11c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-overvoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:dc-bus-overvoltage
  note: Hardware-detected overvoltage on battery or bus.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:battery-connection-check
  note: Includes checking battery breaker state and battery damage.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  review: drafted
  review_note: 'support check: partial - Described as a ''hardware failure'' but the row doesn''t state
    device behavior; fault is only implied.'
---
