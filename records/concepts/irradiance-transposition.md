---
id: concept:irradiance-transposition
type: Concept
name: Irradiance transposition
aliases:
- GHI to POA transposition
- transposition model
- POA decomposition
- plane-of-array irradiance transposition
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: Transposition estimates POA irradiance from a sensor mounted at a different orientation than the
    array.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h3
    h: ab5e834dc829
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:global-horizontal-irradiance
  note: GHI can be either the input (horizontal pyranometer or satellite data) or the output of the calculation.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.2
    h: 9867312e6c19
  review: drafted
  review_note: 'support check: partial - GHI is stated as calculated from available irradiance data, but
    the claim that GHI can be an input (horizontal pyranometer) is only implied; satellite data is not
    mentioned.'
- claim_id: c3
  rel: related_to
  target: concept:diffuse-irradiance
  note: The estimated diffuse part is subtracted before the direct beam is transposed, then added back.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:alsoenergy-kb-pv-shading-model
    loc: sec=front
    h: 11ff663ce925
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:clear-sky-model
  note: PowerTrack takes the diffuse and albedo components from a clear-sky model.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:alsoenergy-kb-pv-shading-model
    loc: sec=front
    h: 11ff663ce925
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:albedo
  note: The PowerTrack transposition ignores albedo, but the shading model can apply an albedo correction
    factor.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:alsoenergy-kb-pv-shading-model
    loc: sec=front
    h: 11ff663ce925
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:expected-energy-model
  note: Getting the effective POA irradiance is the first step in calculating expected power.
  cite:
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.2
    h: 9867312e6c19
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:shading-loss
  note: Shade corrections reuse the direct, diffuse and albedo components.
  cite:
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  - src: src:alsoenergy-kb-pv-shading-model
    loc: sec=front
    h: 11ff663ce925
  review: drafted
- claim_id: c8
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack calculates POA and GHI from pyranometer data at any orientation.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  review: drafted
---
Irradiance transposition converts irradiance measured at one orientation into an estimate of the irradiance at another orientation, usually the plane of the PV array. The light reaching a surface is treated as the sum of three parts: direct beam, diffuse sky and ground-reflected albedo. A pyranometer measures only their combined total, so the split between them has to be estimated. In the PowerTrack method, the estimated diffuse irradiance comes from a clear-sky model and is subtracted from the measured value. The remaining direct beam is then scaled using the sun position and the orientations of the sensor and the module, and the diffuse part is added back. If the sun is below 2 degrees elevation, or the reading is lower than the calculated diffuse irradiance, the measured value is passed through unchanged. The method always adds some error. The error grows with the angle between the sensor and the target plane and also depends on the time of year and on atmospheric and ground conditions. The best practice is to mount POA and GHI sensors in the correct orientations so no transposition is needed. Using a sensor more than 30 degrees off the module plane is not recommended. The transposed POA irradiance feeds the expected energy model and the shading-loss calculation. When only GHI is available, a performance ratio calculated from it usually comes out higher, sometimes above unity.

<!-- review notes
- sentence 7: support check: partial - GHI-based PR being higher and possibly above unity is stated in u4, and POA feeds the expected model, but the passages do not explicitly say transposed POA feeds the shading-loss calculation, and the GHI-only link is not tied to transposition.
-->
