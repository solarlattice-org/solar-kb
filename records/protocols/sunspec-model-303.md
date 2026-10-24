---
id: proto:sunspec-model-303
type: Protocol
name: SunSpec model 303 Back of Module Temperature Model
aliases:
- SunSpec 303
- model 303
- bom_temp
- BOM Temperature Model
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 303 is the SunSpec model for back-of-module (BOM) temperature sensors.
  cite:
  - src: src:rainwise-pvmet-500-user-manual
    loc: sec=h24
    h: d95d2b34d3a9
  - src: src:rainwise-pvmet-500-user-manual
    loc: tbl=15.r30
    h: 55087283ff0f
  review: drafted
---
SunSpec model 303 is the SunSpec information model for back-of-module (BOM) temperature sensors. It defines how the readings are laid out in registers and does not specify the wire or bus they travel over. The model starts with a read-only header: an ID register holding the value 303 and a length register. A repeating block follows, so a device can report a variable number of BOM temperature readings. Each repeated point is TmpBOM, a read-only int16 value in degrees C with a scale factor of -1. The RainWise PVMet 500 weather station is SunSpec compliant and supports model 303 alongside irradiance model 302 and meteorological model 307. When installing a module temperature probe, stick it to the centre of the module's back, away from the edge of the array. A measured back-surface module temperature can be fed into a performance model, which avoids the uncertainty of estimating it from weather data. Cell temperature can then be worked out from the back-surface temperature.

<!-- review notes
- sentence 1: support check: partial - The BOM purpose and register layout are stated, but nothing in the passages says the model does not specify the wire or bus (the Modbus RS-485 table is only mentioned, not contrasted).
-->
