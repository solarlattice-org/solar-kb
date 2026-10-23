---
id: fc:sma-sb-us-41-3401
type: FaultCode
name: SMA SB-US-41 3401
aliases:
- '3401'
- SMA 3401
- DC overvoltage > Disconnect generator
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3401'
code_key: '3401'
display_message: DC overvoltage > Disconnect generator
page: 57
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.20
    h: 58a42ec91edb
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h264
    h: 41676f7fb1bd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h175
    h: 587cea85589b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h264
    h: 41676f7fb1bd
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h265
    h: f9c84c143221
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h533
    h: 7acd25259cf5
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h534
    h: 55dc6331d266
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h259
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h176
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h266
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h535
    h: b3b29436b48d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h259
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h176
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h266
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h535
    h: b3b29436b48d
  review: drafted
  review_note: 'support check: partial - Corrective steps compare DC voltage with max input voltage, but
    detection method isn''t explicitly stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:safety-isolation
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h259
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h176
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h266
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h535
    h: b3b29436b48d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-voltage-margin-design
  note: When DC voltage exceeds the maximum inverter input voltage.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h259
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h176
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h266
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h535
    h: b3b29436b48d
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  note: Overvoltage can destroy the inverter; immediate intervention required.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h175
    h: 587cea85589b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h265
    h: f9c84c143221
  review: drafted
  review_note: 'support check: partial - Disconnect/destroy language implies a fault needing intervention,
    but ''Fault'' classification isn''t explicitly stated.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Operator disconnects and reconnects DC after voltage check; service if the message repeats frequently.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h259
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h176
    h: 5bf6ccea6e5e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  review: drafted
  review_note: 'support check: partial - Operator disconnect/reconnect and service steps are present,
    but passages don''t state that it clears by manual reset.'
---
