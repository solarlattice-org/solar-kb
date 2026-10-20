---
id: stressor:partial-shading
type: Stressor
name: Partial shading
aliases:
- Module shading
- Shading
- shadowing
- partial cell shading
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 5
    unit: unit:PERCENT
  conditions: Typical cumulative annual shading loss of PV systems
  quote: Typically, the cumulative annual shading loss of PV systems is between 1-5%
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Energy loss observed on rooftop or facade PV systems
  note: Source wording is 'up to 20-30%'; the lower figure of the range is 20%.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage says energy losses up to 20-30% for rooftop/facade systems,
    but the statement''s ''typical power loss up to 30%'' frames an upper bound as typical and these are
    energy losses.'
- claim_id: c3
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: Hot cell above module temperature in an IBC half-cell module during an indoor hot-spot test
    with partial cell shading at 55°C module temperature
  note: IBC cells act as a built-in bypass diode; PERC and SHJ modules ran much hotter under the same
    test.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Partial shading happens when part of a cell or module gets less sunlight because something blocks it. Common causes are trees, poles, chimneys, nearby buildings, cables, soiling, or the next row of modules. Cells and modules are wired in series, so the power lost is much larger than the shaded area alone would suggest. The shade pattern moves with the time of day and the season. A shaded cell can be pushed into reverse bias. It then uses up power and heats, which can create a hot spot or hot cell. Hot spots from long-lasting shade can lead to burn marks, bypass diode failure, glass breakage, arcing or fire. They can also speed up module aging. Frequent shading keeps bypass diodes running hot, which raises their failure rate. Hot spots from shading also add thermomechanical stress that fatigues cell interconnections. Hot cells caused by shading can also lead to discoloration, cell cracks, delamination and loss of electrical insulation. You can find shading by looking at the array, by comparing monitoring data from shaded and unshaded strings, or by running shading simulations. Infrared thermography can also help. Shading is best handled at the planning stage. Options include string and module layout, module-level power electronics, MPPT settings, and shade-tolerant modules such as half-cell or back-contact designs.
