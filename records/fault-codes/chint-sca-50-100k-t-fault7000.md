---
id: fc:chint-sca-50-100k-t-fault7000
type: FaultCode
name: CPS SCA50-100K-T Fault7000
aliases:
- Fault7000
- fault7000
- CPS Fault7000
- Bus Over Voltage Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault7000
code_key: fault7000
display_message: Bus Over Voltage Fault
vendor_severity: Fault
page: 147
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
  review_note: 'support check: partial - The row tells the user to measure DC terminal voltage as a troubleshooting
    step, not as the way the fault…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Protection fault; restart required after the alarm clears implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48
    h: 9cff980c7e47
  review: drafted
  review_note: 'support check: partial - No passage states Fault7000 stops production; the Protection
    table covers other codes and a restart instruction only weakly implies a trip.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Wait for alarm to clear, then restart; if persistent, check open-circuit PV voltage, then service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r1
    h: 18eda6e39114
  review: drafted
  review_note: 'support check: partial - Row says wait for auto-clearing, then restart, check open-circuit
    PV voltage and call service; the classification as manual reset is…'
---
