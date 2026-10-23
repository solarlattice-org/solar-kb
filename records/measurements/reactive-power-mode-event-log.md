---
id: meas:reactive-power-mode-event-log
type: Measurement
name: Reactive power mode event log
aliases:
- Reactive Power Regulation Control
---
This signature is a record that the inverter's reactive power mode was set or changed. The mode is found under System and device control, then Inverter, then Reactive power mode. Separate mode parameters exist for active power output, for active power draw and for zero active power, so check which of these entries changed. Available modes include Off, a fixed Q setting and a cos phi setpoint. Note that the cos phi setpoint mode does not apply at zero active power. Other inverters offer PF mode, constant reactive power mode, PFP mode, Q(U) curve mode and Q(P) curve mode, and each has its own parameters. A mode switch can be expected when the setpoint goes missing, for example when communication with the superordinate control unit fails. In that case the grid operator can require a specified fallback reactive power mode. Which reactive power feed modes are used depends on the country or state of installation and on the grid company. Compare a logged change against the required grid settings. To confirm what the inverter actually did after the change, compare the reactive AC power output measurement in volt-amperes reactive.

<!-- review notes
- sentence 1: support check: partial - The menu path System and device control > Inverter > Reactive power mode is stated, but nothing says the signature is a record of the mode being set or changed.
- sentence 2: support check: partial - Separate parameters for active power output, draw and zero active power exist, but the passages don't say to check which entry changed.
- sentence 4: support check: partial - The five modes with different parameters are listed, but the passage doesn't say they belong to other inverters as opposed to this one.
- sentence 6: support check: partial - The passage says feeding modes vary by country/state and grid company, but it doesn't mention comparing a logged change with required grid settings.
- sentence 7: support check: partial - A Reactive AC Power Output (VAr) measurement exists, but nothing says to use it to confirm the inverter's behavior after a change.
-->
