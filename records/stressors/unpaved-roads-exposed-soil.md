---
id: stressor:unpaved-roads-exposed-soil
type: Stressor
name: Unpaved roads and exposed soil
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 6.9
    unit: unit:PERCENT
  conditions: Monthly soiling power loss at a plant built on sandy soil in the countryside of Southern
    Italy
  note: The same source reports 1.1% monthly loss for a plant on more compact soil.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: 'support check: partial - The 6.9% monthly loss on sandy soil in rural Southern Italy is
    stated, but the passage doesn''t link it to "unpaved roads and exposed soil" as a category or call
    it a typical value.; possible conflict with c2 (same source; check the conditions)'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 1.1
    unit: unit:PERCENT
  conditions: Monthly soiling power loss at a plant built on more compact soil in the countryside of Southern
    Italy
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: 'support check: partial - The 1.1% monthly loss on more compact soil is stated, but the
    passage doesn''t frame it as unpaved roads/exposed soil typical loss.; possible conflict with c1 (same
    source; check the conditions)'
---
Unpaved roads and exposed soil near or inside a PV array are local dust sources, and they can make granular dust soiling losses uneven across the site. Dust that settles on the module glass scatters and absorbs light, so module current and plant output drop, and patchy deposits can cause mismatch between strings or substrings. Utility-scale sites often have access roads running through the array, built during civil construction, and these roads need regular maintenance. Exposure is high during construction, when graded sites usually have no ground cover and unmated connectors can be exposed to dust and moisture. Soil type matters: one Italian study found much higher soiling losses at a plant on sandy soil than at a plant on more compact soil. To reduce exposure, establish low-growing vegetation as ground cover early in operation and limit grading, and use polymer soil conditioners to stabilize bare soil surfaces. Remaining dust can be managed with cleaning schedules that are cost-effective, anti-soiling coatings, and trackers that can tilt to steep angles.

<!-- review notes
- sentence 1: support check: partial - The passage says roads and exposed soil can make soiling loss spatially uneven, but it doesn't say they are local dust sources or that they sit near or inside the array.
-->
