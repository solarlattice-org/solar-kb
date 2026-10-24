---
id: concept:clear-sky-model
type: Concept
name: Clear-sky irradiance model
aliases:
- clear-sky irradiance
- clear sky model
- Blue-Sky model
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:irradiance-transposition
  note: Clear-sky direct and diffuse horizontal irradiance are calculated from time, latitude and longitude
    and used to separate diffuse from measured irradiance before the direct beam is transposed.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:diffuse-irradiance
  note: The clear-sky model supplies the estimated diffuse (and albedo) component that is subtracted and
    added back during transposition.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:global-horizontal-irradiance
  note: The clear-sky model can be used to validate GHI measurements.
  cite:
  - src: src:alsoenergy-kb-definitions-data-names-kpis-etc
    loc: sec=front
    h: 95bd390c335f
  review: drafted
- claim_id: c4
  rel: related_to
  target: metric:performance-loss-rate
  note: Clear-sky filters and statistical clear-sky fitting are used in performance loss rate analysis.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.4
    h: 456a1729a79f
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.4.7
    h: 36f8565b3b7d
  review: drafted
- claim_id: c5
  rel: related_to
  target: org:nrel
  note: The PowerTrack clear-sky irradiance is based on an algorithm developed by NREL.
  cite:
  - src: src:alsoenergy-kb-definitions-data-names-kpis-etc
    loc: sec=front
    h: 95bd390c335f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack uses a clear-sky model for transposition, shading and as a baseline for sensor comparison.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-definitions-data-names-kpis-etc
    loc: sec=front
    h: 95bd390c335f
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:shading-loss
  note: The PowerTrack shading model derives diffuse and albedo components from the clear-sky model.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  review: drafted
---
A clear-sky model calculates the irradiance a site would receive with no clouds, using latitude, longitude, elevation and date and time, and assuming normal atmospheric conditions. Clear-sky PV power output is the output calculated without clouds or other weather, so it represents the maximum output possible from an installation; the key input is the angle between the sun's rays and the panel normal. Because the model does not depend on measurements and repeats each year for a given location and time, it serves as a baseline for multi-year comparisons, such as spotting irradiance sensor degradation or validating GHI readings. In performance loss rate work, clear-sky filters keep only periods with little cloud by comparing sensor irradiance with modeled clear-sky irradiance, either with a strict multi-criteria method or a simpler clear sky index ratio. Monitoring platforms also use clear-sky direct and diffuse estimates to transpose a pyranometer reading to plane-of-array irradiance and to estimate shading loss. A statistical clear-sky fitting method can build an adaptive clear-sky model from measured power alone and use it to detect clear conditions, fill gaps and estimate degradation. Clear-sky models work less well in cloudy periods, so gap-filling and filtering methods that rely on them perform best when the data actually come from clear-sky periods.

<!-- review notes
- sentence 1: support check: partial - Passages give inputs and normal atmospheric conditions, but 'no clouds' is only implied by the name 'clear-sky', not stated for the model.
- sentence 7: review: partial - The passages say modeled irradiance does not perform well in cloudy periods and that one gap-filling method (DSG1) works best on clear-sky data, but extending this to filtering methods in general is not stated.
-->
