---
id: fc:chint-sca-25ktl-480-gridfoutlim
type: FaultCode
name: CPS SCA25KTL-480 GridF.OutLim
aliases:
- GridF.OutLim
- gridfoutlim
- CPS GridF.OutLim
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-480
family_name: CPS SCA25KTL-DO-R/US-480
code: GridF.OutLim
code_key: gridfoutlim
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-25kw-user-manual-rev-2-1
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r3
    h: bbd11460677c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r5
    h: '8947913e2857'
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r5
    h: e36a418dd1ab
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r3
    h: bbd11460677c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r5
    h: 545409bca32e
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r2
    h: fab15c9d6b4e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r4
    h: 069b2e30ec6d
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r13
    h: fab15c9d6b4e
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  note: Compare measured frequency on display against limits
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r5
    h: '8947913e2857'
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r5
    h: e36a418dd1ab
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r3
    h: bbd11460677c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r5
    h: 545409bca32e
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r2
    h: fab15c9d6b4e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r5
    h: 6220a5de451a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r13
    h: fab15c9d6b4e
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r5
    h: '8947913e2857'
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r5
    h: e36a418dd1ab
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r3
    h: bbd11460677c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r5
    h: 545409bca32e
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r2
    h: fab15c9d6b4e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r3
    h: 9e880871e4d6
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r13
    h: fab15c9d6b4e
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Restart needed implies inverter stopped
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r5
    h: '8947913e2857'
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r5
    h: e36a418dd1ab
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r3
    h: bbd11460677c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r5
    h: 545409bca32e
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r2
    h: fab15c9d6b4e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r5
    h: 6220a5de451a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r13
    h: fab15c9d6b4e
  review: drafted
  review_note: 'support check: partial - Restart instruction implies stoppage but trip is not explicitly
    stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart once frequency is within limits
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r5
    h: '8947913e2857'
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=50.r5
    h: e36a418dd1ab
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=57.r3
    h: bbd11460677c
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=31.r5
    h: 545409bca32e
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r2
    h: fab15c9d6b4e
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r5
    h: 6220a5de451a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r13
    h: fab15c9d6b4e
  review: drafted
---
