---
id: concept:albedo
type: Concept
name: Albedo
aliases:
- ground reflectance
- ALB
- GroundReflectivity
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:bifaciality
  note: Ground-reflected light matters most for bifacial modules; reflected light on the back side drives
    bifacial gain.
  cite:
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=h1
    h: 51a013571760
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h9
    h: 51a013571760
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h89
    h: f25a1646a5d5
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:diffuse-irradiance
  note: In the PowerTrack model, the albedo factor sets how much of the diffuse irradiance the array cannot
    see is added back to total irradiance.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=h1
    h: ef0a908d0b49
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h5
    h: ef0a908d0b49
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h11
    h: 0abc2ac11bd0
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=h3
    h: ef265a4b7f39
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: Ground-reflected in-plane irradiance depends on albedo and module tilt; it is low at moderate
    tilt angles.
  quote: Gg= αGh(1-cos(β))/2
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: fig=142
    h: 36ebd5b244dd
  - src: src:iea-pvps-t13-25-2022
    loc: fig=180
    h: 946dc13fbee6
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h89
    h: f25a1646a5d5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: concept:global-horizontal-irradiance
  note: Ground-reflected irradiance is calculated from horizontal irradiance multiplied by albedo; GHI
    and albedo pyranometers have similar siting rules.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: fig=142
    h: 36ebd5b244dd
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=h56
    h: 668f0f8c38d3
  review: drafted
- claim_id: c5
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: The PowerTrack PV model uses an albedo factor and a user-set GroundReflectivity constant; albedo
    sensor data is not used in model calculations.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=h1
    h: ef0a908d0b49
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h18
    h: f01f02f869ca
  review: drafted
  review_note: 'support check: partial - Albedo factor, GroundReflectivity constant and unused albedo
    sensor data are stated, but the passages never name PowerTrack explicitly (u10 only gives the hardware
    setting).'
---
Albedo is the share of sunlight that the ground reflects. Some of that reflected light can reach the PV array. For monofacial modules, ground-reflected irradiance is usually a small contribution. It matters much more for bifacial modules, because reflected light on the back side is the main source of bifacial gain. A common estimate gives ground-reflected irradiance as albedo times horizontal irradiance times (1 minus the cosine of tilt), divided by two. This means the contribution grows with tilt and is quite low at moderate tilt angles. White surfaces such as snow can push albedo close to one. Fresh snow often beats other white surfaces because new snowfall covers any soiling. In performance models such as PowerTrack, an albedo factor sets how much of the diffuse light the array cannot see is added back to the total irradiance. A separate ground reflectivity constant has a default value of 0.1. To measure albedo, mount a pyranometer level, facing down, 1.5 to 2 m above ground that matches the ground under the array. Keep it at least 10 times the height of nearby objects away from those objects. Backside irradiance on bifacial arrays is measured or calculated in a separate step. Measuring it requires backside plane-of-array sensors.

<!-- review notes
- sentence 1: support check: partial - GroundReflectivity is described as the amount of sunlight reflected from the ground and some reflected radiation hits the array, but albedo is not explicitly defined as a share.
-->
