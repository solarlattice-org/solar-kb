---
id: fc:chint-sca-50-60ktl-isolationerr
type: FaultCode
name: CPS SCA50-60KTL IsolationErr
aliases:
- IsolationErr
- isolationerr
- CPS IsolationErr
- Insulation resistance low
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: IsolationErr
code_key: isolationerr
display_message: Insulation resistance low
vendor_severity: PROTECTION
page: 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
  review_note: 'support check: partial - PV string wires are checked for leakage to ground, but DC cable
    is not explicitly named as the affected component.'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  note: Strings reconnected one at a time to find the faulted string.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  review: drafted
---
