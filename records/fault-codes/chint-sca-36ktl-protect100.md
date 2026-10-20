---
id: fc:chint-sca-36ktl-protect100
type: FaultCode
name: CPS SCA36KTL Protect0100
aliases:
- Protect0100
- protect100
- CPS Protect0100
- The sensor fault of leakage current
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Protect0100
code_key: protect100
display_message: The sensor fault of leakage current
vendor_severity: Protection
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:filter-board
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If power-cycle fails; service replaces filter board or inverter.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; escalate to service if fault persists.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
