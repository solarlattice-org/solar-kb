---
id: mit:regular-cleaning
type: Mitigation
name: Regular cleaning
aliases:
- Module cleaning
- Periodic Cleaning
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.91
    unit: unit:PERCENT
  conditions: Annual soiling loss with no cleaning, simulated system in Mesa, Arizona (Naeem 2014)
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - 1.91% is the annual soiling loss with no cleaning in Mesa per
    Naeem, but labeling it as ''regular cleaning'' typical loss is a mismatch, though the condition describes
    no cleaning.; possible conflict with c2 (same source; check the conditions); possible conflict with
    c3 (same source; check the conditions); possible conflict with c4 (same source; check the conditions)'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 1.52
    unit: unit:PERCENT
  conditions: Annual soiling loss with one cleaning per year, simulated system in Mesa, Arizona (Naeem
    2014)
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 1.32
    unit: unit:PERCENT
  conditions: Annual soiling loss with two cleanings per year, simulated system in Mesa, Arizona (Naeem
    2014)
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Annual soiling loss with three cleanings per year, simulated system in Mesa, Arizona (Naeem
    2014)
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions)
---
Regular cleaning means removing built-up soiling from the module front surface on a set schedule or when a measured condition calls for it. Its main purpose is to limit soiling losses. One PID guide also lists it as a way to lower the risk of Potential Induced Degradation, because dust can carry positive charge. If cleans are spaced too far apart, bird droppings can etch the glass and lichen can grow, and both are very hard to remove. Cleaning can be manual, robotic or mechanical. Use ultra-pure water and biodegradable detergent, follow the module warranty, and do not use high-pressure water, brushes, solvents or abrasives. Set the cleaning frequency for each site, since rainfall, soiling rate, energy price and labour cost all change whether cleaning pays off. In some wet European regions it may not be cost-effective at all. In a 10 MWp plant in Abu Dhabi, periodic cleaning cut the monetised yield loss well below natural cleaning by rain alone. Cleaning triggered by measured soiling gave a slightly lower total cost. Soiling left by dust storms is harder to remove and may need several cleaning runs. Active cleaning can also wear the anti-reflective coating, which costs a small amount of efficiency.

<!-- review notes
- sentence 2: support check: partial - PID guide lists regular cleaning to minimize PID risk due to positive charge from dust, and soiling losses are implied, but 'main purpose' and 'one PID guide' framing is only loosely supported; 'lower risk' is stated.
-->
