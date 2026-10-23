---
id: fc:solis-s6-gu-ehv-us-ovdcbi
type: FaultCode
name: Solis S6-GU OV-DCB-I
aliases:
- OV-DCB-I
- ovdcbi
- Solis OV-DCB-I
- DC1 average overcurrent
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: OV-DCB-I
code_key: ovdcbi
display_message: DC1 average overcurrent
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r5
    h: 28e6c9b8fdb2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r15
    h: d90fbe003f50
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r15
    h: c62c8a4dce48
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r15
    h: c62c8a4dce48
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r5
    h: 28e6c9b8fdb2
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r5
    h: 28e6c9b8fdb2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r15
    h: d90fbe003f50
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r5
    h: 28e6c9b8fdb2
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r5
    h: 28e6c9b8fdb2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r15
    h: d90fbe003f50
  review: drafted
  review_note: 'support check: partial - Rows do not explicitly classify it as a fault; the classification
    is only loosely implied.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; replace inverter if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r5
    h: 28e6c9b8fdb2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r15
    h: d90fbe003f50
  review: drafted
  review_note: 'support check: partial - Restart then replace is stated, but not manual reset clearing.'
---
