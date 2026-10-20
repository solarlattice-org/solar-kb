---
id: fc:chint-sca-36ktl-eepromerr
type: FaultCode
name: CPS SCA36KTL EepromErr
aliases:
- EepromErr
- eepromerr
- CPS EepromErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: EepromErr
code_key: eepromerr
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r1
    h: f94a58942f56
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r2
    h: e81c19300640
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r3
    h: 609d6ef144dc
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Internal memory problem.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r1
    h: f94a58942f56
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r2
    h: e81c19300640
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: Defined as an internal alarm.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r1
    h: f94a58942f56
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Defined as internal alarm; warning classification is not stated
    in this passage (u6 elsewhere says Warning but not cited).'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r3
    h: 609d6ef144dc
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; contact service if not cleared.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=5.r3
    h: 609d6ef144dc
  review: drafted
---
