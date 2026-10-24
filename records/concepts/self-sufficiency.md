---
id: concept:self-sufficiency
type: Concept
name: Self-sufficiency
aliases:
- autarky
- energy autonomy
- energy self-sufficiency
- internal power supply
category: Storage
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: metric:self-sufficiency-rate
  note: 'SMA calls the metric the self-sufficiency quota: the ratio of internal power supply to consumption
    over a day, month, year or the total period.'
  cite:
  - src: src:sma-doc-259463
    loc: tbl=26.r1
    h: dd20ec4c67aa
  - src: src:sma-doc-246498
    loc: tbl=31.r4
    h: 9ed6514fb98e
  - src: src:sma-doc-259463
    loc: sec=h12
    h: e335bc35e8dc
  - src: src:sma-doc-262631
    loc: tbl=23.r3
    h: a4d19d2bc27f
  - src: src:sma-doc-262660
    loc: sec=h70
    h: 71a353f01bdb
  - src: src:sma-doc-262660
    loc: sec=h75
    h: 8fb2d082397d
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:self-consumption
  note: Changing the ratio of PV generation to demand raises either the self-sufficiency quota or the
    self-consumption quota, not both.
  cite:
  - src: src:sma-doc-259463
    loc: sec=2.3
    h: f540e6e5eea1
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
- claim_id: c3
  rel: related_to
  target: metric:self-consumption-rate
  note: Undersized PV gives a high self-consumption quota and a low self-sufficiency quota. Oversized
    PV gives the opposite.
  cite:
  - src: src:sma-doc-262631
    loc: tbl=23.r3
    h: a4d19d2bc27f
  - src: src:sma-doc-259463
    loc: sec=2.3
    h: f540e6e5eea1
  - src: src:sma-doc-262660
    loc: sec=h70
    h: 71a353f01bdb
  review: drafted
- claim_id: c4
  rel: related_to
  target: comp:battery-storage
  note: Battery discharging counts toward internal power supply. Storage and load-profile matching are
    the ways to raise both quotas together.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=31.r4
    h: 9ed6514fb98e
  - src: src:sma-doc-259463
    loc: sec=2.3
    h: f540e6e5eea1
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:feed-in-tariff
  note: Falling feed-in tariffs moved system design away from maximizing generation and toward self-consumption
    and self-sufficiency.
  cite:
  - src: src:sma-doc-259463
    loc: sec=2.1
    h: cd713234db18
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
---
Self-sufficiency means covering as much of a site's own energy demand as possible with its own PV energy, ideally covering all of it. It is measured by the self-sufficiency quota: internal power supply divided by consumption. Monitoring shows this quota for a day, a month, a year or the total period. Internal power supply is the energy the household takes directly from its PV system plus any energy it draws from the battery. Without a battery, internal power supply equals self-consumption. Self-sufficiency trades off against self-consumption. A PV system much larger than the annual demand raises self-sufficiency but lowers the self-consumption quota, and a much smaller system does the reverse. To raise both quotas together, you need battery storage or a load profile that matches the PV production curve, because the array's alignment and the weather largely fix when PV power is available. High self-sufficiency protects the operator against rising electricity prices and lowers the average cost of each kilowatt hour used. It pays off once PV generation costs are lower than the cost of buying power from the grid. Energy managers such as the Sunny Home Manager work toward this goal by switching loads on when PV energy is available.
