---
id: mit:system-level-degradation-model
type: Mitigation
name: System-level degradation modeling
claims:
- claim_id: c1
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Allowance that some independent engineers add on top of the module degradation rate to cover
    mismatch when modules degrade at different rates; a modeling allowance, not a universal rule
  note: Extra system-level loss per year on top of module degradation, not a module degradation rate by
    itself.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c2
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Default module degradation to assume for new crystalline silicon products when the manufacturer
    gives no value; current rates are often of this order
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=6.8
    h: 385ae00dd135
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c3
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Degradation rate assumed by one monitoring platform's performance waterfall; faster or slower
    degradation is shown as a positive or negative loss
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h11
    h: 84a06d8db5ac
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
---
System-level degradation modeling means putting the degradation of the whole plant into the performance model, not just the nameplate degradation rate of the modules. It addresses System Degradation vs Module Degradation. Modules age at different rates, and the weaker ones can limit the current of the strings or substrings around them. Because of this mismatch, plant energy can fall faster than the average module's power loss, even while the average module is still within warranty. The model should include the spread between modules and the mismatch loss this spread adds at the circuit level. Where possible, refine the assumption with site measurements, module technology, warranty terms, and IV curve or string-level data. Use field results to update long-term energy forecasts. Some module-level power electronics can reduce the added mismatch loss. Measuring degradation losses accurately takes more than two years of data.
