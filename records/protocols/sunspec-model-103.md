---
id: proto:sunspec-model-103
type: Protocol
name: SunSpec model 103 Inverter (Three Phase)
aliases:
- SunSpec 103
- model 103
- inverter_three_phase
- three phase AC Monitoring
- Inverter (3 Phase)
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as model 103 among the SunSpec information models an SMA inverter supports; the 100 series
    is marked outdated, with model 701 recommended instead.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SunSpec model 103 is the SunSpec information model for three-phase inverter AC monitoring data. Its device ID register reads 103, which marks a three-phase inverter, while 101 marks single phase and 102 split phase. SolarEdge inverters support the model 101, 102 and 103 register maps for read-only Modbus monitoring data, based on the SunSpec inverter models. In the SolarEdge map the model 103 block is 50 registers long. It carries total and per-phase AC current, a current scale factor, and the AB, BC and CA line voltages. SMA SunSpec Modbus documentation lists model 103 as supported but recommends model 701 instead, because SunSpec marks the 100 series as outdated and the 700 series replaces it.

<!-- review notes
- sentence 2: support check: partial - The passage says SolarEdge supports SunSpec module IDs 101, 102 and 103 and bases its read-only monitoring data on SunSpec inverter models. It does not say these are 'model' register maps in those words, but that is close enough. Only a minor wording gap remains.
-->
