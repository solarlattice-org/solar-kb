---
id: fc:sma-stp-tl-us-6901-6902
type: FaultCode
name: SMA STP-TL-US 6901-6902
aliases:
- 6901-6902
- SMA 6901-6902
- Self-diagnosis > Input B defective
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 6901-6902
code_key: 6901-6902
code_from: 6901
code_to: 6902
display_message: Self-diagnosis > Input B defective
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r3
    h: 9f5104c85df5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r3
    h: 9f5104c85df5
  review: drafted
  review_note: 'support check: partial - Input B defective is stated, but ''abnormal PV input'' is an
    interpretation of the input being defective.'
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r3
    h: 9f5104c85df5
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r3
    h: 9f5104c85df5
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r3
    h: 9f5104c85df5
  review: drafted
---
