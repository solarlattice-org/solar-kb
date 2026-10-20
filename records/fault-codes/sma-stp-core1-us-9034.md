---
id: fc:sma-stp-core1-us-9034
type: FaultCode
name: SMA CORE1-US 9034
aliases:
- '9034'
- SMA 9034
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9034'
code_key: '9034'
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
  rel: reports
  target: symptom:rapid-shutdown-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-settings-review
  note: Check rapid shutdown configuration against the disconnection unit used.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  review: drafted
  review_note: 'support check: partial - Check of configuration is stated, but ''detected by'' relation
    and the disconnection unit comparison are only loosely implied.'
---
