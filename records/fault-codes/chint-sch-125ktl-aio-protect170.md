---
id: fc:chint-sch-125ktl-aio-protect170
type: FaultCode
name: CPS SCH125KTL-AIO Protect0170
aliases:
- Protect0170
- protect170
- CPS Protect0170
- DCI high
category: Inverters
make: chint
make_name: CPS
model_family: sch-125ktl-aio
family_name: CPS SCH125KTL-AIO/US-600
code: Protect0170
code_key: protect170
display_message: DCI high
vendor_severity: Protection
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch125ktl-aio-us-600-sep-2020
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r1
    h: 0df5fe60a8a2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r1
    h: 0df5fe60a8a2
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32
    h: cf5fe9501873
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r3
    h: ecbfae44be5b
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r9
    h: 60cc9ff28b0b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r7
    h: f967b5cd7f6b
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r1
    h: 0df5fe60a8a2
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r11
    h: a729b3df833e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r9
    h: 50ed835a5c2d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raising the DCI limit is the first step; replacement if fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r9
    h: 60cc9ff28b0b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r7
    h: f967b5cd7f6b
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r1
    h: ba925540d1fd
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r1
    h: 0df5fe60a8a2
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r11
    h: a729b3df833e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r3
    h: ecbfae44be5b
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r10
    h: 71093fbc487a
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r1
    h: ba925540d1fd
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r1
    h: 0df5fe60a8a2
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r11
    h: a729b3df833e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r9
    h: 50ed835a5c2d
  review: drafted
---
