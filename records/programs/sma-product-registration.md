---
id: prog:sma-product-registration
type: Program
name: SMA product registration
aliases:
- product registration
- Product Registration Service
category: Warranty
program_kind: warranty
claims:
- claim_id: c1
  rel: issued_by
  target: org:sma
  note: Run by SMA Solar Technology AG as a service under the mySMA General Terms of Use.
  cite:
  - src: src:sma-doc-tou-mysma-stou-services-202107-en-10
    loc: sec=h27
    h: 94f000590496
  review: drafted
  review_note: 'support check: partial - Passage shows the service supplements mySMA General Terms of
    SMA Solar Technology AG, but doesn''t explicitly say SMA issues the registration or runs it as a service
    (close enough in substance, though).'
- claim_id: c2
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Total factory warranty term after the registration-based extension, selected SMA products
    only.
  cite:
  - src: src:sma-doc-tou-mysma-stou-services-202107-en-10
    loc: sec=h28
    h: 87c9b30bf1bb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SMA runs the Product Registration Service under its mySMA terms of use, so owners can register SMA products and assign them to an SMA warranty. There are three registration options: register within 12 months of purchase to set the factory warranty start date, register within 12 months of purchase to extend the factory warranty on selected products, or enter extended warranty codes to activate an extended warranty. The options do not apply to every product, so check the eligibility details shown in the registration service. An SMA installer article says the system owner (recommended) or the installer can register within 12 months after commissioning, but the customer always has to confirm the registration. When an installer registers on the customer's behalf, SMA emails the customer for confirmation. If the customer has not confirmed within three weeks, after two reminder emails, the registration data is deleted. SMA can block a user who cannot show that the PV system operator authorized them to register the system. If there is any doubt, the operator's instructions take priority.
