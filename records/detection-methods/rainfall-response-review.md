---
id: method:rainfall-response-review
type: DetectionMethod
name: Rainfall response review
claims:
- claim_id: c1
  rel: produces
  target: meas:post-rain-production-recovery
  note: 'Granular dust soiling: gradual decline in irradiance-normalized output during dry periods, then
    partial or full recovery after meaningful rain or washing; months-long mild decline followed by sharp
    improvement after heavy rain.'
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.5
    h: e62247f13b95
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:no-recovery-after-rain
  note: 'Fungal bio-soiling: normalized-production deficit persists after rain but improves after manual
    cleaning, pointing to biological deposits rather than ordinary dust.'
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  review: drafted
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions, which may
    not recover after rainfall
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  review: drafted
---
Rainfall response review compares rain records with normalized production to see if a soiling loss clears when it rains. Line up rainfall, cleaning logs, SCADA output and irradiance-normalized or weather-normalized production over dry spells and the rain events that end them. Granular dust soiling shows up as a slow drop in normalized output during dry periods, followed by partial or full recovery after heavy rain or washing. Widespread fungal soiling shows up as a lasting deficit that rain does not fix but manual cleaning does, so this review helps tell biological soiling apart from ordinary dust. Before blaming soiling, rule out availability losses, clipping, curtailment and irradiance sensor problems, and do not rely on a single dirty irradiance sensor. Check the result against soiling station data and reference blocks, and confirm biofilms with close visual inspection or handheld microscopy at several array areas, because the deposits can be patchy.

<!-- review notes
- sentence 5: support check: partial - u11 and u16 cover excluding availability, clipping, curtailment and sensor issues and not relying on a single dirty sensor, but 'rule out before blaming soiling' is a slight reframing of identifying declines without those issues.
-->
