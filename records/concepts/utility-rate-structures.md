---
id: concept:utility-rate-structures
type: Concept
name: Utility rate structures
aliases:
- flat rate
- tiered rate
- rate schedule
- tariff
- rate structure
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:time-of-use-rate
  note: Time of use is one of the basic rate structures; the price per kWh changes with high-demand periods
    of the day.
  cite:
  - src: src:se-academy-solar-101-na-residential-sales-05-solar-101-lesson-4-utility-bill-basics
    loc: sec=h4
    h: ad98c31714b6
  - src: src:se-academy-successful-selling-series-for-residential-sales-te-04-successful-selling-series-bill-review
    loc: sec=h11
    h: 12726134be61
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h23
    h: 7c370b56f126
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: related_to
  target: concept:demand-response
  note: Utilities are changing demand response programs together with TOU rates and demand charges; tariff-based
    DR programs are moving to different times and rate structures.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h23
    h: 7c370b56f126
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h30
    h: c21bb7df886f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: related_to
  target: concept:net-metering
  note: A site that exports power may be billed under a different rate structure, such as a net metering
    program with non-bypassable charges.
  cite:
  - src: src:se-academy-successful-selling-series-for-residential-sales-te-04-successful-selling-series-bill-review
    loc: sec=h6
    h: cd55a36bc88c
  - src: src:eq-equip-bess-tesla-opticaster-overview
    loc: sec=front
    h: 6f38a75b0d21
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: related_to
  target: func:peak-shaving
  note: Battery control software uses the tariff it is given to plan peak shaving and energy shifting
    that lower utility charges.
  cite:
  - src: src:eq-equip-bess-tesla-opticaster-overview
    loc: sec=front
    h: 6f38a75b0d21
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: related_to
  target: tool:tesla-opticaster
  note: To be configured, Opticaster needs the current utility tariffs and billing cycles.
  cite:
  - src: src:eq-equip-bess-tesla-opticaster-overview
    loc: sec=front
    h: 6f38a75b0d21
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:power-purchase-agreement
  note: In monitoring platforms, PPA rates are set up in the same rate-schedule configuration as utility
    rates.
  cite:
  - src: src:alsoenergy-kb-how-to-add-a-utility-rate-or-ppa-rate-to-a-site
    loc: sec=front
    h: 60b85f017e9a
  review: drafted
- claim_id: c7
  rel: related_to
  target: prod:ge-kv2c
  note: The meter software sets a TOU schedule using rate types, seasons and rates A to F or Non-TOU.
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-metermate-5-51-files-software-instruction-manuals-geh-7273j-mmlp
    loc: sec=1.3.5
    h: 61aab08c059f
  - src: src:eq-equip-meters-ge-kv2c-meters-metermate-5-51-files-software-instruction-manuals-geh-7273j-mmlp
    loc: tbl=18
    h: 35bbb4be8ee4
  review: drafted
  review_note: 'support check: partial - Passages describe TOU schedule with rate types, seasons and rates
    A–F/Non-TOU, but do not tie it to the GE kV2c meter specifically.'
---
A utility rate structure is the way an electricity company bills its customers for the energy they use. Under a flat or fixed rate, the customer pays the same price for every kWh. Under a tiered rate, the price per kWh goes up as the customer uses more electricity. Under a time-of-use rate, the price per kWh changes with the time of day and is higher during high-demand periods. A full rate schedule can include energy charges, demand charges, fixed charges, seasons and time-of-use periods. Its format varies with the utility territory, the customer type and the service voltage. Demand charges are often based on the highest peak in each billing cycle, and a billing cycle does not always start on the first day of the month. A site that exports power may fall under a different rate structure from its original tariff, so battery control software also needs the sell tariff. Storage controllers use the configured tariff to plan peak shaving and energy shifting. If the tariff changes, the rate schedule in the controller has to be updated. Utilities are adjusting time-of-use rates, demand charges and demand response programs as energy becomes more expensive at certain times of day.
