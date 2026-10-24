---
id: fc:sma-stp-x-us-50-6407
type: FaultCode
name: SMA STP-X-US 6407
aliases:
- '6407'
- SMA 6407
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6407'
code_key: '6407'
display_message: Self-diagnosis > Interference device
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.32
    h: 8f19152722c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h525
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  note: The DC input hardware overcurrent threshold was exceeded.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.32
    h: 8f19152722c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h526
    h: a0526953b5c9
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.32
    h: 8f19152722c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h527
    h: ad7e53985968
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.32
    h: 8f19152722c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h527
    h: ad7e53985968
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the message is permanently present.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.32
    h: 8f19152722c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h527
    h: ad7e53985968
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.32
    h: 8f19152722c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h525
    h: 75f49e9e17fb
  review: drafted
---
