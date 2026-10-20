---
id: fc:chint-sca-36ktl-protect180
type: FaultCode
name: CPS SCA36KTL Protect0180
aliases:
- Protect0180
- protect180
- CPS Protect0180
- The sampling offset of DCI
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Protect0180
code_key: protect180
display_message: The sampling offset of DCI
vendor_severity: Protection
page: 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=7.r1
    h: 486149d00bf6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=7.r1
    h: 486149d00bf6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=7.r1
    h: 486149d00bf6
  review: drafted
  review_note: 'support check: partial - DCI sampling offset suggests an internal fault, but this is not
    explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:sensor-recalibration
  note: Applies when the inverter can still start up.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=7.r1
    h: 486149d00bf6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the alarm persists and the inverter cannot start.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=7.r1
    h: 486149d00bf6
  review: drafted
---
