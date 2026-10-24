---
id: fc:sma-shp-peak3-3701
type: FaultCode
name: SMA PEAK3-US 3701
aliases:
- '3701'
- SMA 3701
- Residual current too high > Check generator
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '3701'
code_key: '3701'
display_message: Residual current too high > Check generator
page: 63
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.11
    h: 027b88b7d817
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h329
    h: 073e91a4217c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r1
    h: a1fc2477c9ae
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r1
    h: a1fc2477c9ae
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r1
    h: 3287c94f0288
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h210
    h: dba4882bde4c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h285
    h: 9e1658bb50c5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r1
    h: a1fc2477c9ae
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r1
    h: a1fc2477c9ae
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r1
    h: 3287c94f0288
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h210
    h: dba4882bde4c
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: drafted
  review_note: 'support check: partial - IR camera is mentioned only as a tip for support, not as a definite
    detection method.'
- claim_id: c9
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r1
    h: 3287c94f0288
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h286
    h: 3450f514b95f
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h573
    h: 0818fdbe4234
  review: drafted
- claim_id: c11
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h466
    h: ceee8640eb7c
  review: drafted
  review_note: 'support check: partial - Describes an insulation error with auto reconnect; fault class
    is only loosely implied, not stated.'
- claim_id: c12
  rel: has_production_effect
  target: ec:trip
  note: Momentary insulation error; inverter disconnects and reconnects.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h466
    h: ceee8640eb7c
  review: drafted
  review_note: 'support check: partial - The inverter reconnects implying it disconnected, but disconnecting
    is not explicitly stated.'
- claim_id: c13
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects once values return to permissible range.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h466
    h: ceee8640eb7c
  review: drafted
- claim_id: c14
  rel: applies_to
  target: prod:sma-shp-peak3
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.11
    h: 027b88b7d817
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h329
    h: 073e91a4217c
  review: drafted
---
