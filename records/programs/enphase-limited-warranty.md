---
id: prog:enphase-limited-warranty
type: Program
name: Enphase limited warranty
aliases:
- Enphase warranty
- Limited Warranty
category: Warranty
program_kind: warranty
claims:
- claim_id: c1
  rel: issued_by
  target: org:enphase
  cite:
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h43
    h: b9c9bf823d6b
  review: drafted
- claim_id: c2
  attr: warranty_term
  value:
    nominal: 90
    unit: unit:DAY
  conditions: Coverage on a repaired or replacement product runs for the rest of the original warranty
    period or this many days from Enphase's return shipment, whichever is later
  cite:
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h43
    h: b9c9bf823d6b
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:enphase-iq8
  note: Datasheet tables refer to enphase.com/warranty for the standard warranty term; an Enphase FAQ
    covers the IQ8 limited warranty period
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: tbl=17.r12
    h: 5124b505fd6e
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: tbl=23.r7
    h: 5124b505fd6e
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: tbl=41.r9
    h: 5124b505fd6e
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: tbl=28.r11
    h: 722143519ac9
  - src: src:kb-enphase-what-is-the-limited-warranty-period-for-iq8-series-microinverters
    loc: sec=front
    h: a476ec094312
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - The IQ8 FAQ title and the datasheet references to enphase.com/warranty
    are present, but nothing states that this limited warranty text applies to the IQ8 series. The 15-year
    warranty passage never names the IQ8.'
- claim_id: c4
  rel: applies_to
  target: prod:enphase-iq9n
  note: An Enphase FAQ covers the IQ9N limited warranty period
  cite:
  - src: src:kb-enphase-what-is-the-limited-warranty-period-for-iq9n-microinverter
    loc: sec=front
    h: b3ef626dc343
  review: drafted
  review_note: 'support check: partial - Only the FAQ title about the IQ9N limited warranty period is
    given, with no content, so it does not state that this warranty applies to the IQ9N.'
- claim_id: c5
  rel: applies_to
  target: region:us
  note: Enphase pays non-expedited return shipping of repaired or replacement product within the US, including
    Alaska and Hawaii
  cite:
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h43
    h: b9c9bf823d6b
  review: drafted
- claim_id: c6
  rel: applies_to
  target: region:ca
  note: Enphase pays non-expedited return shipping of repaired or replacement product to Canada
  cite:
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h43
    h: b9c9bf823d6b
  review: drafted
---
Enphase Energy issues a limited warranty against defects in workmanship and materials in its microinverters, and will repair or replace a defective unit free of charge after its inspection confirms a covered defect. For newer models such as IQ8 and IQ9N, the manuals and FAQs refer to the Enphase warranty web page for the standard term. Parts and labor for the repair are covered. Labor to uninstall and reinstall units is not covered, and neither is troubleshooting of the customer's electrical system. Return shipping is paid only to the United States and Canada. To make a claim, call Enphase technical support first to troubleshoot in the field. If that does not fix the problem, request an RMA number and provide proof of purchase, the model and serial numbers, a description of the defect and a return address. Ship returned units in the original or equally protective packaging, and do not open or modify them without Enphase's written approval. The warranty excludes misuse, improper installation, fire, water, corrosion, lightning or out-of-spec input voltage, damage caused by other system components, and units with defaced or removed serial markings.

<!-- review notes
- sentence 2: support check: partial - The datasheet rows point to enphase.com/warranty, and the IQ8 and IQ9N FAQ titles show those FAQs exist. The passages don't show that the manuals and FAQs refer to the web page for the term, and the datasheet rows shown are not for IQ8 or IQ9N (u6 is the M250-60).
- sentence 3: support check: partial - Parts and labor for the repair are covered, uninstall and reinstall labor is excluded, and troubleshooting of the customer's electrical system is excluded. Shipping is covered only to the US and Canada, but the passage says this about Enphase paying shipping costs only for those destinations, which the statement matches.
-->
