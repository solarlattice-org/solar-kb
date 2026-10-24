---
id: fc:solis-s6-gu-ehv-us-gfflu
type: FaultCode
name: Solis S6-GU G-F-FLU
aliases:
- G-F-FLU
- gfflu
- Solis G-F-FLU
- Grid frequency fluctuat ion
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: G-F-FLU
code_key: gfflu
display_message: Grid frequency fluctuat ion
page: 48
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r4
    h: a0c22a49aae0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r4
    h: a0c22a49aae0
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r4
    h: a0c22a49aae0
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r4
    h: a0c22a49aae0
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r4
    h: a0c22a49aae0
  review: drafted
  review_note: 'support check: partial - Monitoring grid frequency variations is suggested, but a detection
    method is not explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r4
    h: a0c22a49aae0
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r4
    h: a0c22a49aae0
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; then monitor grid frequency variations.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r4
    h: a0c22a49aae0
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r4
    h: a0c22a49aae0
  review: drafted
  review_note: 'support check: partial - Restart then monitor frequency is listed, but clearing by manual
    reset is not stated.'
- claim_id: c6
  rel: applies_to
  target: prod:solis-s6-gu-ehv-us
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r4
    h: a0c22a49aae0
  review: drafted
---
