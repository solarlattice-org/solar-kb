---
id: comp:backup-battery
type: Component
name: Clock backup battery
aliases:
- buffer battery
- back-up battery
- backup battery
- clock battery
- Real-time clock battery
---
The clock backup battery is a small CR2032 coin cell mounted on the inverter's communication and control board. Inverter specification tables list the backup battery chemistry as nickel, lead or lithium. When the inverter detects that the backup battery voltage is too low, it raises warning W012 Batt. Low with a flashing yellow LED. A battery that has failed shows up as the date and time resetting to 01/01/2000 after the inverter has been fully powered down and restarted. This also relates to the Clock Fail alarm and to real-time clock failure. Replace the battery only after both the AC and DC sides are fully isolated, and keep the polarity shown on the board silkscreen. On TRIO units the battery sits under a plastic cover over the DC high-voltage sections. Opening the AC+DC switch alone still leaves DC input voltage on the board, so also disconnect the string connectors. Handle the new cell with insulating gloves so it does not discharge during installation. Some meters watch the clock battery voltage as a self-test item and report a warning when it is low.

<!-- review notes
- sentence 6: support check: partial - Cover, DC voltage remaining with AC+DC switch alone, and disconnecting connectors are stated, but the passages say this for versions S2F/S2X and do not name 'TRIO' units.
- sentence 8: support check: partial - Self-test BATT measures clock battery voltage with Warning condition, but 'report a warning when low' and 'some meters' is only loosely stated; limit +2.3 V is not explicit about low.
-->
