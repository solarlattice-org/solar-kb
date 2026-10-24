---
id: concept:global-horizontal-irradiance
type: Concept
name: Global horizontal irradiance
aliases:
- GHI
- Irradiance Global
- global horizontal insolation
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: prod:alsoenergy-weather-station
  note: The weather station standard IO has a raw GHI register, stored as an average and scaled by a GHI
    scale factor.
  cite:
  - src: src:eq-equip-das-alsoenergy-standard-io-s-aliasing-weather-station-standard-io
    loc: tbl=1.r21
    h: d5e1b4a79b5a
  review: drafted
- claim_id: c2
  rel: related_to
  target: prod:solaredge-commercial-gateway
  note: The gateway accepts an 'Irradiance Global' sensor type that reports global horizontal irradiance
    in W/m2.
  cite:
  - src: src:eq-equip-inverters-solaredge-monitoring-communications-se-ccg-install-guide-v1-2
    loc: tbl=7.r5
    h: ed68dcc871e8
  review: drafted
---
Global horizontal irradiance, usually shortened to GHI, is the solar irradiance received on a horizontal surface. It is reported in watts per square meter, and monitoring gateways list it as the 'Irradiance Global' sensor type. Weather stations and data loggers expose GHI as a measured register value, and some systems archive the raw reading as an interval average with a scale factor applied. Installation guidance for GHI sensors covers how far they must sit from nearby obstructions, because shading of the sensor distorts the reading. Some O&M literature uses the same abbreviation for global horizontal insolation, which is the energy accumulated over time.

<!-- review notes
- sentence 1: support check: partial - Passages give the GHI abbreviation expansion but not the definition of irradiance received on a horizontal surface.
- sentence 4: support check: partial - The figure title shows guidance on distance from obstructions, but the shading-distorts-reading rationale is not stated.
- sentence 5: support check: partial - GHI is listed as global horizontal insolation, but the 'energy accumulated over time' definition is not stated.
- sentence 1: review: partial - The passages expand GHI to Global Horizontal Irradiance but never define it as the irradiance received on a horizontal surface.
- sentence 4: review: partial - The figure titles show guidance on how far GHI sensors sit from nearby obstructions, but the claim that shading distorts the reading is not stated.
-->
