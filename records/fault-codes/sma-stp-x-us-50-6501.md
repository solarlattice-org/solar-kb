---
id: fc:sma-stp-x-us-50-6501
type: FaultCode
name: SMA STP-X-US 6501
aliases:
- '6501'
- SMA 6501
- Self-diagnosis > Overtemperature
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6501'
code_key: '6501'
display_message: Self-diagnosis > Overtemperature
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.35
    h: eda105775f27
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h540
    h: 359fae7aa468
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r17
    h: 1fde1d857c34
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h622
    h: abc29332332d
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h541
    h: abc29332332d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h340
    h: abc29332332d
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h622
    h: abc29332332d
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h541
    h: abc29332332d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h340
    h: abc29332332d
  review: drafted
  review_note: 'support check: partial - Inverter switches off, but nothing explicitly classes it as a
    fault vs. warning; switching off implies fault loosely.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h622
    h: abc29332332d
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h541
    h: abc29332332d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h340
    h: abc29332332d
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r17
    h: 1fde1d857c34
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r17
    h: 1fde1d857c34
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h623
    h: 7ab490300d63
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h542
    h: 1b4c87768301
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h341
    h: 1b4c87768301
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r17
    h: 1fde1d857c34
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h623
    h: 7ab490300d63
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h542
    h: 1b4c87768301
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h341
    h: 1b4c87768301
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h623
    h: 7ab490300d63
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h542
    h: 1b4c87768301
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h341
    h: 1b4c87768301
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h542
    h: 1b4c87768301
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h341
    h: 1b4c87768301
  review: drafted
---
