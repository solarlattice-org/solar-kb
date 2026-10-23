---
id: fc:solis-s6-eh3p-75-150k-us-nobattery
type: FaultCode
name: Solis S6-EH3P75-150K NO-Battery
aliases:
- NO-Battery
- nobattery
- Solis NO-Battery
- Battery is not connected
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: NO-Battery
code_key: nobattery
display_message: Battery is not connected
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r17
    h: 0f7b7bbb6564
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-disconnected
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r14
    h: 51fd3e50efb4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r14
    h: 51fd3e50efb4
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r17
    h: a331cae4fe86
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r17
    h: 0f7b7bbb6564
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r17
    h: 0f7b7bbb6564
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Battery voltage measured at the plug.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r17
    h: a331cae4fe86
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r17
    h: 0f7b7bbb6564
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r17
    h: 0f7b7bbb6564
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:battery-connection-check
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r14
    h: 51fd3e50efb4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r14
    h: 51fd3e50efb4
  review: drafted
---
