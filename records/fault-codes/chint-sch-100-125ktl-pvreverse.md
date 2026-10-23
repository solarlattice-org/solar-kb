---
id: fc:chint-sch-100-125ktl-pvreverse
type: FaultCode
name: CPS SCH100-125KTL PV Reverse
aliases:
- PV Reverse
- pvreverse
- CPS PV Reverse
- PV input reverse connection
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: PV Reverse
code_key: pvreverse
display_message: PV input reverse connection
vendor_severity: Protection
page: 77
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r1
    h: d099f0814cab
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r1
    h: d099f0814cab
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37
    h: b3d48b50b5c7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r5
    h: e979706e6564
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r1
    h: d099f0814cab
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r2
    h: e81e09c08204
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r5
    h: e979706e6564
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r1
    h: d099f0814cab
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r2
    h: e81e09c08204
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r5
    h: e979706e6564
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r1
    h: d099f0814cab
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r2
    h: e81e09c08204
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r5
    h: e979706e6564
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=37.r1
    h: d099f0814cab
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r2
    h: e81e09c08204
  review: drafted
---
