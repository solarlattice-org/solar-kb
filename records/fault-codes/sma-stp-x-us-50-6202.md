---
id: fc:sma-stp-x-us-50-6202
type: FaultCode
name: SMA STP-X-US 6202
aliases:
- '6202'
- SMA 6202
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6202'
code_key: '6202'
display_message: Self-diagnosis > Interference device
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.27
    h: 5d7348a30f7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h500
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.27
    h: 5d7348a30f7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h500
    h: 75f49e9e17fb
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h501
    h: 4b31f3312359
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:residual-current-monitor
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.27
    h: 5d7348a30f7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h501
    h: 4b31f3312359
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.27
    h: 5d7348a30f7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h501
    h: 4b31f3312359
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.27
    h: 5d7348a30f7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h501
    h: 4b31f3312359
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the message is permanently present.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.27
    h: 5d7348a30f7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h502
    h: ee6a063b5fe4
  review: drafted
---
