---
id: fc:chint-sca-36ktl-fault90
type: FaultCode
name: CPS SCA36KTL Fault0090
aliases:
- Fault0090
- fault90
- CPS Fault0090
- Dynamic leakage current high
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Fault0090
code_key: fault90
display_message: Dynamic leakage current high
vendor_severity: Fault
page: 8
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:leakage-current
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: drafted
  review_note: 'support check: partial - PV wires and strings are checked for leakage, but DC cable is
    not explicitly named as affected component.'
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  note: Strings reconnected one at a time to find the one causing the alarm.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-36ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  review: drafted
---
