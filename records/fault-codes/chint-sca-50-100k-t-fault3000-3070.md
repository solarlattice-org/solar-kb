---
id: fc:chint-sca-50-100k-t-fault3000-3070
type: FaultCode
name: CPS SCA50-100K-T Fault3000-3070
aliases:
- Fault3000-3070
- fault3000-3070
- CPS Fault3000-3070
- PV1 …PV16 ReverseInject Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault3000-3070
code_key: fault3000-3070
code_from: 3000
code_to: 3070
display_message: PV1 …PV16 ReverseInject Fault
vendor_severity: Fault
page: 145
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
  review_note: 'support check: partial - Row says use a meter to find the abnormal string, but does not
    say it measures string current.'
- claim_id: c6
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c10
  rel: has_production_effect
  target: ec:trip
  note: Protection fault; restart required after the alarm clears implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48
    h: 9cff980c7e47
  review: drafted
  review_note: 'support check: partial - Restart is required after the fault, implying a stop, but a trip
    is not explicitly stated for this row.'
- claim_id: c11
  rel: has_recovery
  target: ec:manual-reset
  note: Wait for alarm to clear, then switch cycle and restart; if persistent, isolate and fix strings,
    then service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
- claim_id: c12
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=63.r1
    h: f481151258c7
  review: drafted
---
