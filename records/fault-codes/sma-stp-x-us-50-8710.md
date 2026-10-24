---
id: fc:sma-stp-x-us-50-8710
type: FaultCode
name: SMA STP-X-US 8710
aliases:
- '8710'
- SMA 8710
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '8710'
code_key: '8710'
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.48
    h: dcc23644ddc0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  note: Timeout of displacement power factor setpoint from system control
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r4
    h: 12e2adb99b2d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h728
    h: f59e6f293bb9
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h729
    h: f532e08430b1
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h602
    h: f59e6f293bb9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h603
    h: f532e08430b1
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h435
    h: f59e6f293bb9
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h436
    h: f532e08430b1
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r4
    h: 12e2adb99b2d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h730
    h: 800a134e3dfa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h604
    h: 800a134e3dfa
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h437
    h: 800a134e3dfa
  review: drafted
  review_note: 'support check: partial - Cable check is stated, but a network cable is not explicitly
    named as affected.'
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r4
    h: 12e2adb99b2d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h730
    h: 800a134e3dfa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h604
    h: 800a134e3dfa
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h437
    h: 800a134e3dfa
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: Feed-in continues with last received or configured fall-back power factor
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r4
    h: 12e2adb99b2d
  review: drafted
  review_note: 'support check: partial - Last values retained or fallback value is set, which implies
    operation continues, but no feed-in or production effect is stated.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.48
    h: dcc23644ddc0
  review: drafted
---
