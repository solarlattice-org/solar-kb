---
id: fc:solis-s6-gc-us-gphase
type: FaultCode
name: Solis S6-GC G-PHASE
aliases:
- G-PHASE
- gphase
- Solis G-PHASE
- Unbalanced Grid
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: G-PHASE
code_key: gphase
display_message: Unbalanced Grid
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r3
    h: 07886c415962
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r6
    h: 108a713179c9
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r6
    h: 108a713179c9
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:phase-current-measurement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r3
    h: 07886c415962
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r6
    h: 108a713179c9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r6
    h: 108a713179c9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r6
    h: 108a713179c9
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; then verify phase currents and grid connection.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r3
    h: 07886c415962
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r3
    h: 07886c415962
  review: drafted
  review_note: 'support check: partial - Restart first then measure currents and check connection is listed,
    but clearing by manual reset is not stated explicitly.'
---
