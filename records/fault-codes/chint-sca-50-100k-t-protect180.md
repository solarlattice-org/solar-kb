---
id: fc:chint-sca-50-100k-t-protect180
type: FaultCode
name: CPS SCA50-100K-T Protect0180
aliases:
- Protect0180
- protect180
- CPS Protect0180
- DCI High Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0180
code_key: protect180
display_message: DCI High Fault
vendor_severity: Protection
page: 134
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r2
    h: 8b40f25628a8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r2
    h: 8b40f25628a8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:current-sensor-offset
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r7
    h: a49b0fcf2476
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r12
    h: e2afb015e016
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r13
    h: f2e08df11d6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r2
    h: 70718c9624f2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r6
    h: 70f2eb9f0ea2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Passages describe DCI sampling offset, which is approximately
    a current sensor offset, but the wording differs.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r7
    h: a49b0fcf2476
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r13
    h: f2e08df11d6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r2
    h: 70718c9624f2
  review: drafted
  review_note: 'support check: partial - Passages refer to the inverter only as the thing to recalibrate
    or replace; no specific component is stated as affected.'
- claim_id: c5
  rel: mitigated_by
  target: mit:sensor-recalibration
  note: Applies when the inverter can still start up.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r7
    h: a49b0fcf2476
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r12
    h: e2afb015e016
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r2
    h: 70718c9624f2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r6
    h: 70f2eb9f0ea2
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the alarm persists and the inverter cannot start.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r7
    h: a49b0fcf2476
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r13
    h: f2e08df11d6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r2
    h: 70718c9624f2
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r6
    h: 70f2eb9f0ea2
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r8
    h: 032b9ffcd667
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r7
    h: a49b0fcf2476
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r13
    h: f2e08df11d6e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r2
    h: 70718c9624f2
  review: drafted
  review_note: 'support check: partial - Inability to start up is implied in some cases but a trip is
    not stated.'
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=52.r2
    h: 8b40f25628a8
  review: drafted
---
