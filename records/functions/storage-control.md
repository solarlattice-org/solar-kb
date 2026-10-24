---
id: func:storage-control
type: Function
name: Storage charge/discharge control
aliases:
- battery control
- storage basic controls
- Time of Use
- Charge Control
- Smart Charge & Discharge
- Storage System Control
- ESS Operating Mode
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: requires
  target: role:qualified-person
  scope:
    standard: std:nfpa-70-2017
  quote: All adjustable means for control of the charging process shall be accessible only to qualified
    persons.
  quote_source: NFPA 70 (NEC) 2017 §706.23(A)
  cite:
  - src: src:std-standards-nec-2017-nec2017-706
    loc: sec=h18
    h: a87ae1939663
  review: drafted
  review_note: 'support check: partial - NEC 706.23 says adjustable charge-control means must be accessible
    only to qualified persons, but it says nothing about discharge control.'
- claim_id: c2
  rel: requires
  target: proto:sunspec-modbus
  scope:
    products:
    - prod:sma-sunny-tripower-storage-60
  note: Option for manual charge/discharge via the active power setpoint register 40349 (unit ID 125);
    the SMA Storage System Control register 1237 (unit ID 25) is the alternative.
  cite:
  - src: src:sma-kb-sts60-10-batterie-ladung-entladung-steuern-via-modbus-register
    loc: sec=h1
    h: 0c32d6f1c381
  review: drafted
- claim_id: c3
  rel: requires
  target: prod:sma-inverter-manager
  scope:
    products:
    - prod:sma-sunny-tripower-storage-60
  note: Modbus charge/discharge commands are addressed to the inverter manager by unit ID.
  cite:
  - src: src:sma-kb-sts60-10-batterie-ladung-entladung-steuern-via-modbus-register
    loc: sec=h1
    h: 0c32d6f1c381
  review: drafted
- claim_id: c4
  rel: requires
  target: func:peak-shaving
  scope:
    products:
    - prod:sma-sunny-tripower-storage-60
  note: Peak Load Shaving must be enabled for Modbus charge/discharge control to work.
  cite:
  - src: src:sma-kb-sts60-10-batterie-ladung-entladung-steuern-via-modbus-register
    loc: sec=h1
    h: 0c32d6f1c381
  review: drafted
- claim_id: c5
  rel: requires
  target: func:time-of-use-optimization
  scope:
    products:
    - prod:sma-sunny-tripower-storage-60
  note: Time of Use must be enabled for Modbus charge/discharge control to work.
  cite:
  - src: src:sma-kb-sts60-10-batterie-ladung-entladung-steuern-via-modbus-register
    loc: sec=h1
    h: 0c32d6f1c381
  review: drafted
- claim_id: c6
  attr: setting_range
  value:
    min: 0
    max: 20000
    unit: unit:W-HR
  conditions: SMA battery management parameter Discharge energy (CmpBMS.BatDschWh), Modbus register 41365
  cite:
  - src: src:man-sma-modbus-pre2018-stp50-41-stpxx-us-41-v17-parameterlist-en
    loc: tbl=1.r13
    h: cd77c5521930
  - src: src:eq-equip-inverters-sma-stp-core1-50-parameterlist-en
    loc: tbl=1.r13
    h: cd77c5521930
  review: drafted
- claim_id: c7
  attr: default_value
  value:
    nominal: 0
    unit: unit:W-HR
  conditions: SMA battery management parameter Discharge energy (CmpBMS.BatDschWh), Modbus register 41365
  cite:
  - src: src:man-sma-modbus-pre2018-stp50-41-stpxx-us-41-v17-parameterlist-en
    loc: tbl=1.r13
    h: cd77c5521930
  - src: src:eq-equip-inverters-sma-stp-core1-50-parameterlist-en
    loc: tbl=1.r13
    h: cd77c5521930
  review: drafted
---
Storage control decides when a battery charges or discharges and at what rate. On Solis hybrids, Time of Use sets charge and discharge periods, each with a current setpoint and a settable cut-off voltage, and it takes priority over the other storage modes. On the SMA Sunny Tripower Storage 60, you can command charging or discharging over Modbus by writing the active power setpoint to SMA SSC register 1237 or SunSpec register 40349. A negative value charges and a positive value discharges, and Peak Load Shaving and Time of Use must both be enabled. Tesla systems can charge or discharge until the remaining battery energy meets a Maintain Energy Target sent from an external interface. With SMA battery inverters, the Sunny Home Manager uses the load profile and the yield forecast to control when lead-acid batteries discharge, so that room is left for forecast PV energy. In off-grid systems, charge controllers limit charging voltage or current through regulation set points. They also prevent over-discharge with low-voltage disconnect and reconnect set points. At commercial sites, the rate structure and the load profile drive the charge and discharge strategy, for example for demand charge management. These strategies often use forecasting.

<!-- review notes
- sentence 1: support check: partial - The passage supports the Time of Use description, but it never mentions Solis hybrids by name.
- sentence 2: support check: partial - The register details, signs and enablement are all stated, but the article never names the Sunny Tripower Storage 60 model beyond its STS60-10 title.
-->
