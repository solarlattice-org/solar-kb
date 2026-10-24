---
id: func:demand-response-modes
type: Function
name: Demand response modes (DRM)
aliases:
- DRM
- DRED
- AS/NZS 4777 DRM modes
- Demand Response Management
- Dynamic Response Mechanism
- DRM0/1/5
- Demand Response Mode
category: Control
function_kind: control
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 0
    max: 110
    unit: unit:PERCENT
  conditions: Solis DRM port, power level for switch S1
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r1
    h: 2b341e25a908
  review: drafted
- claim_id: c2
  attr: default_value
  value:
    nominal: 30
    unit: unit:PERCENT
  conditions: Solis DRM port, power level applied when switch S2 is closed
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r2
    h: eccfe9264935
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c3
  attr: setting_range
  value:
    min: 0
    max: 110
    unit: unit:PERCENT
  conditions: Solis DRM port, power level for switch S2
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r2
    h: eccfe9264935
  review: drafted
- claim_id: c4
  attr: default_value
  value:
    nominal: 60
    unit: unit:PERCENT
  conditions: Solis DRM port, power level applied when switch S3 is closed
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r3
    h: 4eb2a83fc75d
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c5
  attr: setting_range
  value:
    min: 0
    max: 110
    unit: unit:PERCENT
  conditions: Solis DRM port, power level for switch S3
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r3
    h: 4eb2a83fc75d
  review: drafted
- claim_id: c6
  attr: default_value
  value:
    nominal: 100
    unit: unit:PERCENT
  conditions: Solis DRM port, power level applied when switch S4 is closed
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r4
    h: 67e97f232d9d
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions)
- claim_id: c7
  attr: setting_range
  value:
    min: 0
    max: 110
    unit: unit:PERCENT
  conditions: Solis DRM port, power level for switch S4
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r4
    h: 67e97f232d9d
  review: drafted
- claim_id: c8
  attr: response_time
  value:
    max: 1
    unit: unit:SEC
  conditions: Solis inverter shutdown and grid disconnection after the S0 contact (pins 5 and 6) is opened
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: sec=h1
    h: 6ad7f1571bc0
  review: drafted
  review_note: 'support check: partial - Passage says shutdown within 1 second after S0 opened; ''up to''
    is implied but fine, though pins 5/6 as S0 is implied by the 0-100% control section; mostly supported.'
- claim_id: c9
  attr: reconnect_delay
  value:
    max: 30
    unit: unit:SEC
  conditions: Solis inverter reconnection to grid after the S0 contact is closed again
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: sec=h1
    h: 6ad7f1571bc0
  review: drafted
---
Demand response modes let the utility or grid operator command an inverter remotely through contact signals, as required in Australia by AS/NZS 4777.2. DRM0 disconnects the inverter from the grid, DRM1 brings grid import to zero and DRM5 brings export to zero on utility command. On FIMER UNO-DM PLUS inverters, DRM0 uses the REM terminal block and is enabled with a jumper; if it is enabled without correct wiring, the inverter cannot connect to the grid. Solis inverters have an RJ45 DRM port: pins 5 and 6 switch the inverter on or off, and pins 1 to 4 limit output in stages, for example from a ripple control receiver. DRM is off by default on Solis inverters. If it is turned on while the contact is open or not wired, the display reads Limit by DRM and output is limited to zero. You can enable DRM from the inverter display, over Bluetooth in the SolisCloud app under Grid Code Settings, or in SolisCloud, and it must be set on each inverter separately. KACO blueplanet inverters sold in Australia need a DRM 0 safety label fixed next to the nameplate.

<!-- review notes
- sentence 3: support check: partial - REM terminal block and jumper and grid-connection failure are stated, but passages do not mention UNO-DM PLUS model name.
- sentence 7: support check: partial - Label next to nameplate in Australia is stated, but the passage does not name KACO blueplanet (only Powador-protect mention).
-->
