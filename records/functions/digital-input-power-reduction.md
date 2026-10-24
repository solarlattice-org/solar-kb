---
id: func:digital-input-power-reduction
type: Function
name: Power reduction via digital inputs
aliases:
- ripple control receiver
- RCR
- grid management services via digital inputs
- feed-in control 0/30/60/100%
- Feed-in power control
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: subclass_of
  target: func:limit-active-power
  note: Digital inputs carry external active power limitation signals.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.4
    h: 5c24edb504c2
  - src: src:sma-kb-active-power-limitation-settings-using-ripple-control-receiver-and-i-o-module-stp50
    loc: sec=h1
    h: 6245a00e59cc
  review: drafted
- claim_id: c2
  rel: requires
  target: func:system-manager
  scope:
    products:
    - prod:sma-stp-x-us-50
  note: The System Manager applies the open-loop or closed-loop power limit selected via digital inputs.
  cite:
  - src: src:kb-sma-stpxxus50-control-and-regulation-of-grid-management-services-via-digital-inputs
    loc: sec=h1
    h: 84fddafe2d78
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=8.9.3
    h: 29f73b59f211
  review: drafted
  review_note: 'support check: partial - u3/u12 say the System Manager applies open/closed-loop limits
    selected via digital inputs, but nothing ties this to the STP X US 50 product scope.'
- claim_id: c3
  attr: default_value
  value:
    nominal: 0
    unit: unit:PERCENT
  conditions: Solis DRM port, power level assigned to switch S1
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r1
    h: 2b341e25a908
  review: drafted
  review_note: 'support check: partial - u21 gives S1 default 0%, but the passage doesn''t mention the
    Solis DRM port context explicitly.'
- claim_id: c4
  attr: setting_range
  value:
    min: 0
    max: 110
    unit: unit:PERCENT
  conditions: Solis DRM port, adjustable power level for switch S1
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: tbl=1.r1
    h: 2b341e25a908
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - u21 gives an adjustable range of 0…110% for S1, but doesn''t
    name the Solis DRM port.'
- claim_id: c5
  attr: response_time
  value:
    max: 1
    unit: unit:SEC
  conditions: 'Solis DRM port 0-100% control: inverter shuts down and disconnects after switch S0 (pins
    5 and 6) opens'
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: sec=h1
    h: 6ad7f1571bc0
  review: drafted
- claim_id: c6
  attr: reconnect_delay
  value:
    max: 30
    unit: unit:SEC
  conditions: 'Solis DRM port 0-100% control: reconnection after switch S0 is closed again'
  cite:
  - src: src:kb-solis-44002583082-how-do-i-connect-a-ripple-control-receiver-to-the-drm-port
    loc: sec=h1
    h: 6ad7f1571bc0
  review: drafted
---
This function lets the grid operator cut feed-in power through switching contacts, usually from a ripple control receiver, that are wired to the digital inputs of an inverter or system controller. SMA systems connect the receiver through a compatible I/O system and can step feed-in power to 100%, 60%, 30% or 0%. On the SMA Data Manager M, you set this up under Grid management services by choosing digital inputs as the source for the external setpoint and assigning bit patterns to power levels. Set a fallback value or a 100% pattern, because all inputs open is an undefined state. SMA sources disagree on pulse signals. One technical note says the Data Manager M can handle pulse signals with its internal inputs, but a support article says the Data Manager needs static signals and that pulse signals must be preprocessed, for example by a Mini-PLC. On the Core1 with the SMA I/O module, the factory input patterns are D1 for 0%, D2 for 30%, D3 for 60% and all inputs open for 100%. You must also set the operating mode to active power limitation on each inverter. Solis inverters take the receiver contacts on the RJ45 DRM port. Pins 5 and 6 give on/off control, and pins 1 to 4 give 0-30-60-100% limiting, which only works with pins 5 and 6 bridged. DRM is disabled by default on Solis inverters. Enable it on each inverter, either from the display or in SolisCloud.

<!-- review notes
- sentence 3: support check: partial - u17 supports the Grid management services path, digital inputs source and the undefined all-open state with fallback or 100%, but doesn't mention assigning bit patterns to power levels explicitly.
-->
