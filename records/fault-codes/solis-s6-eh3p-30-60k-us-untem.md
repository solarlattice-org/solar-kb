---
id: fc:solis-s6-eh3p-30-60k-us-untem
type: FaultCode
name: Solis S6-EH3P30-60K UN-TEM
aliases:
- UN-TEM
- untem
- Solis UN-TEM
- Low temperature protection
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: UN-TEM
code_key: untem
display_message: Low temperature protection
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r5
    h: f856e6035573
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r5
    h: f856e6035573
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-undertemperature
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r5
    h: b905f83f77d1
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r5
    h: b905f83f77d1
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r5
    h: f856e6035573
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r4
    h: f856e6035573
  review: drafted
  review_note: 'support check: partial - Checking ambient temperature is a troubleshooting step, not stated
    as how the alarm is detected.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r5
    h: b905f83f77d1
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r8
    h: 28b66038f06a
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Check ambient temperature, then restart; replace inverter if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r8
    h: 28b66038f06a
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r5
    h: b905f83f77d1
  review: drafted
---
