---
id: fc:chint-sch-275ktl-gridvoutlim
type: FaultCode
name: CPS SCH275KTL GridV.OutLim
aliases:
- GridV.OutLim
- gridvoutlim
- CPS GridV.OutLim
category: Inverters
make: chint
make_name: CPS
model_family: sch-275ktl
family_name: CPS SCH275KTL-DO/US-800
code: GridV.OutLim
code_key: gridvoutlim
vendor_severity: Protection
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r1
    h: 76ed8f2716c1
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r2
    h: 84a4c51bb192
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r1
    h: 76ed8f2716c1
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r2
    h: 84a4c51bb192
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27
    h: 645c5466b9b0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r4
    h: 07d005ffe789
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r4
    h: 800b94fc4b9a
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r4
    h: 07d005ffe789
  review: drafted
  review_note: 'support check: partial - Passages imply AC voltage is checked against range but don''t
    state a grid voltage measurement detection method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r4
    h: 800b94fc4b9a
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r4
    h: 07d005ffe789
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r2
    h: 6ec924c33315
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r4
    h: cac2c2524082
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r1
    h: 44a791cf9744
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r1
    h: 76ed8f2716c1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r12
    h: 44a791cf9744
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Restart needed implies inverter stopped
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r4
    h: 800b94fc4b9a
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r4
    h: 07d005ffe789
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r2
    h: 6ec924c33315
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r4
    h: cac2c2524082
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r1
    h: 44a791cf9744
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r2
    h: 84a4c51bb192
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r12
    h: 44a791cf9744
  review: drafted
  review_note: 'support check: partial - Restart instruction implies stoppage but passages never state
    that feed-in stops or that it is a trip.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after verifying grid connection; service if not cleared
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r4
    h: 800b94fc4b9a
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r4
    h: 07d005ffe789
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r2
    h: 6ec924c33315
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r4
    h: cac2c2524082
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r1
    h: 44a791cf9744
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r2
    h: 84a4c51bb192
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r12
    h: 44a791cf9744
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sch-275ktl
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r1
    h: 76ed8f2716c1
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r2
    h: 84a4c51bb192
  review: drafted
---
