---
id: fc:chint-sca-36ktl-extfanerr
type: FaultCode
name: CPS SCA36KTL ExtFanErr
aliases:
- ExtFanErr
- extfanerr
- CPS ExtFanErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: ExtFanErr
code_key: extfanerr
vendor_severity: Warning
page: 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-supply-voltage-check
  note: When fan is not spinning; low supply voltage points to inverter, adequate voltage to fan.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Check fan blades for foreign objects.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:fan-replacement
  note: When fan stopped and supply voltage is adequate.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When fan spins (sensing fault) or fan supply voltage is low.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:auto-reset
  note: Alarm may clear on its own; escalate to cleaning blades, AC power cycle, then service.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  review: drafted
---
