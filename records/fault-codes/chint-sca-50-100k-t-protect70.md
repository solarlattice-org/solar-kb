---
id: fc:chint-sca-50-100k-t-protect70
type: FaultCode
name: CPS SCA50-100K-T Protect0070
aliases:
- Protect0070
- protect70
- CPS Protect0070
- Grid Line Vrms OutLim
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0070
code_key: protect70
display_message: Grid Line Vrms OutLim
vendor_severity: Protection
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r3
    h: 71846a8453a0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r3
    h: 71846a8453a0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-point-voltage-imbalance
  note: Bus imbalance, linked to grid phase impedance and voltage imbalance
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r2
    h: d9c627238336
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r2
    h: 14073738a6a6
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r7
    h: 5a995483cf94
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r2
    h: f5d9bb942146
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r8
    h: e9adaf6de0e7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r10
    h: 1e434493c756
  review: drafted
  review_note: 'support check: partial - Protect0070 is bus imbalance tied to grid phase impedance and
    voltage imbalance, but ''neutral point'' is not stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise DC injection limit parameter to tolerate transients
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r2
    h: d9c627238336
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r2
    h: 14073738a6a6
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r7
    h: 5a995483cf94
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r2
    h: f5d9bb942146
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r8
    h: e9adaf6de0e7
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r10
    h: 1e434493c756
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if fault persists after parameter adjustment
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r2
    h: 14073738a6a6
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r7
    h: 5a995483cf94
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r2
    h: f5d9bb942146
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r10
    h: 1e434493c756
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r3
    h: 71846a8453a0
  review: drafted
---
