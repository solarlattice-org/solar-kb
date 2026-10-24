---
id: concept:plane-of-array-irradiance
type: Concept
name: Plane-of-array irradiance
aliases:
- POA irradiance
- in-plane irradiance
- effective irradiance
- POA
- POAI
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:direct-normal-irradiance
  note: Direct beam is one of the three POA components; the beam term on the plane equals direct normal
    irradiance times the cosine of the angle of incidence.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h2
    h: 097224a34f0a
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h30
    h: 67b7cdd52848
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:diffuse-irradiance
  note: Diffuse sky light is one of the three POA components; how much of it the array sees depends on
    tilt.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h2
    h: 097224a34f0a
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h4
    h: aa0dab698880
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h8
    h: a128b48f86ea
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:albedo
  note: Ground-reflected light is the third POA component. It is usually small except with bifacial modules.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h2
    h: 097224a34f0a
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=h1
    h: 51a013571760
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h9
    h: 51a013571760
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: concept:irradiance-transposition
  note: Transposition estimates POA from a sensor mounted at a different orientation.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h2
    h: 097224a34f0a
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h3
    h: ab5e834dc829
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:global-horizontal-irradiance
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:clear-sky-model
  note: Modeled clear-sky diffuse irradiance is subtracted and added back during POA transposition.
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
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:effective-irradiance
  note: Effective irradiance is the in-plane irradiance the cells actually respond to, after spectral,
    angle-of-incidence and soiling effects.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h29
    h: 44614856eec2
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h15
    h: 2361d5f2450e
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:bifaciality
  note: The ground-reflected contribution becomes significant with bifacial modules.
  cite:
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=h1
    h: 51a013571760
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h9
    h: 51a013571760
  review: drafted
- claim_id: c9
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack can calculate POA from a pyranometer at any orientation.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-irradiance-transposition
    loc: sec=front
    h: '429855123554'
  - src: src:alsoenergy-kb-irradiance-transposition
    loc: sec=front
    h: 0dbda907089f
  review: drafted
- claim_id: c10
  rel: related_to
  target: prod:rainwise-pvmet
  note: The PVMet 500 reports measured plane-of-array irradiance in W/m² through Modbus registers.
  cite:
  - src: src:rainwise-pvmet-500-user-manual
    loc: tbl=15.r26
    h: 8d1a11b14636
  - src: src:rainwise-pvmet-500-user-manual
    loc: tbl=6.r4
    h: 24391a44406e
  - src: src:rainwise-pvmet-500-user-manual
    loc: tbl=10.r2
    h: '782815551746'
  review: drafted
  review_note: 'support check: partial - The passages show POA irradiance registers in W/m², but none
    names the PVMet 500 or RainWise.'
---
Plane-of-array irradiance is the sunlight falling on the surface of the PV modules at their actual tilt and orientation. It is reported in W/m2. It is made up of three components: direct beam, diffuse sky light and ground-reflected light (albedo). If a pyranometer is mounted at the same angle as the modules, it measures POA directly. Otherwise, irradiance transposition converts the sensor reading to the module plane, which adds error that grows with the difference in angle. Calculating POA from a sensor oriented more than 30 degrees away from the modules is not recommended. Measured POA can still differ from what the modules receive. The sensor and the modules can respond differently to the angle of incidence and to the light spectrum. How much diffuse sky light the array sees depends on tilt. A horizontal surface sees the whole sky, while a vertical surface sees only half of it. The ground-reflected part is normally small, except where bifacial modules are used. A related term is effective irradiance: the in-plane irradiance the cells actually respond to, after spectral, angle-of-incidence and soiling losses. It is the basis for translating field I-V curve tests.
