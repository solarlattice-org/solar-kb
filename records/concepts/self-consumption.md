---
id: concept:self-consumption
type: Concept
name: Self-consumption
aliases:
- self-use
- own consumption
category: Storage
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:feed-in-tariff
  note: Self-consumption is attractive when the feed-in tariff is well below the grid purchase price;
    high self-consumption reduces dependence on the feed-in tariff.
  cite:
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  - src: src:sma-doc-259463
    loc: sec=2.2
    h: dc218d62571e
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:self-sufficiency
  note: Internal power supply counts battery discharging, while self-consumption counts battery charging;
    without a battery the two are equal.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h94
    h: 4e2a959105d9
  - src: src:sma-doc-246498
    loc: tbl=31.r4
    h: 9ed6514fb98e
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
  review_note: 'support check: partial - Passages say internal power supply (self-sufficiency) includes
    battery discharging, self-consumption includes battery charging, and they are equal without a battery.
    ''Counts'' is fine, but the relation to self-sufficiency is given via internal power supply and the
    quota.'
- claim_id: c3
  rel: related_to
  target: metric:self-consumption-rate
  note: 'Self-consumption is quantified by the self-consumption quota or rate: self-consumption relative
    to PV power or yield.'
  cite:
  - src: src:sma-doc-259463
    loc: tbl=26.r7
    h: e6cff3f9975d
  - src: src:sma-doc-259463
    loc: sec=h12
    h: e335bc35e8dc
  - src: src:sma-doc-262631
    loc: tbl=23.r3
    h: a4d19d2bc27f
  - src: src:sma-doc-262660
    loc: sec=h70
    h: 71a353f01bdb
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: related_to
  target: func:self-consumption-optimization
  note: Energy management switches controllable loads on when enough PV energy is available.
  cite:
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  - src: src:sma-doc-259463
    loc: sec=2.2
    h: dc218d62571e
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
- claim_id: c5
  rel: related_to
  target: comp:battery-storage
  note: Battery charging from PV counts as part of self-consumption, and storage raises the self-consumption
    quota.
  cite:
  - src: src:sma-doc-259463
    loc: tbl=26.r6
    h: e9e164204890
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=39.r1
    h: e9e164204890
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: drafted
- claim_id: c6
  rel: related_to
  target: comp:energy-meter
  note: Meters must be placed so household loads consume PV energy before the grid-connection point.
  cite:
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:peak-shaving
  note: Setting both the consumption limit and the feed-in limit to 0 gives classic increased self-consumption
    without peak-load shaving.
  cite:
  - src: src:sma-doc-278879
    loc: sec=h92
    h: f77755baab0a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: prod:sma-sunny-home-manager
  cite:
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  - src: src:sma-kb-pv-energy-for-internal-power-supply-and-self-consumption
    loc: sec=h1
    h: f7d9b949428a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Self-consumption means that PV power is used at the same site where it is generated. It includes energy used directly by loads and energy used to charge a battery. PV energy goes to active household loads first, and only the surplus is exported to the utility grid. For this reason, energy meters must be placed so that loads draw PV energy before the feed-in point. Self-consumption is different from internal power supply, also called self-sufficiency. Internal power supply counts battery discharging instead of battery charging. In systems without a battery, the two values are the same. The self-consumption quota, or rate, compares self-consumption with PV power or yield. Monitoring can show it for a day, a month, a year or the whole system lifetime. High self-consumption pays off when the feed-in tariff is well below the price of grid electricity. It also lowers energy costs and reduces the load on the grid. Energy managers such as the Sunny Home Manager raise self-consumption by switching controllable loads on when there is enough PV power. Battery storage raises it further. In an SMA example home with a natural self-consumption of 30%, load control raised the quota to about 45%. A 5 kWh battery system raised it to about 65%.
