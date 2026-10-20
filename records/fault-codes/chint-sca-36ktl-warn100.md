---
id: fc:chint-sca-36ktl-warn100
type: FaultCode
name: CPS SCA36KTL Warn0100
aliases:
- Warn0100
- warn100
- CPS Warn0100
- AC SPD
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Warn0100
code_key: warn100
display_message: AC SPD
vendor_severity: Warning
page: 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:surge-protector-exhausted
  note: When the SPD indicator shows red.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
  review_note: 'support check: partial - Red indicator means replace SPD, implying exhausted, not explicit;
    text says DC SPD check though row is AC SPD.'
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:spd-replacement
  note: 'Indicator red: replace; green: reseat module, then service if unresolved.'
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  review: drafted
  review_note: 'support check: partial - Service/replacement implied but not explicit.'
---
