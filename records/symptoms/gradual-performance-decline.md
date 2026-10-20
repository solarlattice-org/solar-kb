---
id: symptom:gradual-performance-decline
type: Symptom
name: Gradual performance decline
claims:
- claim_id: c1
  rel: observed_as
  target: meas:performance-ratio-decline
  note: For dust soiling, irradiance-normalized production falls slowly through dry periods; compare performance
    ratio trends and model residuals for dry accumulation periods.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: observed_as
  target: meas:post-rain-production-recovery
  note: Soiling-driven decline is often partly or fully recovered after meaningful rain or washing.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: observed_as
  target: meas:normalized-output-decline
  note: For system vs module degradation, long-term normalized plant output and string or inverter trends
    decline faster than the module nameplate degradation rate.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  review: drafted
  review_note: 'support check: partial - Passages support comparing long-term normalized output and string/inverter
    trends and system degradation exceeding nameplate, but not the specific yearly energy or string current
    spread signals.'
- claim_id: c4
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Allowance some independent engineers add to the module degradation rate to cover mismatch
    from modules degrading at different rates; a modeling allowance, not a universal rule.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 1
    max: 2
    unit: unit:PERCENT
  conditions: Loss from glass breakage events in temperate climates, per the Herz et al. study.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c6
  attr: typical_power_loss
  value:
    min: 20
    max: 80
    unit: unit:PERCENT
  conditions: Reduction of PV string performance from potential induced degradation after commissioning,
    per Libby et al.; source states it as up to 20-80%.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h3
    h: 0587f1d564ae
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
---
A gradual performance decline is a slow fall in irradiance-normalized production while the plant stays online. Track performance ratio trends and normalized output against rain and cleaning records, soiling station data and model residuals. If the decline builds up during dry periods and recovers partly or fully after real rain or washing, dust soiling is the likely cause. Do not judge soiling from one dirty irradiance sensor, because sensor drift or local obstruction can look like soiling. A decline that lasts for years and runs faster than the module warranty rate can point to system-level degradation: modules age at different rates, and the weaker ones limit the current of their strings. To separate this from average module ageing, compare string or inverter trends, IV curve data and module test results. Broken glass may not cut power at first, but moisture getting in later speeds up corrosion and degradation, so check the rear glass visually and watch for insulation faults. Potential induced degradation usually shows up after commissioning and can strongly reduce string performance.

<!-- review notes
- sentence 3: support check: partial - Passages describe the dry-period decline with recovery after rain as the soiling signature, but do not explicitly state it as a diagnostic rule for the likely cause, and note models can misjudge.
- sentence 5: support check: partial - Passages support system degradation exceeding warranty rate due to uneven module aging and weaker modules limiting string current, but not explicitly that it lasts for years.
-->
