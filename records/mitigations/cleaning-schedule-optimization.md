---
id: mit:cleaning-schedule-optimization
type: Mitigation
name: Cleaning schedule optimization
aliases:
- Best-Time-to-Clean models
- optimal cleaning schedule
- cleaning frequency optimization
- optimal cleaning interval
- Triggered Cleaning
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.91
    unit: unit:PERCENT
  conditions: Annual soiling loss with no cleaning, simulated for a system in Mesa, Arizona (Naeem 2014)
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'possible conflict with c2 (same source; check the conditions); possible conflict with
    c3 (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); reviewer: the compiler-flagged conflict
    is a different scenario or technology, not disagreement'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 1.52
    unit: unit:PERCENT
  conditions: Annual soiling loss with one cleaning per year, same Mesa, Arizona simulation
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'possible conflict with c1 (same source; check the conditions); possible conflict with
    c3 (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); reviewer: the compiler-flagged conflict
    is a different scenario or technology, not disagreement'
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 1.32
    unit: unit:PERCENT
  conditions: Annual soiling loss with two cleanings per year, same Mesa, Arizona simulation
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'possible conflict with c1 (same source; check the conditions); possible conflict with
    c2 (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); reviewer: the compiler-flagged conflict
    is a different scenario or technology, not disagreement'
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Annual soiling loss with three cleanings per year, same Mesa, Arizona simulation
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'possible conflict with c1 (same source; check the conditions); possible conflict with
    c2 (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); reviewer: the compiler-flagged conflict
    is a different scenario or technology, not disagreement'
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 4.3
    max: 7.5
    unit: unit:PERCENT
  conditions: Reported annual soiling losses across studies, where special soiling conditions require
    scheduled cleaning
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h69
    h: c3545479b8b9
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions, which should
    be included in cleaning schedules
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
---
Cleaning schedule optimization means picking when and how often to clean modules so the value of energy recovered outweighs the cost of cleaning. It addresses soiling losses, including granular dust soiling and fungal bio-soiling, where cleaning triggers should be set by the value of the lost energy. The simplest rule is to clean once the revenue lost to soiling exceeds the cost of a cleaning, but more detailed models also account for free cleaning by rain, wind or dew. Key inputs are cleaning cost, soiling accumulation rate, capacity factor, electricity price and module efficiency, so the schedule must be set per site and may vary by season or by area within a site. Soiling sensors or real-time soiling data, together with a soiling model calibrated against operational data, help decide the most profitable time to clean. In one Abu Dhabi plant comparison, triggered cleaning gave the lowest total cost, below both periodic cleaning and relying on natural cleaning. Limits: rain right after a triggered cleaning can make the benefit hard to judge, and advanced models are harder to apply because soiling and rainfall vary from year to year. Where persistent fungal deposits are present, treat cleaning as required maintenance and do not assume rain will restore output.

<!-- review notes
- sentence 5: support check: partial - Real-time soiling data/sensors and soiling models are supported for deciding best time to clean, but calibration against operational data is only in the diagnostic workflow (updating model if mismatched), loosely stated.
-->
