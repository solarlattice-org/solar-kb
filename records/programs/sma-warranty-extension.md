---
id: prog:sma-warranty-extension
type: Program
name: SMA warranty extension
aliases:
- SMA extended warranty
- Extended Warranty Flex
- SMA free 5-year extended warranty
- SMA Extended Warranty Flex
- free 5-year extended warranty
- ACTIVE/COMFORT extended warranty
- FLEX extended warranty
category: Warranty
program_kind: warranty
claims:
- claim_id: c1
  rel: issued_by
  target: org:sma
  cite:
  - src: src:sma-kb-sma-extended-warranty-flex
    loc: sec=h1
    h: 19896f7a2b02
  - src: src:sma-kb-sma-warranty-extension-process
    loc: sec=h1
    h: 04fa0e56c1fb
  review: drafted
- claim_id: c2
  rel: applies_to
  target: prod:sma-sunny-tripower-x
  cite:
  - src: src:sma-kb-how-long-is-the-warranty-for-the-sunny-tripower-x
    loc: sec=h1
    h: e1bb3a977435
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-home-storage
  note: Free additional eight-year warranty when the battery is registered within 30 days of commissioning.
  cite:
  - src: src:sma-kb-how-long-is-the-limited-factory-warranty-for-sma-battery-systems-and-do-i-get-a-fre
    loc: sec=h1
    h: 6553120329ec
  review: drafted
- claim_id: c4
  rel: applies_to
  target: region:au
  negated: true
  note: The 5 to 10 year extension through product registration is not offered in Australia.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: drafted
- claim_id: c5
  rel: applies_to
  target: region:nz
  negated: true
  note: The 5 to 10 year extension through product registration is not offered in New Zealand.
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: drafted
- claim_id: c6
  attr: warranty_term
  value:
    max: 15
    unit: unit:YR
  conditions: SMA Extended Warranty Flex, for PV systems with inverter capacity of 100 kWp or more
  cite:
  - src: src:sma-kb-sma-extended-warranty-flex
    loc: sec=h1
    h: 19896f7a2b02
  review: drafted
- claim_id: c7
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: Free additional extension of the factory warranty for selected SMA products registered within
    12 months of purchase
  cite:
  - src: src:sma-doc-tou-mysma-stou-services-202107-en-10
    loc: sec=h28
    h: 87c9b30bf1bb
  review: disputed
  review_note: 'support check: partial - The passage says registration within 12 months gives an additional
    5 years for selected products; it does not state the warranty term as 5 YR in the way given, though
    the 5-year extension is stated.; possible conflict with c8 (same source; check the conditions)'
  conflicts_with:
  - prog:sma-warranty-extension#c9
  - prog:sma-warranty-extension#c10
- claim_id: c8
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Total factory warranty after the free extension for selected SMA products registered within
    12 months of purchase
  cite:
  - src: src:sma-doc-tou-mysma-stou-services-202107-en-10
    loc: sec=h28
    h: 87c9b30bf1bb
  review: disputed
  review_note: possible conflict with c7 (same source; check the conditions)
  conflicts_with:
  - prog:sma-warranty-extension#c10
