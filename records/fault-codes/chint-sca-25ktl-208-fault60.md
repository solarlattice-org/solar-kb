---
id: fc:chint-sca-25ktl-208-fault60
type: FaultCode
name: CPS SCA25KTL-208 Fault0060
aliases:
- Fault0060
- fault60
- CPS Fault0060
- CPLD Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Fault0060
code_key: fault60
display_message: CPLD Fault
vendor_severity: Fault
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r3
    h: a2eaee3a693f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r4
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r1
    h: 3f0a2a621e5d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r3
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r3
    h: c59976c38153
  review: drafted
  review_note: 'support check: partial - CPLD fault is an internal fault, but the passages don''t describe
    it as an internal device fault explicitly.'
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r3
    h: a2eaee3a693f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r1
    h: 3f0a2a621e5d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r3
    h: a2eaee3a693f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r4
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r1
    h: 3f0a2a621e5d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r3
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r3
    h: c59976c38153
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:control-board-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r3
    h: a2eaee3a693f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r1
    h: 3f0a2a621e5d
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r3
    h: a2eaee3a693f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r4
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r1
    h: 3f0a2a621e5d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r3
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r3
    h: c59976c38153
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; board or inverter replacement if the fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r2
    h: e263f88ecf19
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r3
    h: a2eaee3a693f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r4
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=35.r1
    h: 3f0a2a621e5d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r3
    h: e17d4c1a5c6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r3
    h: c59976c38153
  review: drafted
  review_note: 'support check: partial - Power cycle then replacement stated; manual-reset classification
    only implied.'
---
