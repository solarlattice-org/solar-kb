---
id: meas:normalized-output-decline
type: Measurement
name: Long-term normalized output decline
aliases:
- Performance Loss Rate
- PLR
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: weather-normalized yearly energy declines more than module warranty degradation implies
- point: model_403.InDCA
  unit: unit:A
  pattern: string currents spread apart over years as weaker modules limit strings
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used as the irradiance reference for normalization
- point: model_103.W
  unit: unit:W
  pattern: Irradiance-normalized AC power falls steadily across dry days
- point: model_307.Rain
  unit: unit:MilliM
  pattern: No rainfall during the declining period
claims:
- claim_id: c1
  attr: degradation_rate
  value:
    min: 1
    max: 2
    unit: unit:PERCENT-PER-YR
  conditions: First-year drop that yield assessors generally assumed in long-term yield predictions, per
    a PVPS Task 13 expert survey
  note: This is a modelling assumption, not a field measurement.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c2
  attr: degradation_rate
  value:
    min: 0.5
    max: 0.7
    unit: unit:PERCENT-PER-YR
  conditions: Annual rate that yield assessors assumed after the first year and up to year 5 in long-term
    yield predictions (PVPS Task 13 survey)
  note: This is a modelling assumption.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions)
- claim_id: c3
  attr: degradation_rate
  value:
    min: 0.3
    max: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Annual rate that yield assessors assumed from year 5 up to year 30 in long-term yield predictions
    (PVPS Task 13 survey)
  note: This is a modelling assumption.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions)
- claim_id: c4
  attr: degradation_rate
  value:
    nominal: 0.25
    unit: unit:PERCENT-PER-YR
  conditions: Low overall performance loss rate that some yield assessors use for crystalline silicon
    PV systems
  note: The source says there is no consensus on which proxy value to use.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions)
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 0.3
    max: 1
    unit: unit:PERCENT
  conditions: Initial light-induced degradation term that some yield assessors add; it depends on module
    technology and location
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h78
    h: f76ff6f06aa0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This signature is a slow drop in plant output over months or years, after the output has been normalized for irradiance. The decline is usually expressed as a performance loss rate in percent per year, either as a single linear rate or as rates over several time segments. The trend includes permanent module degradation as well as losses that can be reversed or avoided with good O&M. With granular dust soiling, normalized output falls during dry periods while the plant stays online, then recovers partly or fully after rain or washing. Before blaming soiling, rule out availability losses, clipping, curtailment and irradiance sensor problems, then compare the trend with soiling station data, rainfall, cleaning logs and reference blocks. When modules age at different rates, the extra mismatch can make system degradation higher than the nameplate module degradation rate. To separate average module degradation from mismatch-driven loss, compare the long-term normalized output with string or inverter trends, IV curve data and module test results. Clean and filter the data carefully, because the filtering choices change the result: high irradiance threshold filters tend to give a lower reported loss rate.

<!-- review notes
- sentence 1: support check: partial - The passages describe PLR as a decline of power output over time and soiling as a decline in irradiance-normalized production, but they don't state a general slow months-or-years drop signature.
-->
