---
id: concept:demand-charge
type: Concept
name: Demand charge
aliases:
- demand charges
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:time-of-use-rate
  note: Utilities adjust both time-of-use energy rates and demand charges to address time-of-day cost
    imbalance.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h23
    h: 7c370b56f126
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9
    loc: sec=h4
    h: 037737a78a19
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:demand-response
  note: Utilities are adjusting demand charges and demand response programs together.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h23
    h: 7c370b56f126
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:battery-storage
  note: Energy storage control settings are configured to reduce demand charges.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-energy-toolbase-energy-toolbase-user-guide-for-stem-partn
    loc: tbl=2
    h: 779ad8e3ac12
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: related_to
  target: tool:stem-athena
  note: Athena Utility Bill Optimization settings list demand-charge reduction as an activated storage
    feature.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-energy-toolbase-energy-toolbase-user-guide-for-stem-partn
    loc: tbl=2
    h: 779ad8e3ac12
  review: drafted
- claim_id: c5
  rel: part_of
  target: concept:utility-rate-structures
  note: Demand charges are one element of a utility bill, alongside time-of-use rates, capacity charges
    and critical peak rates.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9
    loc: sec=h4
    h: 037737a78a19
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h24
    h: 714f66e3f0a4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The passages list demand charges alongside time-of-use rates,
    capacity charges and critical peak rates, and u12 says they are part of the bill. Neither passage
    states that they are an element of a utility rate structure; u16 is only a list of topics.'
---
A demand charge is a utility bill cost set by the highest power (kW) a customer draws over a short interval, not by the total energy used. One source describes the interval as just 15 minutes per month. Demand charges are a large and growing share of commercial bills. One source says they now make up more than 50% of a typical commercial bill, and that commercial demand charges in California have risen by 100% in the last decade. Traditional energy efficiency measures do not help a site avoid demand charges, because the charge follows short peaks in power draw. Energy storage can cut demand charges. Storage controller settings such as Stem Athena utility bill optimization can be set to reduce demand charges only, or demand and energy charges together. One storage qualification guide flags a site as a good fit when demand charges are more than 20 dollars per kW per month, or when they are more than 50% of the bill. Utilities adjust demand charges together with time-of-use energy rates and demand response programs, because energy costs more at certain times of day.

<!-- review notes
- sentence 1: support check: partial - u12 says demand charges are costs calculated by the maximum power (kW) used in just 15 minutes per month. It does not say they are not set by total energy used, and it does not describe a general short interval.
- sentence 3: support check: partial - u12 says traditional efficiency measures won't help avoid demand charges. It does not give the stated reason that the charge follows short peaks, although the 15-minute maximum-kW basis implies it.
- sentence 4: support check: partial - u23 shows settings for demand charges only and for demand plus energy charges. It does not state in general that energy storage can cut demand charges, although the settings imply it.
-->
