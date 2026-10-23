---
id: fc:sma-shp-peak3-503
type: FaultCode
name: SMA PEAK3-US 0503
aliases:
- '0503'
- '503'
- SMA 0503
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '0503'
code_key: '503'
display_message: Grid incident
page: 60
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.3
    h: 3b2cd378567a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h289
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r3
    h: 14fa443485b6
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h291
    h: '371272301941'
  review: drafted
  review_note: 'support check: partial - Passage advises checking grid frequency, but it''s for a different
    message (u31) and doesn''t state detection by frequency measurement; the…'
- claim_id: c4
  rel: mitigated_by
  target: mit:external-fuse-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r3
    h: 14fa443485b6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: When frequency fluctuations occur frequently.
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h291
    h: '371272301941'
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only with grid operator approval, coordinated with Service.
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h291
    h: '371272301941'
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h290
    h: 272c39d1e1c3
  review: drafted
  review_note: 'support check: partial - Disconnection from grid is stated but no explicit fault classification.'
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h290
    h: 272c39d1e1c3
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r3
    h: 14fa443485b6
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Reconnection after grid monitoring implies auto-reset, but manual
    acknowledgment may be required depending on parameterization.'
---
