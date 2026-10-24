---
id: fc:sma-stp-tl-us-6801-6802
type: FaultCode
name: SMA STP-TL-US 6801-6802
aliases:
- 6801-6802
- SMA 6801-6802
- Self-diagnosis > Input
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 6801-6802
code_key: 6801-6802
code_from: 6801
code_to: 6802
display_message: Self-diagnosis > Input
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r2
    h: c26f36d80f19
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r2
    h: c26f36d80f19
  review: drafted
  review_note: 'support check: partial - Input A defective is stated, but ''abnormal PV input'' is an
    interpretation of the input being defective.'
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r2
    h: c26f36d80f19
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r2
    h: c26f36d80f19
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r2
    h: c26f36d80f19
  review: drafted
---
