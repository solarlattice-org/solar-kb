---
id: method:soiling-model-residuals
type: DetectionMethod
name: Soiling model residual analysis
claims:
- claim_id: c1
  rel: produces
  target: meas:normalized-output-decline
  note: Look for output falling during dry accumulation periods with no availability, clipping, curtailment
    or irradiance sensor problem to explain it.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages support looking for dry-period output decline without
    availability/clipping/curtailment/irradiance sensor issues, but not the specific signals (rain absence,
    POAI drift check) or that it is framed as a residual-analysis output.'
- claim_id: c2
  rel: produces
  target: meas:post-rain-production-recovery
  note: The recovery seen after rain is compared with the recovery the assumed soiling model predicts.
    If the two do not match, the local wash-off assumptions are wrong.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: drafted
  review_note: 'support check: partial - Passage says to test whether the model explains recovery after
    rain and update wash-off assumptions if mismatched, but doesn''t mention a step-up in normalized power
    or specific signals.'
- claim_id: c3
  rel: produces
  target: meas:post-cleaning-production-step
  note: The step seen after cleaning is compared with the step the model predicts, to check the model's
    accumulation rate.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage covers testing model against recovery after cleaning
    and updating accumulation assumptions, but not the step on the cleaning date or specific signal.'
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 28.4
    unit: unit:PERCENT
  conditions: Soiling loss with natural cleaning only (2 precipitation events, 0 cleaning events), in
    a technical-risk quantification example
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=24.r1
    h: c445e2348acf
  review: drafted
  review_note: 'support check: partial - Index row gives natural cleaning 28.4% with 2 precipitation and
    0 cleaning events, but nothing links it to soiling model residual analysis or ''typical power loss''.;
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions)'
- claim_id: c5
  attr: typical_power_loss
  value:
    nominal: 4.1
    unit: unit:PERCENT
  conditions: Soiling loss with periodic cleaning (2 precipitation events, 12 cleaning events), same example
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=24.r2
    h: 9396b4336aaa
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Row gives periodic cleaning 4.1% with 2 precipitation and 12
    cleaning events, but no link to residual analysis or ''typical''.; possible conflict with c4 (same
    source; check the conditions); possible conflict with c6 (same source; check the conditions)'
- claim_id: c6
  attr: typical_power_loss
  value:
    nominal: 2.3
    unit: unit:PERCENT
  conditions: Soiling loss with triggered cleaning (2 precipitation events, 20 cleaning events), same
    example
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=24.r3
    h: f39cb9b31f82
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Row gives triggered cleaning 2.3% with 2 precipitation and 20
    cleaning events, but no link to residual analysis or ''typical''.; possible conflict with c4 (same
    source; check the conditions); possible conflict with c5 (same source; check the conditions)'
---
Soiling model residual analysis compares measured plant output against a soiling model during dry periods, when dust builds up, to confirm granular dust soiling losses. Start with normalized production trends and find dry periods where output falls even though availability, clipping, curtailment and irradiance sensors do not explain the drop. Check that trend against soiling station data, rainfall, cleaning logs and nearby reference blocks if they are available. Some models, such as the Kimber approach, build the soiling profile from power and rainfall data. They need a minimum cleaning threshold for rain and a grace period after each rain event. Results can differ between analyses because there is no agreement on grace periods and cleaning thresholds. Global models have also correlated poorly at sites with low average soiling losses. Do not rely on one dirty irradiance sensor. Sensor drift, poor cleaning practice or a local obstruction can produce what looks like soiling but does not represent the array.

<!-- review notes
- sentence 1: support check: partial - Detection method mentions model residuals for dry accumulation periods, but doesn't say it compares measured output to a model to confirm dust soiling in these words.
- sentence 5: support check: partial - Lack of agreement on grace periods and cleaning thresholds causing differing results is stated, but global models correlating poorly at low-loss sites is overstated: the passage says two models correlated poorly with each other at sites under 5% average loss.
-->
