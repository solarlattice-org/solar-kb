---
id: symptom:control-fallback-operation
type: Symptom
name: Fallback operation after loss of control or meter signal
aliases:
- Communication with the System Manager failed
- timeout in communication for active power limitation
- fallback mode
- LimByEPM
- fallback level
- reactive power setpoint timeout
- failsafe
- restricted function
- Loss of Meter Communication
- Fallback activated
claims:
- claim_id: c1
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: In fallback the inverter holds AC output at a configured fallback setpoint, or at the last received
    values, until the trigger has stayed clear for the re-entry time.
  cite:
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h35
    h: a2fa68991134
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h31
    h: 07524ffc6b81
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h54
    h: e845e36f0d5a
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=45.r6
    h: 04c22a7b8304
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h246
    h: 63768ed4f2a1
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r46
    h: b51cc6d2945d
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h47
    h: 3a8e65edf69d
  review: drafted
  review_note: 'support check: partial - Fallback setpoint hold and re-entry time are stated, but the
    passages say nothing about irradiance staying normal/rising or power staying flat regardless of irradiance;
    the ''last received values'' option is also covered.'
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: With failsafe ON, losing the meter or CT shuts generation down. Tesla systems curtail output to
    zero when the lost meter is needed by the active control function.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=5.6.8.3
    h: 616919bf0a40
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: sec=h227
    h: ad773aa06169
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: sec=h218
    h: 45f83744a35b
  - src: src:tesla-megapack-2-xl-operation-and-maintenance-manual-v1-1
    loc: tbl=19
    h: c32ec831212d
  - src: src:tesla-megapack-2-xl-operation-and-maintenance-manual-v1-1
    loc: tbl=21
    h: 9f93c2e2d466
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:fallback-event-message
  note: Examples are SMA event 8708 (timeout in communication for active power limitation) and Inverter
    Manager status IDs 2055/2056 (fallback activated/completed).
  cite:
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=29.r9
    h: 4632eac88839
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=29.r10
    h: e9316c0ce376
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=29
    h: 979cbbc5a32f
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r46
    h: b51cc6d2945d
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h47
    h: 3a8e65edf69d
  - src: src:sma-stpxx-us-50-be-en-14
    loc: tbl=16.r1
    h: d6c30d03df80
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Solis displays show a Failsafe alarm when the CT or meter disconnects with failsafe ON, or a LimByEPM
    message when external power meter limiting is active.
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: sec=h227
    h: ad773aa06169
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: sec=h218
    h: 45f83744a35b
  - src: src:kb-solis-44002485982-limbyemp
    loc: sec=h1
    h: 8296049b45a3
  - src: src:kb-solis-44002649144-limb-by-epm
    loc: sec=h1
    h: 009d4ba35915
  review: drafted
  review_note: 'support check: partial - The Failsafe alarm on the LCD is stated and a LimByEPM message
    is mentioned, but the passages do not say it appears when external power meter limiting is active
    (only that it can occur when the setting is on).'
- claim_id: c5
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: A flashing red LED pattern warns that communication with the System Manager failed and that the
    inverter is running with restricted function.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: tbl=16.r1
    h: d6c30d03df80
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:frozen-meter-readings
  note: After loss of meter communication, the reported meter values stay frozen at their last value.
  cite:
  - src: src:tesla-megapack-2-xl-operation-and-maintenance-manual-v1-1
    loc: tbl=19
    h: c32ec831212d
  - src: src:tesla-megapack-2-xl-operation-and-maintenance-manual-v1-1
    loc: tbl=21
    h: 9f93c2e2d466
  review: drafted
- claim_id: c7
  rel: observed_as
  target: meas:meter-invalid-alert
  note: A Meter Invalid alert is raised on loss of meter communication, out-of-bounds or unreasonable
    readings, or a PT/CT failure, and control elements are then disabled.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.5
    h: 95c425ad14fe
  review: drafted
---
Fallback operation happens when an inverter or plant controller loses its energy meter, its system manager or its external setpoint. Instead of following live control, it switches to a predefined behaviour. In monitoring data, output either holds flat at a set fallback power or at the last received values, or drops to zero when a failsafe shutdown is configured. Look for SMA event 8708 or a fallback activated status, a flashing red LED warning, or a Failsafe or LimByEPM message on Solis displays. Likely causes are a meter that has failed or lost power, a damaged or unplugged communication cable between the inverter and the system manager, or an external setpoint that is missing or invalid. If output stays limited while the meter communicates normally, check the failsafe and EPM settings. Solis advises turning both the external and internal EPM fail safe options off when they are not needed. Start by checking that the meter is powered, then inspect the network connection and cables to the controller, and confirm the meter settings. Normal operation resumes once communication has been back for the configured re-entry time.

<!-- review notes
- sentence 3: support check: partial - Event 8708, the fallback activated status, the red flashing LED and the Failsafe alarm are in the passages, and LimByEPM is mentioned; but the passages never say 'Solis displays' show these, and 8708 isn't tied to a fallback-activated status.
- sentence 4: support check: partial - Passages support a damaged or unplugged communication cable to the system manager and a missing or invalid setpoint, but a meter that has failed or lost power is only implied by the 'verify meter is powered on' step, not stated as a cause.
- sentence 5: support check: partial - Solis advice to turn the external and internal EPM fail safe settings off is stated, but 'when not needed' and the 'meter communicates normally' condition are not in the passages.
-->