- claim_id: c9
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Automatic extension from initial commissioning or invoice date after product registration
    within 12 months, for listed products
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: disputed
  conflicts_with:
  - prog:sma-warranty-extension#c7
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c10
  attr: warranty_term
  value:
    min: 11
    max: 20
    unit: unit:YR
  conditions: Warranty years covered by an optional purchased ACTIVE/COMFORT extended warranty, only after
    timely registration and extension to 10 years
  cite:
  - src: src:sma-doc-278702
    loc: sec=h5
    h: 961f01d834a8
  review: disputed
  conflicts_with:
  - prog:sma-warranty-extension#c7
  - prog:sma-warranty-extension#c8
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c11
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  scope:
    products:
    - prod:sma-sunny-tripower-x
  conditions: Sunny Tripower X extended warranty option
  cite:
  - src: src:sma-kb-how-long-is-the-warranty-for-the-sunny-tripower-x
    loc: sec=h1
    h: e1bb3a977435
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions)
- claim_id: c12
  attr: warranty_term
  value:
    nominal: 15
    unit: unit:YR
  scope:
    products:
    - prod:sma-sunny-tripower-x
  conditions: Sunny Tripower X extended warranty option
  cite:
  - src: src:sma-kb-how-long-is-the-warranty-for-the-sunny-tripower-x
    loc: sec=h1
    h: e1bb3a977435
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions)
- claim_id: c13
  attr: warranty_term
  value:
    nominal: 20
    unit: unit:YR
  scope:
    products:
    - prod:sma-sunny-tripower-x
  conditions: Sunny Tripower X extended warranty option
  cite:
  - src: src:sma-kb-how-long-is-the-warranty-for-the-sunny-tripower-x
    loc: sec=h1
    h: e1bb3a977435
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions)
- claim_id: c14
  attr: warranty_term
  value:
    nominal: 8
    unit: unit:YR
  scope:
    products:
    - prod:sma-home-storage
  conditions: Free additional warranty for SMA battery systems registered within 30 days of commissioning,
    giving ten years in total
  cite:
  - src: src:sma-kb-how-long-is-the-limited-factory-warranty-for-sma-battery-systems-and-do-i-get-a-fre
    loc: sec=h1
    h: 6553120329ec
  review: drafted
- claim_id: c15
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  scope:
    regions:
    - region:es
    - region:pl
    - region:be
    - region:nl
    - region:lu
    valid_from: '2021-04-01'
  conditions: Free extended warranty for eligible residential inverters in Spain, Poland or Benelux commissioned
    after April 1, 2021 and registered within 12 months of commissioning
  cite:
  - src: src:sma-kb-for-which-sma-inverters-does-the-free-5-year-warranty-apply
    loc: sec=h1
    h: f150f4bc82e7
  review: drafted
  review_note: 'support check: partial - Passage gives the commissioning after April 1, 2021 and 12-month
    registration conditions for Spain, Poland and Benelux, but the 5-year term and ''residential'' are
    as an extension; broadly supported, though the cited text does not name the individual countries Belgium,
    Netherlands and Luxembourg.'
- claim_id: c16
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  scope:
    valid_from: '2021-10-01'
  conditions: Free extended warranty for eligible residential inverters in other countries commissioned
    after October 1, 2021 and registered within 12 months of commissioning
  cite:
  - src: src:sma-kb-for-which-sma-inverters-does-the-free-5-year-warranty-apply
    loc: sec=h1
    h: f150f4bc82e7
  review: drafted
---
SMA offers warranty extensions that keep inverters covered after the SMA factory warranty runs out. Selected residential inverters get a free 5-year extension, for 10 years in total, if they are registered in mySMA Product Registration within 12 months of commissioning. US model inverters do not get the free extension because they already come with a 10-year factory warranty. Inverters that already have a 10-year warranty are also excluded. Installers can start the registration with the customer's contact details, the serial number and the commissioning date, but the customer has to confirm it from their own mySMA account. If an inverter does not qualify for the free extension, the owner can buy a paid extension plan. For PV systems with 100 kWp or more of inverter capacity, the Flex plan runs for up to 15 years. To buy a paid extension, fill in the warranty form for your country and email it to SMA. After you pay the invoice, enter the activation code you receive against the device serial number in Product Registration. If the commissioning date conflicts with the SMA delivery date, send proof of commissioning to SMA, such as an invoice or commissioning report, and SMA will correct the warranty dates.

<!-- review notes
- sentence 2: support check: partial - Selected products get 5 extra years to 10 total with registration within 12 months, and the free program is for residential inverters, but the passages don't say registration is specifically via mySMA Product Registration and commissioning (vs purchase) wording differs.
-->
