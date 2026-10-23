---
id: fc:sma-sbse-us-50-9034
type: FaultCode
name: SMA SBSE-US-50 9034
aliases:
- '9034'
- SMA 9034
- Error in the rapid shutdown system
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9034'
code_key: '9034'
display_message: Error in the rapid shutdown system
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.66
    h: e4c50c813897
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h742
    h: a3877c085030
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
