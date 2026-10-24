---
id: fc:chint-sch-350ktl-reversepvxelectrode
type: FaultCode
name: CPS SCH350KTL Reverse PVx electrode
aliases:
- Reverse PVx electrode
- reversepvxelectrode
- CPS Reverse PVx electrode
- x=1, 2…30
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: Reverse PVx electrode
code_key: reversepvxelectrode
display_message: x=1, 2…30
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r5
    h: 9ba5fff33828
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r5
    h: 9ba5fff33828
  review: drafted
  review_note: 'support check: partial - The row implies reverse polarity on a PV string, but it does
    not explicitly say the fault reports it as…'
- claim_id: c3
  rel: affects
  target: comp:pv-array
  note: The PV string connected with reversed polarity on input x.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r5
    h: 9ba5fff33828
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r5
    h: 9ba5fff33828
  review: drafted
  review_note: 'support check: partial - A meter is used to find the reversed string, which is a manual
    check; the row doesn''t say the fault…'
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct the reversed string connection; contact service if the problem remains.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r5
    h: 9ba5fff33828
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sch-350ktl
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r5
    h: 9ba5fff33828
  review: drafted
---
