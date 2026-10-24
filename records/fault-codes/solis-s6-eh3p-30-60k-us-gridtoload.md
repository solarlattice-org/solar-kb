---
id: fc:solis-s6-eh3p-30-60k-us-gridtoload
type: FaultCode
name: Solis S6-EH3P30-60K GridToLoad
aliases:
- GridToLoad
- gridtoload
- Solis GridToLoad
- Grid to load
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: GridToLoad
code_key: gridtoload
display_message: Grid to load
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r11
    h: 2b2a678c83b7
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=25.r11
    h: 2b2a678c83b7
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: Status message; manual says no action needed.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r11
    h: 2b2a678c83b7
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r11
    h: 2b2a678c83b7
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r11
    h: 2b2a678c83b7
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r11
    h: 2b2a678c83b7
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r11
    h: 2b2a678c83b7
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r11
    h: 2b2a678c83b7
  review: drafted
  review_note: 'review: partial - The row only says ''No need to deal with it''; it never says production
    is unaffected, so ''no production effect'' is implied…'
- claim_id: c5
  rel: applies_to
  target: prod:solis-s6-eh3p-30-60k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r11
    h: 2b2a678c83b7
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=25.r11
    h: 2b2a678c83b7
  review: drafted
---
