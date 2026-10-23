---
id: fc:sma-shp-peak3-501
type: FaultCode
name: SMA PEAK3-US 501
aliases:
- '501'
- SMA 501
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '501'
code_key: '501'
display_message: Grid incident
page: 60
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.1
    h: b63afb31b862
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h279
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h162
    h: bd3d762be238
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h247
    h: bd3d762be238
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h182
    h: 72c8aa2a8079
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r4
    h: 5c74c3dbfd51
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h233
    h: 272c39d1e1c3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h479
    h: 272c39d1e1c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h413
    h: 272c39d1e1c3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h280
    h: 272c39d1e1c3
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h162
    h: bd3d762be238
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h247
    h: bd3d762be238
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h182
    h: 72c8aa2a8079
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h233
    h: 272c39d1e1c3
  review: drafted
  review_note: 'support check: partial - Passages call it a ''Grid fault'' and the inverter disconnects,
    but there is no explicit fault classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h162
    h: bd3d762be238
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h247
    h: bd3d762be238
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h182
    h: 72c8aa2a8079
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r4
    h: 5c74c3dbfd51
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h233
    h: 272c39d1e1c3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h479
    h: 272c39d1e1c3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h413
    h: 272c39d1e1c3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h280
    h: 272c39d1e1c3
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h246
    h: 56143efbc9dc
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h163
    h: 56143efbc9dc
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h248
    h: 56143efbc9dc
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h183
    h: b7762bd72e17
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r4
    h: 5c74c3dbfd51
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h234
    h: 3f810abc1c00
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h480
    h: '371272301941'
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h414
    h: bdff814344f6
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h281
    h: '371272301941'
  review: drafted
  review_note: 'support check: partial - Passages say frequency is out of range but don''t explicitly
    state detection by grid frequency measurement; it is only implied.'
- claim_id: c6
  rel: mitigated_by
  target: mit:utility-consultation
  note: When fluctuations and the message occur frequently.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h246
    h: 56143efbc9dc
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h163
    h: 56143efbc9dc
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h248
    h: 56143efbc9dc
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h183
    h: b7762bd72e17
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r4
    h: 5c74c3dbfd51
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h234
    h: 3f810abc1c00
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h480
    h: '371272301941'
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h414
    h: bdff814344f6
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h281
    h: '371272301941'
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only with grid operator approval, coordinated with service.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h246
    h: 56143efbc9dc
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h163
    h: 56143efbc9dc
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h248
    h: 56143efbc9dc
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h183
    h: b7762bd72e17
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r4
    h: 5c74c3dbfd51
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h234
    h: 3f810abc1c00
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h480
    h: '371272301941'
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h414
    h: bdff814344f6
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h281
    h: '371272301941'
  review: drafted
---
