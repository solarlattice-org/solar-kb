---
id: meas:no-recovery-after-rain
type: Measurement
name: No recovery after rain
signals:
- point: model_307.Rain
  unit: unit:MilliM
  pattern: rainfall event recorded
- point: model_103.W
  unit: unit:W
  pattern: normalized production deficit unchanged after rain; step-up only after manual cleaning
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used to normalize output
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Fungal bio-soiling in humid subtropical regions; the loss persists and may not recover after
    rainfall
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
This signature is a normalized-production deficit that stays in place after rain instead of recovering. To check for it, compare irradiance-normalized or weather-normalized production before and after rain events, and line it up with rainfall data and cleaning records. Ordinary granular dust soiling usually works the other way: output falls during dry spells, then partly or fully recovers after meaningful rain or washing. If the deficit survives rain but improves after manual cleaning, biological soiling such as fungal biofilm is more likely than ordinary dust. Strong supporting evidence is a repeatable step up in production after cleaning, especially where rain had not brought output back to the expected level. Biological deposits can be patchy, so inspect several array areas closely or with a handheld microscope rather than relying on one module. If module glass is still visibly dirty after a rain event, for example after smoke exposure, a cleaning protocol is advised.

<!-- review notes
- sentence 2: support check: partial - Passages say to compare normalized production before/after cleanings, and review rainfall response and cleaning records, but not specifically comparing before and after rain events.
-->
