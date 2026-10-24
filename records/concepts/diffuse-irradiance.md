---
id: concept:diffuse-irradiance
type: Concept
name: Diffuse horizontal irradiance
aliases:
- DHI
- diffuse irradiance
- Diffuse Horizontal Irradiation
- DFI
- diffuse sky
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: part_of
  target: concept:global-horizontal-irradiance
  note: GHI includes both the direct beam and the scattered diffuse component received on a horizontal
    surface.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=3.1
    h: f07096ada173
  review: drafted
- claim_id: c2
  rel: part_of
  target: concept:plane-of-array-irradiance
  note: Irradiance on the modules is broken into direct beam, diffuse sky and ground-reflected albedo
    components.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:direct-normal-irradiance
  note: DNI, GHI and DHI together are the usual way to describe the solar resource at a site.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=3.1
    h: f07096ada173
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:irradiance-transposition
  note: Transposition removes the estimated diffuse part, applies trigonometry to the direct beam, then
    adds the diffuse part back.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:clear-sky-model
  note: PowerTrack estimates diffuse horizontal irradiance from a clear-sky model based on site location
    and sun position.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h10
    h: 3719fb7dc2cc
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=h2
    h: 3719fb7dc2cc
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:albedo
  note: PowerTrack combines diffuse light and albedo weights using the diffuse factor.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h11
    h: 0abc2ac11bd0
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:expected-energy-model
  note: Finding POA, direct and diffuse irradiance is the first step in the PowerTrack expected-production
    calculation.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  review: drafted
- claim_id: c8
  rel: related_to
  target: prod:alsoenergy-weather-station
  note: The Standard IO map has a Diffuse Horizontal Irradiance point (DHI), stored as an average in W/m².
  cite:
  - src: src:eq-equip-das-alsoenergy-standard-io-s-aliasing-weather-station-standard-io
    loc: tbl=1.r16
    h: d65c6e64f5a9
  review: drafted
  review_note: 'support check: partial - The register row shows DHI stored as an average in W/m², but
    nothing ties it to a specific AlsoEnergy weather station product or the Standard IO map by name.'
---
Diffuse horizontal irradiance (DHI) is the sunlight that reaches a horizontal surface from every part of the sky after the atmosphere or the surroundings have scattered it. Together with the direct beam, it makes up global horizontal irradiance, and PV plants can use both the diffuse and the beam components. The irradiance landing on a module can be split into three parts: direct beam, diffuse sky and ground-reflected albedo. A pyranometer measures the total from the whole hemisphere unless special equipment is used to measure each part separately. When irradiance is transposed to the module plane, the estimated diffuse part is subtracted first. Only the remaining direct beam is corrected for angles, and then the diffuse part is added back. PowerTrack estimates diffuse light from a model based on site location and sun position, because diffuse light changes fairly little with cloud cover. If the measured irradiance is lower than the modeled diffuse value, the measured value is used instead. How much diffuse light a module can collect depends on its tilt. A horizontal module sees the whole sky, while a vertical module sees only half of it, so it gets about 50 percent.

<!-- review notes
- sentence 5: support check: partial - The model and the fallback to measured irradiance are stated, but the passage says the value is fairly consistent regardless of clouds, and it gives simplicity as the reason for the model approach.
-->
