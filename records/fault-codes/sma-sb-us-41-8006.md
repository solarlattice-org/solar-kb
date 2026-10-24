---
id: fc:sma-sb-us-41-8006
type: FaultCode
name: SMA SB-US-41 8006
aliases:
- '8006'
- SMA 8006
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '8006'
code_key: '8006'
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-kb-sbx-x-1sp-us-41-event-8006-string-x-is-in-derating-mode
  cite:
  - src: src:sma-kb-sbx-x-1sp-us-41-event-8006-string-x-is-in-derating-mode
    loc: sec=h1
    h: 2b63d5211f3b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  note: 'At least one string leaves MPP tracking whenever output is limited: current limit, nominal power,
    temperature, grid condition or setpoint.'
  cite:
  - src: src:sma-kb-sbx-x-1sp-us-41-event-8006-string-x-is-in-derating-mode
    loc: sec=h1
    h: 2b63d5211f3b
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: No single limit value is given; 10 A string current is a trigger, not an output limit.
  cite:
  - src: src:sma-kb-sbx-x-1sp-us-41-event-8006-string-x-is-in-derating-mode
    loc: sec=h1
    h: 2b63d5211f3b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  note: The event only shows an existing operating state; inverter behaviour is unchanged by the firmware
    that added it.
  cite:
  - src: src:sma-kb-sbx-x-1sp-us-41-event-8006-string-x-is-in-derating-mode
    loc: sec=h1
    h: 2b63d5211f3b
  review: drafted
  review_note: 'support check: partial - The article says the event only displays an existing operating
    state and the behavior is unchanged by the firmware, but…'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-kb-sbx-x-1sp-us-41-event-8006-string-x-is-in-derating-mode
    loc: sec=h1
    h: 2b63d5211f3b
  review: drafted
---
