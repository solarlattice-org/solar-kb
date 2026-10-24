---
id: fc:sma-stp-core1-us-9034
type: FaultCode
name: SMA CORE1-US 9034
aliases:
- '9034'
- SMA 9034
- Error in Rapid Shutdown System
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9034'
code_key: '9034'
display_message: Error in Rapid Shutdown System
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r2
    h: 7e25a82051cf
  review: drafted
- claim_id: c4
  rel: defined_in
  target: src:sma-kb-stp-us-41-sb-us-41-event-9034
  cite:
  - src: src:sma-kb-stp-us-41-sb-us-41-event-9034
    loc: sec=h1
    h: 1ed454275821
  review: drafted
- claim_id: c5
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
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
- claim_id: c10
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r2
    h: 7e25a82051cf
  - src: src:sma-kb-stp-us-41-sb-us-41-event-9034
    loc: sec=h1
    h: 1ed454275821
  review: drafted
---
