---
id: fc:solis-s6-eh2p-l-us-lmtbyunfr
type: FaultCode
name: Solis S6-EH2P LmtByUnFr
aliases:
- LmtByUnFr
- lmtbyunfr
- Solis LmtByUnFr
- Under frequency limit
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: LmtByUnFr
code_key: lmtbyunfr
display_message: Under frequency limit
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r8
    h: c1ae475656c6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r8
    h: c1ae475656c6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r8
    h: c1ae475656c6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r8
    h: c1ae475656c6
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r8
    h: c1ae475656c6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r8
    h: c1ae475656c6
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r8
    h: c1ae475656c6
  review: drafted
---
