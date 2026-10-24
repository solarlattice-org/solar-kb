---
id: fc:sma-sb-us-41-9034
type: FaultCode
name: SMA SB-US-41 9034
aliases:
- '9034'
- SMA 9034
- Error in the rapid shutdown system
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '9034'
code_key: '9034'
display_message: Error in the rapid shutdown system
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.66
    h: d9920f98dbb5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h434
    h: a3877c085030
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-stp-us-41-sb-us-41-event-9034
  cite:
  - src: src:sma-kb-stp-us-41-sb-us-41-event-9034
    loc: sec=h1
    h: 1ed454275821
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:rapid-shutdown-failure
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r2
    h: 7e25a82051cf
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h435
    h: 0f9623b7f0ff
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r2
    h: 7e25a82051cf
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h435
    h: 0f9623b7f0ff
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Standby voltage of switches per string must be below 30 V.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h436
    h: ab549348ae54
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h744
    h: ab549348ae54
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h628
    h: ab549348ae54
  review: drafted
  review_note: 'support check: partial - The passages say to check the switches'' standby voltage is below
    30 V, but they don''t name DC voltage measurement…'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Rapid shutdown mode must match the DC disconnection unit used.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h436
    h: ab549348ae54
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h744
    h: ab549348ae54
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h628
    h: ab549348ae54
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:pv-switch-function-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h436
    h: ab549348ae54
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h744
    h: ab549348ae54
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h628
    h: ab549348ae54
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.66
    h: d9920f98dbb5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h434
    h: a3877c085030
  - src: src:sma-kb-stp-us-41-sb-us-41-event-9034
    loc: sec=h1
    h: 1ed454275821
  review: drafted
---
