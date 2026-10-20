---
id: fc:chint-sca-36ktl-intfanerr
type: FaultCode
name: CPS SCA36KTL IntFanErr
aliases:
- IntFanErr
- intfanerr
- CPS IntFanErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: IntFanErr
code_key: intfanerr
vendor_severity: Warning
page: 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r2
    h: dbbc0d063b61
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r2
    h: dbbc0d063b61
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r2
    h: dbbc0d063b61
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r2
    h: dbbc0d063b61
  review: drafted
  review_note: 'support check: partial - Replace inverter implies service-required, but it is a warning
    and ''clears by'' is not stated; replacement is implied repair.'
---
