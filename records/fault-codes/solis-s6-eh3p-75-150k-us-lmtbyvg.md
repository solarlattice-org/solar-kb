---
id: fc:solis-s6-eh3p-75-150k-us-lmtbyvg
type: FaultCode
name: Solis S6-EH3P75-150K LmtByVg
aliases:
- LmtByVg
- lmtbyvg
- Solis LmtByVg
- The device is in the Volt-Watt mode
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: LmtByVg
code_key: lmtbyvg
display_message: The device is in the Volt-Watt mode
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r6
    h: 3183d09b9801
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r6
    h: 5750320b131a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r6
    h: 3183d09b9801
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r6
    h: 3183d09b9801
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only if the mode was enabled by factory test error.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=17.r6
    h: 5750320b131a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=25.r6
    h: 3183d09b9801
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r6
    h: 3183d09b9801
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:solis-s6-eh3p-75-150k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=26.r6
    h: 3183d09b9801
  review: drafted
---
