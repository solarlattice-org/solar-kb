---
id: fc:chint-sca-25ktl-208-warn30
type: FaultCode
name: CPS SCA25KTL-208 Warn0030
aliases:
- Warn0030
- warn30
- CPS Warn0030
- EepromErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Warn0030
code_key: warn30
display_message: EepromErr
vendor_severity: Warning
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r1
    h: a1a7180ea659
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r2
    h: b231add85b97
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r1
    h: a1a7180ea659
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r2
    h: b231add85b97
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:data-storage-failure
  note: Internal memory alarm per EepromErr label; definition only says internal alarm
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r1
    h: a1a7180ea659
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r1
    h: 3e69f4301b13
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r1
    h: 820ba9509056
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r1
    h: 3e69f4301b13
  review: drafted
  review_note: 'support check: partial - Passages only say ''Internal alarm'' with the EepromErr label;
    ''data storage failure'' is an inference, though the statement''s note admits this.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears by itself within minutes; restart then service if it persists
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r2
    h: b231add85b97
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r2
    h: 188818cfc2d0
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r2
    h: 0add3ff3ad57
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r2
    h: bdc8c4a39513
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r4
    h: 2dbc93c6662f
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r2
    h: 0add3ff3ad57
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation only when the alarm does not clear automatically
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r2
    h: b231add85b97
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r2
    h: 188818cfc2d0
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=34.r2
    h: 0add3ff3ad57
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r2
    h: bdc8c4a39513
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r4
    h: 2dbc93c6662f
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r2
    h: 0add3ff3ad57
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r6
    h: 62f30197194f
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-25ktl-208
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r1
    h: a1a7180ea659
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=48.r2
    h: b231add85b97
  review: drafted
---
