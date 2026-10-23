---
id: fc:chint-sch-350ktl-cflowerr
type: FaultCode
name: CPS SCH350KTL CfLowErr
aliases:
- CfLowErr
- cflowerr
- CPS CfLowErr
- voltage across flying capacitor too low
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: CfLowErr
code_key: cflowerr
display_message: voltage across flying capacitor too low
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:flying-capacitor-undervoltage
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=h143
    h: 1a6d43333022
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Only a table title ''Warning Faults'' is cited, with no row showing
    CfLowErr in it; classification not clearly tied to…'
- claim_id: c4
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Remove the lowest-voltage branch and restart; contact service if the condition remains
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r1
    h: 1cf0c0d20e6c
  review: drafted
  review_note: 'support check: partial - Restart is an operator action, but the passage doesn''t explicitly
    say how it clears; manual reset is implied only.'
---
