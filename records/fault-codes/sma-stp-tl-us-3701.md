---
id: fc:sma-stp-tl-us-3701
type: FaultCode
name: SMA STP-TL-US 3701
aliases:
- '3701'
- SMA 3701
- Resid.curr.too.high > Check generator
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '3701'
code_key: '3701'
display_message: Resid.curr.too.high > Check generator
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r5
    h: 38f49f27de55
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-stp12000-24000tl-us-10-event-number-3701
  cite:
  - src: src:sma-kb-stp12000-24000tl-us-10-event-number-3701
    loc: sec=h1
    h: 4ec59787e34e
  review: drafted
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
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
  target: method:visual-inspection
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.20
    h: 1fc05755d2d4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h467
    h: 10a07fe57d31
  review: drafted
- claim_id: c9
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
- claim_id: c10
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
- claim_id: c11
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
- claim_id: c12
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
- claim_id: c13
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
- claim_id: c14
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
---
