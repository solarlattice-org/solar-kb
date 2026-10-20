---
id: mit:forecast-update
type: Mitigation
name: Production forecast update
aliases:
- project revenue forecasts
- long-term energy assumptions
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent fungal bio-soiling in humid subtropical regions; loss may not recover after rainfall,
    which is why forecasts should be updated
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
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Added annual production loss when gust-driven tracker stow is accounted for, compared with
    models using only hourly wind data
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c3
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Allowance some independent engineers add to the module degradation rate to represent mismatch
    when estimating system degradation
  note: A modeling allowance, not a universal rule; site measurements and string or IV data should be
    used when available.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
A production forecast update revises the expected energy and revenue of a plant once field evidence shows that the original model assumptions do not match actual behavior. It applies to flawed PAN file yield losses when independent testing reveals material differences in module parameters from the file used for financing or design. For widespread fungal soiling losses, forecasts should be based on site cleaning results instead of assuming that rain resets the loss, because bio-soiling can cause persistent losses that do not recover after rainfall. For system degradation vs module degradation, the long-term energy assumptions should be updated with field measurements and model degradation at system level, including the mismatch from modules aging at different rates. For tracker wind stow production losses, compare actual annual stow hours with the energy model assumptions and update forecasts and variance reporting if recurring gust-driven stow was not modeled. Before changing loss assumptions, separate the issue from real operational faults, clipping, curtailment and outages, and document the uncertainty when only low-resolution data is available. Updating the forecast does not recover the lost energy; it only makes expectations and reporting reflect the loss. Physical actions such as cleaning or tracker settings must be handled separately and stay within structural limits.

<!-- review notes
- sentence 1: support check: partial - Passages describe updating forecasts when evidence (cleaning results, stow hours, independent testing) differs from model assumptions, but do not define it explicitly as revising expected energy and revenue generally.
- sentence 6: support check: partial - Passages support separating stow loss from clipping, curtailment, outages and documenting uncertainty with low-resolution data, but the general framing across all issues and 'real operational faults' is only partly stated (PAN note separates from operational losses).
- sentence 7: support check: partial - Passages support cleaning as separate maintenance and not lowering stow thresholds beyond structural limits, but do not explicitly state that forecast updates do not recover energy and only align expectations.
-->
