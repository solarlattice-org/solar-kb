---
id: fc:sma-sb-us-41-1001
type: FaultCode
name: SMA SB-US-41 1001
aliases:
- '1001'
- SMA 1001
- L / N swapped
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '1001'
code_key: '1001'
display_message: L / N swapped
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.15
    h: 4a20eb0e64ec
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h244
    h: 794ff9de1b02
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-polarity-reversed
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h191
    h: adf6db4a4ed9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h244
    h: 794ff9de1b02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h503
    h: 794ff9de1b02
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h432
    h: 794ff9de1b02
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:inverter-installation-defect
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h245
    h: 9e2dcc04eff8
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h504
    h: 9e2dcc04eff8
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h433
    h: 9e2dcc04eff8
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h246
    h: 4099f25892c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h505
    h: 4099f25892c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h434
    h: 4099f25892c4
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h246
    h: 4099f25892c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h505
    h: 4099f25892c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h434
    h: 4099f25892c4
  review: drafted
  review_note: 'support check: partial - The passages say to check AC voltages at the inverter connection,
    which is a corrective step; they don''t say the…'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Escalate to manufacturer service if the message persists after wiring check.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h192
    h: d39e62db4d56
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h246
    h: 4099f25892c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h505
    h: 4099f25892c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h434
    h: 4099f25892c4
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.15
    h: 4a20eb0e64ec
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h244
    h: 794ff9de1b02
  review: drafted
---
