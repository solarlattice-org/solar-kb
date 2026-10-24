---
id: func:night-reactive-power
type: Function
name: Reactive power at night
aliases:
- Q at Night
- Q on Demand
- night-time reactive power
- Q on Demand 24/7
- night SVG function
- Reactive power generation at night
- Reactive power injection at night
- Reactive power output at night
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: requires
  target: func:watt-power-factor
  negated: true
  note: Q on Demand 24/7 is stated to be incompatible with the cos phi(P) and cos phi(V) characteristic
    curve reactive power modes.
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=9.17
    h: 8f8c41459bba
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=8.20
    h: 134a7bde8770
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: -100
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:sungrow-sg250hx
    - prod:sungrow-sg-cx-us
  conditions: Reactive power ratio at night parameter for the night SVG function, range listed as -100%
    to 0% / 0% to 100%
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=33
    h: 2b52d6a1abf7
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=33.r2
    h: 8a8b47aefbb4
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=43.r2
    h: 19cf9b0c599c
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=43
    h: 3697eeae32d6
  review: drafted
---
Reactive power at night lets an inverter supply reactive power to support the grid when it is not feeding in active power, for example at night. It can also compensate the reactive power needed inside the PV plant. To do this, the inverter stays connected to the grid overnight. It draws active power from the grid to cover its losses and run its internal assemblies. On the Sunny Central CP XT, this needs the Q at Night option. The option adds hardware so the inverter can operate without DC voltage. Reactive output is limited to protect the MV transformer, and an extra cable set to the transformer may be needed. To activate SMA Q on Demand, configure the zero-active-power reactive range with Inverter.VArModCfg.VArModZerW and set Inverter.VArModCfg.QoDEna to ON. The Q at Night setpoint mode is chosen separately with QoDQ-VArMod. Q on Demand 24/7 on SMA string inverters accepts only Q setpoints. It does not work with the cos phi(P) or cos phi(V) curve modes. If the inverter disconnects at night, the function restarts only after enough PV power has returned.
