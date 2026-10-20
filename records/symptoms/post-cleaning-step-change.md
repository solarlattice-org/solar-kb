---
id: symptom:post-cleaning-step-change
type: Symptom
name: Production step after cleaning
aliases:
- production step-change after cleaning
claims:
- claim_id: c1
  rel: observed_as
  target: meas:post-cleaning-production-step
  note: Weather-normalized production rises in a step when cleaning records are overlaid on SCADA and
    irradiance data; strongest evidence for biological soiling when rain had not restored expected output.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:post-rain-production-recovery
  note: For granular dust, normalized output recovers partly or fully after meaningful rain as well as
    after washing, which separates it from bio-soiling.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: drafted
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent fungal bio-soiling losses at North Carolina solar farms (humid subtropical climate),
    recoverable only by manual cleaning; 2024 field work
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  review: drafted
---
This symptom is a clear, repeatable rise in weather-normalized production right after the array is cleaned. You find it by lining up cleaning records against SCADA, irradiance and normalized output. If the deficit stayed in place through rain but went away after manual cleaning, suspect widespread fungal soiling (sub-aerial biofilms) rather than ordinary dust. Granular dust soiling looks different. Output declines gradually through dry periods, then recovers partly or fully after meaningful rain as well as after washing. Bio-soiling is easy to mistake for dust, pollen or a weather-normalization error. In North Carolina it caused persistent losses of 5-11%. Before blaming soiling, check the dry-period decline against availability, clipping, curtailment and irradiance sensor problems. Do not rely on one dirty irradiance sensor to measure the loss. If the contaminant type matters, inspect closely or use a handheld microscope, and check several areas of the array, because biological deposits can be patchy. Where the step after cleaning keeps recurring, update the soiling model and production forecasts using the site's actual cleaning results, not the assumption that rain resets the loss.
