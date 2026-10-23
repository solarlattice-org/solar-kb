---
id: fc:sma-sbse-us-50-9033
type: FaultCode
name: SMA SBSE-US-50 9033
aliases:
- '9033'
- SMA 9033
- Rapid shutdown has been triggered
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9033'
code_key: '9033'
display_message: Rapid shutdown has been triggered
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.65
    h: da224bdfc1a8
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h738
    h: '284843253247'
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:rapid-shutdown
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r7
    h: eaf36c5b0c2a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r7
    h: eaf36c5b0c2a
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r6
    h: 4d079dd65358
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h739
    h: f4280bd32756
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h623
    h: 7bf9fb38dceb
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: AC side disconnected and PV inputs discharged.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r7
    h: eaf36c5b0c2a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r7
    h: eaf36c5b0c2a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h739
    h: f4280bd32756
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h623
    h: 7bf9fb38dceb
  review: drafted
---
