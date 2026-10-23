---
id: fc:sma-stp-x-us-50-6406
type: FaultCode
name: SMA STP-X-US 6406
aliases:
- '6406'
- SMA 6406
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6406'
code_key: '6406'
display_message: Self-diagnosis > Interference device
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h520
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  note: Current at input A exceeds the specified maximum.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h521
    h: 0fb28072e8bd
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h522
    h: a1d43f878551
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h522
    h: a1d43f878551
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h522
    h: a1d43f878551
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h522
    h: a1d43f878551
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h522
    h: a1d43f878551
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the event persists after successful checks.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.31
    h: 21b255574630
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h522
    h: a1d43f878551
  review: drafted
---
