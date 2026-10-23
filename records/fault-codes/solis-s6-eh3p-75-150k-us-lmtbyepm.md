---
id: fc:solis-s6-eh3p-75-150k-us-lmtbyepm
type: FaultCode
name: Solis S6-EH3P75-150K LmtByEPM
aliases:
- LmtByEPM
- lmtbyepm
- Solis LmtByEPM
- The device's output is under cont rol led
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: LmtByEPM
code_key: lmtbyepm
display_message: The device's output is under cont rol led
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r2
    h: a7f800254dbe
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r2
    h: a7f800254dbe
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r2
    h: a7f800254dbe
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r2
    h: a7f800254dbe
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-settings-review
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r2
    h: a7f800254dbe
  review: drafted
  review_note: 'support check: partial - Settings are to be checked/verified, but the passages don''t
    say that reviewing them mitigates the limit.'
- claim_id: c6
  rel: has_production_effect
  target: ec:derate
  note: Output limited by external meter, third-party controller or power-control setting; no number stated.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r2
    h: a7f800254dbe
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r2
    h: a7f800254dbe
  review: drafted
---
