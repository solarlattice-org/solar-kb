---
id: fc:sma-sunny-central-cp-xt-3501
type: FaultCode
name: SMA SC-CP-XT 3501
aliases:
- '3501'
- SMA 3501
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3501'
code_key: '3501'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r1
    h: 82dbfd767650
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h204
    h: 90a2ed93d28f
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r3
    h: 37b0c92512b9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h277
    h: aa84d8588c73
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h559
    h: b4a70384c4fe
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h320
    h: aa84d8588c73
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r1
    h: 82dbfd767650
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h453
    h: ff98adfd21c5
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  note: Defective insulation or faulty plug connections are named as the frequent cause.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h453
    h: ff98adfd21c5
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h204
    h: 90a2ed93d28f
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r3
    h: 37b0c92512b9
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r1
    h: 82dbfd767650
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h560
    h: 8ca40d7d772c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h453
    h: ff98adfd21c5
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h453
    h: ff98adfd21c5
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h454
    h: 736fbc74e526
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h454
    h: 736fbc74e526
  review: drafted
- claim_id: c9
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h454
    h: 736fbc74e526
  review: drafted
  review_note: 'support check: partial - Open-circuit voltage measurement is listed as a verification
    step, but not explicitly as detection of this fault.'
- claim_id: c10
  rel: detected_by
  target: method:dc-voltage-measurement
  note: String pole-to-ground voltage measurement.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h454
    h: 736fbc74e526
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h560
    h: 8ca40d7d772c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h454
    h: 736fbc74e526
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h454
    h: 736fbc74e526
  review: drafted
  review_note: 'support check: partial - IR camera is only a tip for support, not a stated detection method.'
- claim_id: c13
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h262
    h: e4a2a2e70403
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h179
    h: e4a2a2e70403
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h205
    h: 7f7d30d371d5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h278
    h: 3450f514b95f
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h560
    h: 8ca40d7d772c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h321
    h: 3450f514b95f
  review: drafted
- claim_id: c14
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h453
    h: ff98adfd21c5
  - src: src:sma-kb-event-3501-with-sunnyboy-smart-energy-sbse
    loc: sec=h1
    h: 05d7bba15124
  review: drafted
  review_note: 'support check: partial - Inverter disconnects/does not operate, but ''Fault'' classification
    isn''t explicitly stated.'
- claim_id: c15
  rel: has_production_effect
  target: ec:trip
  note: Inverter disconnects from grid or fails to connect during self-test.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h453
    h: ff98adfd21c5
  - src: src:sma-kb-event-3501-with-sunnyboy-smart-energy-sbse
    loc: sec=h1
    h: 05d7bba15124
  review: drafted
---
