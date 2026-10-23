---
id: fc:chint-sch-350ktl-protect150
type: FaultCode
name: CPS SCH350KTL Protect0150
aliases:
- Protect0150
- protect150
- CPS Protect0150
- mini MCU fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: Protect0150
code_key: protect150
display_message: mini MCU fault
vendor_severity: Protection
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r3
    h: 26a057f88126
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r2
    h: fcadfccee7df
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r4
    h: 325cd2c200f2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r4
    h: 0b612a193887
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r3
    h: 26a057f88126
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r2
    h: fcadfccee7df
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r4
    h: 325cd2c200f2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r4
    h: 0b612a193887
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r3
    h: 26a057f88126
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r2
    h: fcadfccee7df
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r4
    h: 325cd2c200f2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r4
    h: 0b612a193887
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35
    h: 2441b6237235
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r3
    h: 26a057f88126
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r2
    h: fcadfccee7df
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r4
    h: 325cd2c200f2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r4
    h: 0b612a193887
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r4
    h: 0b612a193887
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r4
    h: 325cd2c200f2
  review: drafted
  review_note: 'support check: partial - Type is Protection with power cycling needed, which implies a
    stop, but no passage explicitly states that production stops or…'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle clears normal case; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r3
    h: 26a057f88126
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r2
    h: fcadfccee7df
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r4
    h: 325cd2c200f2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r4
    h: 0b612a193887
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r4
    h: 98a40429d17b
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35
    h: 2441b6237235
  review: drafted
---
