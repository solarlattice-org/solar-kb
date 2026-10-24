---
id: proto:sunspec-model-302
type: Protocol
name: SunSpec model 302 Irradiance Model
aliases:
- SunSpec 302
- model 302
- irradiance
- Irradiance Model
- SunSpec Irradiance Model
- Solar Irradiance
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 302 is the irradiance model defined in the SunSpec standard and is identified by the well-known
    ID value 302.
  cite:
  - src: src:rainwise-pvmet-500-user-manual
    loc: sec=h24
    h: d95d2b34d3a9
  - src: src:rainwise-pvmet-500-user-manual
    loc: tbl=15.r23
    h: 0dba2c13495c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages say 302 is the SunSpec Irradiance Model with well-known
    ID 302, but don''t explicitly state it belongs to the ''SunSpec information models'' proto concept
    (implied only).'
---
SunSpec model 302 is the irradiance information model in the SunSpec standard. It defines a register block that reports solar irradiance readings over Modbus. The block opens with a read-only ID register that holds 302, followed by a length register that holds 5. Five read-only uint16 data points follow, all in W/m2: global horizontal irradiance (GHI), plane-of-array irradiance (POAI), diffuse irradiance (DFI), direct normal irradiance (DNI) and other irradiance (OTI). The RainWise PVmet-500 weather station is SunSpec compliant and supports models 302, 303 and 307. On the PVmet-500, model 302 carries only global horizontal, plane-of-array and other irradiance, so the remaining points should be ignored. The PVmet-500 manual pairs this model with its default Modbus RS-485 communication settings.

<!-- review notes
- sentence 1: support check: partial - Passages show 302 is the SunSpec irradiance model with a register block of irradiance values, but Modbus transport is only implied via the PVmet-500's Modbus settings.
- sentence 5: support check: partial - Text says PVmet-500 provides GHI, POA and other irradiance and other data should be ignored, but the manufacturer attribution 'RainWise' etc. aside, 'only' is consistent; the minor gap is that the statement matches closely though 'remaining points' is paraphrase.
- sentence 6: support check: partial - The manual places a Modbus RS-485 default settings table amid the 302 text, but doesn't explicitly pair it with the model; it's likely a layout artifact.
- sentence 1: review: partial - The passages show 302 as the SunSpec solar irradiance model with a register table of irradiance points, but Modbus transport is only hinted at by a nearby RS-485 settings table title.
-->
