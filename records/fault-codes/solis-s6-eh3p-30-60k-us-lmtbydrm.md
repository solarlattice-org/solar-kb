---
id: fc:solis-s6-eh3p-30-60k-us-lmtbydrm
type: FaultCode
name: Solis S6-EH3P30-60K LmtByDRM
aliases:
- LmtByDRM
- lmtbydrm
- Solis LmtByDRM
- DRM Function ON
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: LmtByDRM
code_key: lmtbydrm
display_message: DRM Function ON
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r3
    h: 260fe9806c06
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=25.r3
    h: 260fe9806c06
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r3
    h: 260fe9806c06
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r3
    h: 260fe9806c06
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r3
    h: 260fe9806c06
  review: drafted
  review_note: 'support check: partial - DRM function ON implies a demand-response limit, but power limiting
    is not explicitly stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r3
    h: 260fe9806c06
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r3
    h: 260fe9806c06
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r3
    h: 260fe9806c06
  review: drafted
  review_note: 'support check: partial - Name ''LmtBy'' suggests limiting but the row doesn''t explicitly
    state reduced output.'
- claim_id: c5
  rel: applies_to
  target: prod:solis-s6-eh3p-30-60k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r3
    h: 260fe9806c06
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=25.r3
    h: 260fe9806c06
  review: drafted
---
