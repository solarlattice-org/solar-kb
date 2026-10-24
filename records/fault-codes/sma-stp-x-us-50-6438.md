---
id: fc:sma-stp-x-us-50-6438
type: FaultCode
name: SMA STP-X-US 6438
aliases:
- '6438'
- SMA 6438
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6438'
code_key: '6438'
display_message: Self-diagnosis > Interference device
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h535
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Operating conditions for the internal AC converter stage were not met.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h535
    h: 75f49e9e17fb
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h536
    h: 3bb42b45fcd1
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h536
    h: 3bb42b45fcd1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h537
    h: 2b783c31e6c7
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h536
    h: 3bb42b45fcd1
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h536
    h: 3bb42b45fcd1
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: 'Applies when the event is frequent or permanent: disconnect and recommission; replace the inverter
    if it persists.'
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h536
    h: 3bb42b45fcd1
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h537
    h: 2b783c31e6c7
  review: drafted
  review_note: 'support check: partial - Disconnect and recommission is an operator action implying manual
    reset, but not explicitly stated as clearing.'
- claim_id: c8
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h537
    h: 2b783c31e6c7
  review: drafted
  review_note: 'support check: partial - Mains voltage check is a corrective measure rather than a detection
    method.'
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h537
    h: 2b783c31e6c7
  review: drafted
  review_note: 'support check: partial - The corrective measures amount to disconnecting, waiting for
    LEDs to go out and recommissioning, which is roughly a restart, but…'
- claim_id: c10
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the event persists or the relays do not switch.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h537
    h: 2b783c31e6c7
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.34
    h: 13035cbe4ca6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h535
    h: 75f49e9e17fb
  review: drafted
---
