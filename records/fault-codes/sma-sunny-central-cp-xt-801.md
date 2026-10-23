---
id: fc:sma-sunny-central-cp-xt-801
type: FaultCode
name: SMA SC-CP-XT 801
aliases:
- '801'
- SMA 801
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '801'
code_key: '801'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h252
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h169
    h: 0d3c0d95a150
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
  review_note: 'support check: partial - Evidence for grid failure/line conductor failure appears under
    0801 row, but the u2 text is about AC cable/country data; grid…'
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h252
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h253
    h: 5027c6815068
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h169
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h170
    h: 5027c6815068
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h253
    h: 5027c6815068
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h170
    h: 5027c6815068
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r7
    h: b36691fd426f
  review: drafted
  review_note: 'support check: partial - Grid voltage checks are instructed, but detection by grid voltage
    measurement isn''t explicitly stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h253
    h: 5027c6815068
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h170
    h: 5027c6815068
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Applies when the country data set is misconfigured.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h253
    h: 5027c6815068
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h170
    h: 5027c6815068
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When grid voltage is permanently outside the permitted range; service if the message persists
    otherwise.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h253
    h: 5027c6815068
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h170
    h: 5027c6815068
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  note: Inverter waits for grid voltage and does not feed in.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h252
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h169
    h: 0d3c0d95a150
  review: drafted
  review_note: 'support check: partial - Evidence says ''waiting for grid voltage'' but doesn''t explicitly
    state it stops feed-in/trips.'
---
