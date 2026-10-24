---
id: concept:direct-normal-irradiance
type: Concept
name: Direct normal irradiance
aliases:
- DNI
- beam irradiance
- Direct Normal Irradiation
- Direct irradiance
- direct beam irradiance
- Edni
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:global-horizontal-irradiance
  note: DNI, GHI and diffuse horizontal irradiation together usually define a site's solar resource.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=3.1
    h: f07096ada173
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:diffuse-irradiance
  note: The beam and diffuse components are measured separately in the detailed laboratory approach.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=3.1
    h: f07096ada173
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h30
    h: 67b7cdd52848
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: Plane-of-array irradiance is the sum of the direct beam, diffuse sky and albedo components.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h3
    h: ab5e834dc829
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: drafted
  review_note: 'support check: partial - POA is stated as the sum of direct, diffuse and albedo components,
    but the passages do not explicitly link DNI itself to POA (direct beam is not named as DNI).'
- claim_id: c4
  rel: related_to
  target: concept:irradiance-transposition
  note: During transposition, trigonometry is applied to the direct beam part only, after the estimated
    diffuse part has been removed.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  review: drafted
  review_note: 'support check: partial - The transposition process is described as subtracting diffuse
    and applying trigonometry to the direct beam, but it is applied to direct horizontal irradiance, not
    explicitly DNI.'
- claim_id: c5
  rel: related_to
  target: concept:clear-sky-model
  note: Clear-sky direct and diffuse irradiance are calculated from the time of day, latitude and longitude.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  review: drafted
  review_note: 'support check: partial - Clear-sky direct and diffuse horizontal irradiance are computed
    from time, latitude, longitude, but the link to DNI specifically is not stated.'
- claim_id: c6
  rel: related_to
  target: concept:albedo
  note: Albedo is the third component of surface irradiance, alongside the direct and diffuse components.
  cite:
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h3
    h: ab5e834dc829
  review: drafted
  review_note: 'support check: partial - Albedo is stated as the third component alongside direct and
    diffuse, but no relation to DNI is stated.'
- claim_id: c7
  rel: related_to
  target: tool:pyrheliometer
  note: DNI is measured with a thermopile pyrheliometer, also called a normal incidence pyrheliometer.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h30
    h: 67b7cdd52848
  - src: src:alsoenergy-kb-powertrack-driver-data-name-naming-convention
    loc: tbl=4.r27
    h: aab301c47224
  review: drafted
  review_note: 'support check: partial - DNI is from a pyrheliometer and a ''normal incidence pyrheliometer''
    entry exists, but ''thermopile'' and ''also called'' are only loosely supported.'
- claim_id: c8
  rel: related_to
  target: concept:air-mass
  note: In the Sandia model, an air mass spectral function is applied together with the beam irradiance.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h30
    h: 67b7cdd52848
  review: drafted
  review_note: 'support check: partial - The Sandia equation applies an air mass function f1(AMa) with
    Eb, but it multiplies the whole bracket rather than only the beam term, and the relation to DNI is
    only indirect.'
---
Direct normal irradiance is the solar power received per unit area on a surface that always faces the sun directly. When it is summed over a period as energy, it is called direct normal irradiation. Direct normal irradiation, global horizontal irradiation and diffuse horizontal irradiation are the values normally used to describe the solar resource at a site. DNI matters most for systems that track the sun and for concentrating technologies, because concentrating technologies can only use the direct beam. The irradiance on a PV array is the sum of three components: direct beam, diffuse sky and albedo. DNI is measured with a pyrheliometer. The beam irradiance on the module plane is DNI multiplied by the cosine of the angle of incidence. Weather stations and data loggers often report DNI as a separate data point in watts per square meter. During irradiance transposition, software subtracts the estimated diffuse part and re-angles the remaining direct beam to the module orientation. It then adds the diffuse part back. When the sun is very low, it assumes there is no direct beam.
