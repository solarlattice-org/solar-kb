---
id: fc:chint-sca-25ktl-208-fault90
type: FaultCode
name: CPS SCA25KTL-208 Fault0090
aliases:
- Fault0090
- fault90
- CPS Fault0090
- Dynamic leakage current high
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Fault0090
code_key: fault90
display_message: Dynamic leakage current high
vendor_severity: Fault
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r2
    h: 04e6497a3710
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r2
    h: e9c9afab52c4
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r4
    h: a45c1f6ef302
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r7
    h: 4479bde286d9
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r7
    h: 10e9da6af778
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r2
    h: 04e6497a3710
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r2
    h: e9c9afab52c4
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r4
    h: a45c1f6ef302
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r7
    h: 4479bde286d9
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r7
    h: 10e9da6af778
  review: drafted
  review_note: 'support check: partial - Remedy traces PV wiring for leakage to ground, but a DC cable
    is not explicitly named.'
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r2
    h: 04e6497a3710
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r2
    h: e9c9afab52c4
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r4
    h: a45c1f6ef302
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r7
    h: 4479bde286d9
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r7
    h: 10e9da6af778
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r2
    h: 04e6497a3710
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r2
    h: e9c9afab52c4
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r4
    h: a45c1f6ef302
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r8
    h: e845aaf5667b
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r9
    h: f21d92270551
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r7
    h: 10e9da6af778
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r2
    h: 04e6497a3710
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r2
    h: e9c9afab52c4
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r4
    h: a45c1f6ef302
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r7
    h: 4479bde286d9
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r7
    h: 10e9da6af778
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=62.r2
    h: 04e6497a3710
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=39.r2
    h: e9c9afab52c4
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r4
    h: a45c1f6ef302
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r9
    h: f21d92270551
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r7
    h: 10e9da6af778
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:chint-sca-25ktl-208
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=53.r4
    h: 8dc323ede861
  review: drafted
---
