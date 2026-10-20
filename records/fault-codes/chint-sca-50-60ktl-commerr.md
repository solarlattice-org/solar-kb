---
id: fc:chint-sca-50-60ktl-commerr
type: FaultCode
name: CPS SCA50-60KTL CommErr
aliases:
- CommErr
- commerr
- CPS CommErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: CommErr
code_key: commerr
vendor_severity: ALARM
page: 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r2
    h: 1772b17b4f0d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r2
    h: 1772b17b4f0d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: Internal communication within the inverter.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r2
    h: 1772b17b4f0d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r2
    h: 1772b17b4f0d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r2
    h: 1772b17b4f0d
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then AC power cycle; then service if persistent.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r2
    h: 1772b17b4f0d
  review: drafted
---
