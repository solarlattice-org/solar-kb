---
id: fc:fronius-primo-516
type: FaultCode
name: Fronius Primo 516
aliases:
- '516'
- Fronius 516
- Communication with memory unit not possible
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '516'
code_key: '516'
display_message: Communication with memory unit not possible
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r4
    h: 414040a2b514
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r4
    h: 9aa7020f2e61
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r4
    h: 414040a2b514
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:memory-unit
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r4
    h: 9aa7020f2e61
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r4
    h: 414040a2b514
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r4
    h: 9aa7020f2e61
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r4
    h: 414040a2b514
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r4
    h: 9aa7020f2e61
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r4
    h: 9aa7020f2e61
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
---
