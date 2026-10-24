---
id: concept:c-rate
type: Concept
name: C-rate
aliases:
- charge rate
- continuous vs peak battery power
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:battery-storage
  note: C-rate describes how fast a battery is charged or discharged relative to its rated capacity.
  cite:
  - src: src:iea-pvps-iea-pvps-t13-35-2026-report-pv-bess-2026
    loc: tbl=1.r13
    h: 24823a35e97a
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h630
    h: 841ae497ca41
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:power-vs-energy
  note: Battery spec sheets separate continuous power from surge (peak) power.
  cite:
  - src: src:se-academy-solaredge-nexis-sales-certification-na-residential-03-brush-up-on-solar-batteries-nexis
    loc: sec=h6
    h: 0cfb7b876cd7
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h13
    h: 8e9120c54e0d
  review: drafted
  review_note: 'support check: partial - Passages cover continuous vs peak power on spec sheets but never
    link C-rate to power vs energy.'
---
C-rate tells you how fast a battery can be charged or discharged. A battery's nominal capacity always comes with the discharge time it was measured at. Stationary batteries are usually rated by their C10 capacity, which is the capacity over a 10-hour discharge. For example, a battery rated C10 = 200 Ah can be discharged for 10 hours at 0.1 × C10, which is a nominal current of 20 A. The capacity you get depends on the discharge time. SMA gives factors to estimate C10 from other ratings: C10 = C100 / 1.25, C10 = C5 / 0.88 and C10 = C1 / 0.61. Battery and inverter spec sheets list continuous power separately from surge (peak) power. Peak power covers short events such as starting large appliances. The Sunny Island 4548-US shows this split: it is rated 4,500 W continuous and 11,000 W for 3 seconds at 25°C. Its continuous charging current is 85 A, and its maximum charging current is 110 A.

<!-- review notes
- sentence 5: support check: partial - Passages show continuous vs surge/peak power on spec sheets, but nothing about inverter spec sheets or peak covering short events like starting appliances beyond the washer/dryer image title.
-->
