---
id: symptom:backup-mode-unavailable
type: Symptom
name: Backup mode unavailable
aliases:
- Backup operation not possible
- SPS mode
- Secure Power Supply
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Sunny Boy Storage SBSx.x-10/-US-10 units, event 29252 means Secure Power Supply mode is unavailable
    because battery state of charge is too low to supply the loads.
  cite:
  - src: src:sma-kb-event-29252-with-sbsx-x-10-us-10
    loc: sec=h1
    h: 72313f895641
  review: drafted
---
On the Smart Energy inverter, the usual cause is that the inverter still sees an active utility grid connection, so SPS mode does not start. Check first whether the grid is really down, or whether the AC breaker has actually cut the inverter's AC supply. Next, check the backup parameters. Backup can be set in Energy management or in the SMA 360° commissioning wizard. That includes the backup type, which must be set to automatic backup operation if the transfer switch should change over by itself when the grid fails. On Sunny Boy Storage US-10 units, the same event means the battery has too little charge to run the loads in Secure Power Supply mode. Check the battery state of charge there. On those storage units the event can also show up where SPS is not activated or not used, and then it does not change how the system behaves. Firmware 3.00.23 or later stops the event in that case. Keep this separate from the event saying input power is too low for backup operation. That one points to not enough input power, not a grid connection that is still live.

<!-- review notes
- sentence 1: support check: partial - u1 says SPS mode is not started because the utility grid connection is still active, but it does not say this is the 'usual' cause or name the 'Smart Energy' inverter.
- sentence 3: support check: partial - u1 and u11 support checking the backup parameters and setting them in Energy management or the 360° wizard, and u2 supports the automatic backup type; the claim that this comes 'next' as a check for this event is an inference.
- sentence 6: support check: partial - u24 only lists the message 'Input power too low for backup operation' and gives no cause or explanation, so it does not show that this event is about insufficient input power or that it differs from the live-grid case.
-->
