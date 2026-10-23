---
id: fc:solis-s6-eh3p-75-150k-us-unbbus
type: FaultCode
name: Solis S6-EH3P75-150K UNB-BUS
aliases:
- UNB-BUS
- unbbus
- Solis UNB-BUS
- DC bus unbalanced voltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: UNB-BUS
code_key: unbbus
display_message: DC bus unbalanced voltage
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r10
    h: 04cf8a3254ae
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-imbalance
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r10
    h: a69d0f7676a1
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r10
    h: 04cf8a3254ae
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r10
    h: 04cf8a3254ae
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r10
    h: a69d0f7676a1
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r10
    h: 04cf8a3254ae
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r10
    h: 04cf8a3254ae
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r10
    h: a69d0f7676a1
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r10
    h: 04cf8a3254ae
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r10
    h: 04cf8a3254ae
  review: drafted
  review_note: 'support check: partial - Fault class not explicit; implied by ''confirm that the fault
    continues''.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r10
    h: a69d0f7676a1
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r10
    h: 04cf8a3254ae
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r10
    h: 04cf8a3254ae
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
