---
id: mit:manual-cleaning
type: Mitigation
name: Manual cleaning
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions, which may
    not recover after rainfall
  note: This is the loss that cleaning addresses, not a figure for how well cleaning works.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages give a 5-11% persistent loss from fungal bio-soiling
    in humid subtropical regions that may not recover after rain, but not that it is a ''typical'' loss;
    also it is described as an impact factor, not a manual-cleaning figure.; reviewer: the compiler-flagged
    conflict is a different scenario or technology, not disagreement'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 1.91
    unit: unit:PERCENT
  conditions: Annual soiling loss without cleaning, simulated for a system in Mesa, Arizona (Naeem 2014)
  note: In the same simulation, one cleaning a year cut the loss to 1.52 %/yr, two to 1.32 %/yr and three
    to 1.20 %/yr.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h68
    h: aa451386499f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - The 1.91% annual soiling loss in Mesa and the 1.52/1.32/1.20
    %/yr reductions are stated, but the passage does not say 1.91% is the loss without cleaning explicitly
    as ''manual cleaning typical power loss''; it is the baseline with rain only and cleaning is not stated
    to be manual.; reviewer: the compiler-flagged conflict is a different scenario or technology, not
    disagreement'
---
Manual cleaning means crews wash module glass by hand to remove soiling, usually with water. It is the targeted fix for Widespread Fungal Soiling Losses. Black fungal biofilms stick to the glass and stay there through rain until someone cleans them off. On sites with persistent biological deposits, treat cleaning as required maintenance and put bio-soiling in the cleaning schedule. A simple, economical method is a bucket of water with a strip cleaner and squeegee, using overlapping vertical strokes. Do not use high-pressure water, brushes, solvents, abrasives or harsh detergents. Make sure the method fits the module maker's warranty. Use high-purity water, and if detergents are used they must be biodegradable. Check that cleaning worked by comparing cleaning records with normalized production. A repeatable step up in output after cleaning, where rain had not restored it, confirms the effect. Limits: hand cleaning is costly and slow, so whether it pays depends on local soiling rate, energy value and labour cost. Long gaps between cleans let lichen take hold, and lichen is very hard to remove.

<!-- review notes
- sentence 5: support check: partial - Warranty fit and biodegradable detergents are stated, and ultra-pure water is required, but 'if detergents are used' is a minor paraphrase; also detergents must comply with local regulations, which is omitted, so only minor detail is missing.
-->
