---
id: fc:sma-stp-x-us-50-404
type: FaultCode
name: SMA STP-X-US 404
aliases:
- '404'
- SMA 404
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '404'
code_key: '404'
display_message: Grid incident
page: 81
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.8
    h: 919ac480c742
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h407
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h229
    h: f714a156b3c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h474
    h: f714a156b3c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h408
    h: f714a156b3c4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-instability
  note: Very large or too fast change of grid frequency.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r1
    h: af5b72b20eed
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h229
    h: f714a156b3c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h474
    h: f714a156b3c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h408
    h: f714a156b3c4
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h230
    h: a59ad34e5713
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h475
    h: a59ad34e5713
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h409
    h: a59ad34e5713
  review: drafted
  review_note: 'support check: partial - The passages only mention checking for frequency fluctuations,
    and the detection method is implied rather than stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: Contact grid operator if an outage or grid work is suspected.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h230
    h: a59ad34e5713
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h475
    h: a59ad34e5713
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h409
    h: a59ad34e5713
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r3
    h: 9b5f0abed84a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h229
    h: f714a156b3c4
  review: drafted
  review_note: 'support check: partial - It is called a grid fault where the inverter stopped feeding
    in, which is a trip; a fault classification is…'
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r3
    h: 9b5f0abed84a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h229
    h: f714a156b3c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h474
    h: f714a156b3c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h408
    h: f714a156b3c4
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects after grid monitoring time; depending on parameterization may need manual acknowledgement.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r1
    h: af5b72b20eed
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
---
