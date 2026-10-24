---
id: func:ramp-rate-control
type: Function
name: Ramp rate control
aliases:
- power gradient
- normal ramp rate
- WRmp
- Ramp Rate Limit
- Ramp-Rate
category: Control
function_kind: control
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 0.1
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Normal ramp rate, expressed as percent of rated current per second; used for ramp-up after
    irradiance loss or when curtailment is removed or reduced
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=h87
    h: ca99210ae1af
  review: drafted
---
Ramp rate control limits how fast an inverter or storage system changes its power output. On the CPS SCA25KTL-DO/US-208, ramp rate is listed as a smart-grid feature and is enabled in the IEEE 1547-2018, Rule 21 and ISO-NE settings. On SGI XTM firmware D002, the MPPT algorithm can hold the ramp-up below this setting. On firmware D003, the inverter follows the ramp rate until it reaches maximum attainable or maximum output power. In Tesla's control manuals, separate real-power and reactive-power ramp rates, in W/s or var/s, apply only to the direct real and reactive power commands and not to any other control element. In the Tesla manuals, a ramp rate of zero does not switch ramping off. To get an immediate, unramped response, set a large ramp rate value. In the Tesla manuals, if the Enable Manager cancels a direct command, for example after a command timeout or loss of meter communications, the command ramps down at the configured ramp rate.
