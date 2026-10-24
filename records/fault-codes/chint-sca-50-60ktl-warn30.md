---
id: fc:chint-sca-50-60ktl-warn30
type: FaultCode
name: CPS SCA50-60KTL Warn0030
aliases:
- Warn0030
- warn30
- CPS Warn0030
- EepromErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Warn0030
code_key: warn30
display_message: EepromErr
vendor_severity: Warning
page: 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r3
    h: 3290ff04c783
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r3
    h: 3290ff04c783
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the warning does not clear by itself.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r3
    h: 3290ff04c783
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; contact service if not cleared.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r3
    h: 3290ff04c783
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r3
    h: 3290ff04c783
  review: drafted
---
