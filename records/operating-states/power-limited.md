---
id: state:power-limited
type: OperatingState
name: Power limited
aliases:
- active power limitation
- curtailed
- export limited
- setpoint limited
- limited operation
- Limited Export
- Power reduction
- Power limiting
- Nameplate Limits
- Active power limited AC voltage
category: Inverters
claims:
- claim_id: c1
  attr: output_limit
  value:
    nominal: 50
    unit: unit:PERCENT
  scope:
    products:
    - prod:abb-pvs-60-tl-us
  conditions: 'Worked example in the manual: a display reading of LIM 50% means output is held to 50%
    of nominal output power. In this case the limit comes from low grid voltage (CODE:04).'
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r5
    h: 4d9606c648cb
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  attr: output_limit
  value:
    nominal: 50
    unit: unit:PERCENT
  scope:
    products:
    - prod:abb-uno-dm-3-3-5-0-plus-us
  conditions: 'Worked example in the manual: a display reading of LIM 50% means output is held to 50%
    of nominal output power. In this case the limit comes from the anti-islanding function (CODE:03).'
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r4
    h: 33ad73be773c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  attr: output_limit
  value:
    min: 0
    max: 100
    unit: unit:PERCENT
  conditions: SMA reports active power limitation as active when the default limitation value is above
    0% and below 100%.
  cite:
  - src: src:sma-doc-240154
    loc: tbl=75.r2
    h: 1af8cf11fe08
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Power limited means the inverter is running normally but is held below the power it could otherwise deliver, because of a setpoint, an export limit or its own nameplate rating. On SMA Inverter Manager systems, the limit can be a fixed active power setpoint (P_ref). It can also be sent dynamically through the I/O Box, Modbus or a direct marketer interface, and a dynamic value overrides the fixed one. With Limited Export and a Modbus energy meter, the limit applies at the grid connection point. Inverter output rises or falls with on-site consumption, so local loads are still supplied. Indications differ by vendor. Solectria inverters keep the green LED on and show messages such as L1 Power reduction or PV1 PW limit to Pn. FIMER inverters show LIMxxx% with a code giving the cause. SMA systems log an event that reports how many minutes active power was limited that day. A limit set by the nameplate rating needs no action. If the limit comes from low grid voltage and does not go away, check the grid voltage and contact the grid operator. If an anti-islanding limit stays active while the inverter is still connected to the grid, contact customer assistance. Hours with heavy curtailment can make the performance ratio look low even when the equipment is healthy. Take this into account before you look for a fault.

<!-- review notes
- sentence 1: support check: partial - The passages cover setpoint, export limit and nameplate limiting, but they don't state that the inverter is running normally; the definition is a synthesis.
- sentence 4: support check: partial - FIMER's LIMxxx% with a cause code is supported, but the passages show the PV1 PW limit to Pn message with a red LED (not green) and do not name the vendor as Solectria or FIMER.
- sentence 8: support check: partial - The passage says low PR in curtailed hours may reflect grid instructions rather than equipment health, but it doesn't give the advice to account for this before looking for a fault.
- sentence 1: review: partial - Setpoint, export-limit and nameplate limiting are supported, but the passages never say the inverter is 'running normally', and the nameplate row only says it is not tracking the MPP.
- sentence 4: review: partial - L1 Power reduction is shown with a green LED that is on, but PV1 PW limit to Pn is shown with a red LED that is off, which contradicts 'keep the green LED on' for that message; the FIMER LIMxxx%…
-->
