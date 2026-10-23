---
id: fc:chint-sca-50-100k-t-fault4000
type: FaultCode
name: CPS SCA50-100K-T Fault4000
aliases:
- Fault4000
- fault4000
- CPS Fault4000
- PN Bus DropFault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault4000
code_key: fault4000
display_message: PN Bus DropFault
vendor_severity: Fault
page: 146
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r3
    h: 791f54d5c6ae
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r3
    h: 791f54d5c6ae
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r3
    h: 791f54d5c6ae
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r3
    h: 791f54d5c6ae
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Protection fault; restart required after the alarm clears implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r3
    h: 791f54d5c6ae
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48
    h: 9cff980c7e47
  review: drafted
  review_note: 'support check: partial - No passage states Fault4000 stops production; the Protection
    table covers other codes and a restart instruction only weakly implies a trip.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Wait for alarm to clear, then restart; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=64.r3
    h: 791f54d5c6ae
  review: drafted
  review_note: 'support check: partial - Row says wait for auto-clearing, then restart the inverter and
    call service if it persists; the classification as manual reset…'
---
