---
id: fc:sma-stp-x-us-50-6401
type: FaultCode
name: SMA STP-X-US 6401
aliases:
- '6401'
- SMA 6401
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6401'
code_key: '6401'
display_message: Self-diagnosis > Interference device
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h505
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h505
    h: 75f49e9e17fb
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h506
    h: ba36534001ef
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:insulation-monitor
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h506
    h: ba36534001ef
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h506
    h: ba36534001ef
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  note: Implied by the inverter reconnecting to the grid afterward.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
  review_note: 'support check: partial - Reconnecting to the grid implies a disconnect, but fault classification
    is not clearly stated; weakly implied.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Implied by the reconnection to the grid.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Single occurrences reconnect within minutes; if recurring, test insulation, isolate the faulty
    string, then replace the inverter.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
  review_note: 'support check: partial - Single occurrences reconnect within minutes (auto-recovery implied),
    and the recurring steps are listed, though no explicit auto-reset wording.'
- claim_id: c8
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
- claim_id: c9
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
  review_note: 'support check: partial - Voltage measurement is mentioned within faulty string tests,
    but as a follow-up step rather than detection.'
- claim_id: c10
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the event persists or recurs after the string is repaired.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.28
    h: f1bf8bafb90e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h507
    h: 90e3985f0ea6
  review: drafted
---
