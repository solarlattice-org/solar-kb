---
id: stressor:uv-exposure
type: Stressor
name: UV exposure
aliases:
- UV
- Ultraviolet
- Ultra Violet
- UV radiation
- UV irradiation
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 0.5
    max: 8
    nominal: 3
    unit: unit:PERCENT
  conditions: 14 TOPCon module types after an accelerated UV dose of 60 kWh/m² under short-circuit conditions
    (Gebhardt et al.); nominal is the median
  note: The authors say a 60 kWh/m² dose matches about 1 to 2 years outdoors, depending on location. Field
    loss may be lower because modules run at maximum power point, not short circuit.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 0
    max: 10
    unit: unit:PERCENT
  conditions: 28 TOPCon module types after an accelerated UV dose of 60 kWh/m² under short-circuit conditions
    (Shina)
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage gives 0-10% for 28 TOPCon at 60 kWh/m² short-circuit,
    but it is a range with no stated typical/median value.'
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 1
    max: 2.5
    unit: unit:PERCENT
  conditions: 2 SHJ module types after an accelerated UV dose of 60 kWh/m² under short-circuit conditions
    (Shina)
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c4
  attr: typical_power_loss
  value:
    min: 5
    unit: unit:PERCENT
  conditions: Some monocrystalline modules after long-term indoor UV exposure of 150 kWh/m² or more, often
    together with EVA browning
  note: In one test, one of five modules lost more than 5% after 160 kWh/m². No module reached 5% at the
    15 kWh/m² IEC 61215 dose.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.3.2
    h: 7ac5ae6f2098
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage supports >5% for one of five modules at 160 kWh/m², <5%
    at 15 kWh/m², and EVA browning; but ''some modules'' at 150+ is potential, and the ''indoor'' 160
    test is single-module, so ''at least 5%'' typical is overstated.; reviewer: the compiler-flagged conflict
    is a different scenario or technology, not disagreement'
---
UV exposure means the ultraviolet part of sunlight hitting the plant. It is only a small share of global irradiation, and its strength depends on climate and altitude, with higher annual doses at high-elevation sites. UV breaks down polymers such as EVA encapsulant and backsheets. This shows up as yellowing or browning of the encapsulant, along with power loss. UV can also weaken the bond between the encapsulant and the glass, which can lead to delamination. This can happen on its own or as a secondary effect after the encapsulant becomes brittle. In modern TOPCon, heterojunction and PERC cells, UV can damage the cell surface passivation. This UV-induced degradation lowers current or voltage. Exposed DC cables can crack when their insulation degrades under UV, even when the cable is certified for UV. This can cause insulation faults, and the cable then has to be replaced. Damage builds up faster when high UV comes with high module temperature, which is why hot, arid sites carry more risk. To reduce exposure, protect exposed wiring from sunlight. Choose modules whose antireflective coating, glass, encapsulant or passivation layers reflect or absorb UV before it reaches the cell.

<!-- review notes
- sentence 3: support check: partial - Passages say UV alone can cause adhesion loss and delamination (EVA-glass debonding) and delamination as secondary effect of embrittlement, but no explicit statement about weakening the bond as described beyond that.
- sentence 6: support check: partial - Passages say temperature accelerates UV photodegradation and arid zone predicted severe degradation due to higher temperatures, but 'hot, arid sites carry more risk' with high UV is only loosely stated.
-->
