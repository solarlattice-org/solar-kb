---
id: fc:sma-stp-x-us-50-6107
type: FaultCode
name: SMA STP-X-US 6107
aliases:
- '6107'
- SMA 6107
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6107'
code_key: '6107'
page: 88
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Internal program state exceeded its allowed duration.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h495
    h: 21b49de0bb18
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h496
    h: a4de091edfda
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h496
    h: a4de091edfda
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h496
    h: a4de091edfda
  - src: src:sma-kb-event-6107-on-stp33-us-41-stp50-us-41-stp62-us-41
    loc: sec=h1
    h: 0276023694aa
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Brief occurrences at dawn or dusk need no action; if permanent, restart, then replace assembly
    or inverter.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h497
    h: 6a2a7f7a4a21
  - src: src:sma-kb-event-6107-on-stp33-us-41-stp50-us-41-stp62-us-41
    loc: sec=h1
    h: 0276023694aa
  review: drafted
  review_note: 'support check: partial - Corrective measures match, but auto-reset is not explicitly stated;
    brief occurrences need no action only implies it.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: When the event follows a parameter change.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h497
    h: 6a2a7f7a4a21
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:sma-kb-event-6107-on-stp33-us-41-stp50-us-41-stp62-us-41
    loc: sec=h1
    h: 0276023694aa
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-restart
  note: When the event is permanently present.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h497
    h: 6a2a7f7a4a21
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the event persists after a restart.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h497
    h: 6a2a7f7a4a21
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: When it persists after a firmware update outside the start-up or sunset periods.
  cite:
  - src: src:sma-kb-event-6107-on-stp33-us-41-stp50-us-41-stp62-us-41
    loc: sec=h1
    h: 0276023694aa
  review: drafted
  review_note: 'support check: partial - Contact service line is stated if it occurs outside start-up/sunset
    after firmware update, but ''persists after update'' is roughly there;…'
- claim_id: c11
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.26
    h: 336e0ccc0f7b
  review: drafted
---
