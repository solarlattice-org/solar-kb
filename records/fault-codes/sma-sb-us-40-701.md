---
id: fc:sma-sb-us-40-701
type: FaultCode
name: SMA SB-US-40 701
aliases:
- '701'
- SMA 701
- Frq. not permitted > Check parameter
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '701'
code_key: '701'
display_message: Frq. not permitted > Check parameter
page: 48
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h187
    h: 1b7a4d540c92
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h188
    h: 7931737921cb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h188
    h: 7931737921cb
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h241
    h: 272c39d1e1c3
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r2
    h: 8700c90cd6e3
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h188
    h: 7931737921cb
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h241
    h: 272c39d1e1c3
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h188
    h: 7931737921cb
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h241
    h: 272c39d1e1c3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h494
    h: 272c39d1e1c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h428
    h: 272c39d1e1c3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h305
    h: 272c39d1e1c3
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h189
    h: b7762bd72e17
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h242
    h: c704af31bf5e
  review: drafted
  review_note: 'support check: partial - Corrective measures involve checking grid frequency, but detection
    by frequency measurement is only implied.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h242
    h: c704af31bf5e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h495
    h: c704af31bf5e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h429
    h: c704af31bf5e
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h306
    h: c704af31bf5e
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When frequency fluctuations and this message occur often.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h189
    h: b7762bd72e17
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h242
    h: c704af31bf5e
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only with grid operator approval, coordinated with manufacturer service.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h189
    h: b7762bd72e17
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h242
    h: c704af31bf5e
  review: drafted
---
