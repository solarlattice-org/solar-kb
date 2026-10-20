---
id: symptom:low-module-voc
type: Symptom
name: Low module open-circuit voltage
aliases:
- Voc
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-voc
  note: Measured Voc falls below the value expected from the datasheet, flash report, an earlier IV curve,
    or a comparable string. Causes include failed cell interconnections, cell-to-cell shorts, a shorted
    bypass diode, reversed module polarity, poor insulation, LID or PID.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  - src: src:iec-62446-1
    loc: sec=6.4
    h: c2c39f38b7e7
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h6
    h: a0a9f72d8381
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:iv-curve-step
  note: Steps in the IV curve can point to a bypass diode defect, damaged cells or heavy cell mismatch,
    and can appear together with reduced voltage.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
  review_note: 'support check: partial - Steps are linked to bypass diode defect, damaged cells, or heavy
    mismatch, but the passages do not say they appear together with reduced voltage.'
- claim_id: c3
  rel: observed_as
  target: meas:iv-sloped-isc-region
  note: In PID, lower Voc comes with a steeper slope at the current axis because shunt resistance has
    dropped.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h6
    h: a0a9f72d8381
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:el-patchwork-pattern
  note: With LID, an EL image that grows more non-uniform (patchwork) can sometimes reveal ongoing degradation.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Boron-oxygen LID in c-Si modules, within the first days of sun exposure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: disputed
  conflicts_with:
  - symptom:low-module-voc#c9
- claim_id: c6
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID, mainly in PERC modules running above 50 °C; this loss adds to the LID loss and develops
    over years
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: disputed
  conflicts_with:
  - symptom:low-module-voc#c9
- claim_id: c7
  attr: typical_power_loss
  value:
    min: 2
    max: 4
    unit: unit:PERCENT
  conditions: Initial light-induced degradation, as limited loss reported in the IV-curve failure review
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: disputed
  conflicts_with:
  - symptom:low-module-voc#c9
- claim_id: c8
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light soaking effect (LID) in general, as potential loss
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - LID losses up to 30% are stated, but the passage does not link
    this to Voc and it is an upper potential bound, not a typical value.; reviewer: the compiler-flagged
    conflict is a different scenario or technology, not disagreement'
- claim_id: c9
  attr: typical_power_loss
  value:
    nominal: 41
    unit: unit:PERCENT
  conditions: Average performance loss from PID at one 10.7 MW plant in Spain
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h4
    h: 21df64fc133e
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - The 41% average performance loss at the 10.7 MW plant in Spain
    is stated, but it is not tied to Voc.; reviewer: the compiler-flagged conflict is a different scenario
    or technology, not disagreement'
---
Low module or string open-circuit voltage means the measured Voc is below what the datasheet, flash report, an earlier IV curve or a similar string would predict. Find it with an IV trace or a string Voc measurement, and compare against a model corrected for module temperature or against identical strings under stable irradiance. Possible causes include a shorted bypass diode, failed cell interconnections, cell-to-cell shorts, light induced degradation and potential induced degradation. A shorted bypass diode lowers module voltage all the time and can heat cells unevenly, while an open diode usually shows no loss until the module is mismatched or shaded. PID typically affects modules unevenly across the field and shows a lower Voc together with a steeper IV slope near short-circuit current; EL, thermography and Voc checks help confirm it. LID appears early in the system's life as lower power, current and voltage with no visible defect, sometimes with a patchwork EL pattern. At the string level, a voltage well below expected can also mean a module wired with reversed polarity, poor insulation or water in conduits or junction boxes, so check the wiring and the number of modules in series first.

<!-- review notes
- sentence 2: support check: partial - String Voc comparison with a temperature-aware model or identical strings under stable irradiance is stated, but IV trace is only generally supported.
-->
