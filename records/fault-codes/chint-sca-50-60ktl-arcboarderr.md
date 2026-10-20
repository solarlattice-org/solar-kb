---
id: fc:chint-sca-50-60ktl-arcboarderr
type: FaultCode
name: CPS SCA50-60KTL Arcboard Err
aliases:
- Arcboard Err
- arcboarderr
- CPS Arcboard Err
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Arcboard Err
code_key: arcboarderr
vendor_severity: Protection
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
  review_note: 'support check: partial - Arcboard Err name suggests arc board failure and replacement
    is suggested, but no explicit failure statement.'
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:arc-fault-self-test
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm recurs after connector check and arc test.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Operator checks connector and runs arc test; service if alarm recurs.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  review: drafted
  review_note: 'support check: partial - Operator actions stated, but manual reset clearing not explicit.'
---
