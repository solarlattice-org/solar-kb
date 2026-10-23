---
id: fc:solis-s6-eh3p-75-150k-us-standbysynoch
type: FaultCode
name: Solis S6-EH3P75-150K StandbySynoch
aliases:
- StandbySynoch
- standbysynoch
- Solis StandbySynoch
- Off grid status to On grid status
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: StandbySynoch
code_key: standbysynoch
display_message: Off grid status to On grid status
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r10
    h: 3cb0b6a71110
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status message for the off-grid to on-grid transition; no action needed.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r10
    h: 3cb0b6a71110
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r10
    h: 3cb0b6a71110
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r10
    h: 3cb0b6a71110
  review: drafted
---
