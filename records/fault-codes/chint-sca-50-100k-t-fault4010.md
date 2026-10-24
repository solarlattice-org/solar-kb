---
id: fc:chint-sca-50-100k-t-fault4010
type: FaultCode
name: CPS SCA50-100K-T Fault4010
aliases:
- Fault4010
- fault4010
- CPS Fault4010
- Bus High VoltageDiffere ntialFault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault4010
code_key: fault4010
display_message: Bus High VoltageDiffere ntialFault
vendor_severity: Fault
page: 146
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-point-voltage-imbalance
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
  review_note: 'support check: partial - Bus High Voltage Differential Fault loosely maps to neutral point
    voltage imbalance, but this is not stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Protection fault; restart required after the alarm clears implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48
    h: 9cff980c7e47
  review: drafted
  review_note: 'support check: partial - The passages don''t state the device stops feeding in for Fault4010;
    the Protection Faults table is for different codes and…'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Wait for alarm to clear, then restart; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
  review_note: 'support check: partial - Row says wait for auto-clearing, then restart the inverter and
    call service if it persists; the classification as manual reset…'
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r2
    h: a03501754bb9
  review: drafted
---
