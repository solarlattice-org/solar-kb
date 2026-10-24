---
id: fc:chint-sca-50-100k-t-warn50
type: FaultCode
name: CPS SCA50-100K-T Warn0050
aliases:
- Warn0050
- warn50
- CPS Warn0050
- Temp Sensor Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Warn0050
code_key: warn50
display_message: Temp Sensor Abn
vendor_severity: Warning
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r3
    h: 484e3858d5c4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r3
    h: 484e3858d5c4
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r3
    h: 484e3858d5c4
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r4
    h: 293b6da87375
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r3
    h: 484e3858d5c4
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r4
    h: 293b6da87375
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:inverter-display-check
  note: Check the displayed temperature reading
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r4
    h: 293b6da87375
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r3
    h: 92744a5bbe83
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r4
    h: 1a288429d4be
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r4
    h: d151d754f8e6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r4
    h: 293b6da87375
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r4
    h: 293b6da87375
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r3
    h: 92744a5bbe83
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r4
    h: 1a288429d4be
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r4
    h: d151d754f8e6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r4
    h: 293b6da87375
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Reboot by power cycling the supply; contact service if it persists
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r4
    h: 293b6da87375
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r3
    h: 92744a5bbe83
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r4
    h: 1a288429d4be
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r4
    h: d151d754f8e6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r4
    h: 293b6da87375
  review: drafted
  review_note: 'support check: partial - A manual power-cycle reboot is recommended, but the passages
    don''t state that it clears the warning; u31 also mentions automatic elimination.'
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r3
    h: 484e3858d5c4
  review: drafted
---
