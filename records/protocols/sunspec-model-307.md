---
id: proto:sunspec-model-307
type: Protocol
name: SunSpec model 307 Base Met
aliases:
- SunSpec 307
- model 307
- base_met
- Base Meteorological Model
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 307 is the base meteorological model within the SunSpec standard; its header ID value is
    307 and it supersedes model 301.
  cite:
  - src: src:rainwise-pvmet-500-user-manual
    loc: sec=h24
    h: d95d2b34d3a9
  - src: src:rainwise-pvmet-500-user-manual
    loc: tbl=8
    h: 021d0a590ab4
  review: drafted
---
SunSpec model 307, Base Met, is the base meteorological information model in the SunSpec standard. It sets out how weather data is laid out in registers. The model starts with a header: an ID register that reads 307 and a length register that reads 11. It replaces the older model 301. The fixed block holds read-only int16 points: ambient temperature, relative humidity, barometric pressure, wind speed, wind direction, rainfall, snow depth, precipitation type, electric field, surface wetness and soil wetness. The RainWise PVMet-500 weather station is SunSpec compliant and supports models 302, 303 and 307, read over Modbus RS-485. In model 307 the PVMet-500 only fills in ambient temperature, relative humidity, barometric pressure, wind speed, wind direction and rainfall. Ignore the other points.

<!-- review notes
- sentence 4: support check: partial - SunSpec compliance and models 302, 303, 307 are stated, and a Modbus RS-485 settings table is referenced, but the passages don't clearly say the models are read over RS-485 and don't mention RainWise by name.
-->
