---
id: mit:yield-model-initial-loss
type: Mitigation
name: Initial degradation in yield model
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 0.3
    max: 1
    unit: unit:PERCENT
  conditions: Initial LID term some yield assessors add in long-term yield predictions; depends on module
    technology and location
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: disputed
  conflicts_with:
  - mit:yield-model-initial-loss#c5
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 1
    max: 2
    unit: unit:PERCENT
  conditions: First-year drop commonly assumed by PVPS Task 13 survey participants in long-term yield
    predictions
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: disputed
  conflicts_with:
  - mit:yield-model-initial-loss#c5
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Boron-oxygen LID in p-type crystalline silicon modules, within the first days of sun exposure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: disputed
  conflicts_with:
  - mit:yield-model-initial-loss#c5
- claim_id: c4
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in susceptible modules (first seen with PERC), adding to the LID loss over years
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: drafted
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 10
    max: 30
    unit: unit:PERCENT
  conditions: Amorphous silicon modules within the first months of outdoor exposure (Staebler-Wronski
    effect)
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h4
    h: c8bc75bb2d8d
  review: disputed
  conflicts_with:
  - mit:yield-model-initial-loss#c1
  - mit:yield-model-initial-loss#c2
  - mit:yield-model-initial-loss#c3
---
This action means building the expected initial light-induced power loss into the energy yield model, so that early stabilization losses are not mistaken for faults and do not inflate production forecasts. It addresses Light Induced Degradation (LID), which appears as a drop in STC power, short-circuit current and open-circuit voltage early in system life, with no visible defect. If initial degradation is under-estimated, energy yield predictions and investor expectations are directly affected. Some yield assessors add a separate initial LID term to the long-term yield prediction, sized by module technology and site location. The size of the allowance must match the technology: crystalline LID is a few percent in the first days, amorphous silicon can lose much more over the first months, and some CIS modules actually gain power. LeTID is harder to model because it develops over years, depends on module temperature and site, and may not recover within the module lifetime. There is no consensus on which degradation values to use, so pair this action with low-LID module selection, and check unexpected early losses with IV and flash testing.

<!-- review notes
- sentence 1: support check: partial - Mitigation says account for stabilization in yield assumptions, but the 'not mistaken for faults/inflate forecasts' rationale is only loosely implied.
- sentence 6: support check: partial - Passage supports years-long development, temperature/site dependence, possible non-recovery and difficulty predicting trend, but doesn't say LeTID is harder to model than LID in yield models explicitly.
-->
