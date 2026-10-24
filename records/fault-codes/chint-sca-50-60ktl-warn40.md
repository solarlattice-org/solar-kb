---
id: fc:chint-sca-50-60ktl-warn40
type: FaultCode
name: CPS SCA50-60KTL Warn0040
aliases:
- Warn0040
- warn40
- CPS Warn0040
- DC SPD
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Warn0040
code_key: warn40
display_message: DC SPD
vendor_severity: Warning
page: 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:surge-protector-exhausted
  note: When the SPD indicator shows red.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
  review_note: 'support check: partial - Red indicator means replace SPD, implying exhausted, but exhaustion
    is not explicitly stated.'
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:spd-replacement
  note: 'Indicator red: replace; green: reseat module, then service if unresolved.'
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
  review_note: 'support check: partial - Replace SPD/contact service implies service required, but not
    explicitly stated for this row.'
- claim_id: c9
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  review: drafted
---
