---
id: fc:schneider-electric-conext-cl125-36
type: FaultCode
name: Schneider Electric CL125 036
aliases:
- '036'
- '36'
- Schneider Electric 036
- Module temperature is too high.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '036'
code_key: '36'
display_message: Module temperature is too high.
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r1
    h: eb9ca4d202d5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  note: Power module temperature too high.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r1
    h: eb9ca4d202d5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r1
    h: eb9ca4d202d5
  review: drafted
  review_note: 'support check: partial - Inverter module temperature is the subject, but ''affects Inverter''
    is generic and only implied.'
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-ac-ratio-reduction
  note: When DC input exceeds a DC:AC ratio of 1.5.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r1
    h: eb9ca4d202d5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r1
    h: eb9ca4d202d5
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r1
    h: eb9ca4d202d5
  review: drafted
---
