---
id: prog:sma-factory-warranty
type: Program
name: SMA factory warranty
aliases:
- SMA standard warranty
- SMA manufacturer warranty
- SMA Limited Factory Warranty
- Standard SMA Limited Factory Warranty
category: Warranty
program_kind: warranty
claims:
- claim_id: c1
  rel: issued_by
  target: org:sma
  note: SMA Solar Technology AG is the warrantor; services may be performed by SMA authorized partners.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h3
    h: 0f2dfeb0cc6f
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: applies_to
  target: prod:sma-sunny-tripower
  note: Applies only to new devices.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-boy
  note: Applies only to new devices.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-boy-storage
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
  review_note: 'review: partial - SUNNY ISLAND is a listed product type, but the specific models 4.4M
    / 6.0H / 8.0H do not appear in the passage.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-island-x
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: applies_to
  target: prod:sma-sunny-home-manager
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: applies_to
  target: prod:sma-com-gateway
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-inverter-manager
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: applies_to
  target: prod:sma-energy-meter
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sma-rapid-shutdown-system
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c12
  rel: applies_to
  target: prod:jms-f-rapid-shutdown-device
  scope:
    regions:
    - region:us
  note: Warranty for the JMS-F/JMS-FA Rapid Shutdown Junction Box 1500V applies only in the USA.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  rel: applies_to
  target: prod:sma-ev-charger
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  rel: applies_to
  target: prod:sma-echarger
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c15
  rel: applies_to
  target: prod:sma-data-manager-m
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c16
  rel: applies_to
  target: prod:sma-sunny-tripower-smart-energy
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c17
  rel: applies_to
  target: prod:sma-sunny-boy-smart-energy
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c18
  rel: applies_to
  target: prod:sma-home-storage
  negated: true
  note: Covered only by its own separate warranty terms.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h1
    h: 7e1ee30a5535
  review: drafted
- claim_id: c19
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Listed products, when the product is registered on the SMA website within 12 months after
    initial commissioning or the first claimant's invoice date; not available in Australia and New Zealand
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: drafted
  review_note: 'support check: partial - The 10-year extension on registration within 12 months and the
    Australia/NZ exclusion are stated, but the passage does not say which products are listed (footnote
    2 products).; possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions)'
- claim_id: c20
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Selected SMA products registered in the Product Registration Service within 12 months of
    purchase (an additional five years)
  cite:
  - src: src:sma-doc-tou-mysma-stou-services-202107-en-10
    loc: sec=h28
    h: 87c9b30bf1bb
  review: disputed
  conflicts_with:
  - prog:sma-factory-warranty#c21
  - prog:sma-factory-warranty#c22
- claim_id: c21
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: Base manufacturer warranty before extension by product registration
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: disputed
  review_note: 'support check: partial - The passage implies a 5-year base (extension from 5 to 10), but
    it never states the base term outright for all products.; possible conflict with c19 (same source;
    check the conditions)'
  conflicts_with:
  - prog:sma-factory-warranty#c20
- claim_id: c22
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: -US Sunny Tripower models and -US SMA Connection Units installed outside the United States
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c19 (same source; check the conditions); review: the compiler-flagged
    conflict (prog:sma-factory-warranty#c20) is a scenario difference, resolved at review'
---
The SMA factory warranty is SMA's standard manufacturer warranty on new devices such as Sunny Boy, Sunny Tripower, Sunny Island, storage inverters, meters, gateways, EV chargers and rapid shutdown equipment. SMA SMA Home Storage, SMA Storage XL and SMA Storage M fall under separate warranty terms instead. Under the warranty, SMA provides a replacement device or spare part of equivalent value; the claimant pays for transport and customs, and the replacement may have cosmetic defects or be refurbished. Claims can be made by the end customer who first put the device into operation, or by a later buyer who got the unmodified device legitimately; a third party such as an installer may file on their behalf. Register the product on the SMA website within 12 months of commissioning or invoice date to set the warranty start date and, for listed products, extend the term from 5 to 10 years; this extension is not offered in Australia or New Zealand. Without timely registration, the warranty starts on the day SMA delivered the device. The warranty requires installation and commissioning per the manufacturer's installation manual and ends if unauthorized structural changes are made to the device. Loss of production, removal and reinstallation costs, and other indirect damages are not covered.

<!-- review notes
- sentence 1: support check: partial - The passages cover new devices and the product types listed, including Sunny Boy, Sunny Tripower, Sunny Island, meters, gateways, EV chargers and rapid shutdown; the 'standard manufacturer warranty' framing is loosely supported.
- sentence 3: support check: partial - Equivalent-value replacement, claimant-borne transport and customs, and cosmetic defects are stated, but 'refurbished' is only supported as 'new and/or equivalent to new' devices or parts.
-->
