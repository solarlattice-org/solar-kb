---
id: fc:fronius-symo-309
type: FaultCode
name: Fronius Symo 309
aliases:
- '309'
- Fronius 309
- DC input voltage MPPT1 too high
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '309'
code_key: '309'
display_message: DC input voltage MPPT1 too high
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r10
    h: c8ec92ca6ba9
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r10
    h: c8ec92ca6ba9
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 97667f973ec2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r10
    h: c8ec92ca6ba9
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 97667f973ec2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
  review_note: 'support check: partial - 309 is listed among the status codes, but the passages don''t
    call it a fault. The only mention of fault…'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Self-clears; escalate only if persistent.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r10
    h: c8ec92ca6ba9
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 97667f973ec2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
  review_note: 'review: partial - The 309 row''s behavior and remedy cells are blank in both tables, so
    auto-clearing and ''escalate if persistent'' rest only on the…'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the code persists.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 97667f973ec2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
  review_note: 'support check: partial - The 309 row has no remedy; contact-service-if-persists is only
    inferred from the grouped 308 row.'
- claim_id: c6
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r10
    h: c8ec92ca6ba9
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
---
