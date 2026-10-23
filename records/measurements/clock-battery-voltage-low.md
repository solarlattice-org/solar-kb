---
id: meas:clock-battery-voltage-low
type: Measurement
name: Low clock battery voltage
aliases:
- Batt. Low
- Battery Low
- LOWBAT
- BATT
---
Some meters report the real-time clock battery voltage as a diagnostic value in volts. The value refreshes about once per second. A built-in self-test measures the clock battery voltage. When the voltage drops below the 2.3 V limit, the self-test raises a warning and pulses the alarm output, and the meter keeps running. A status bit called LOWBAT flags a low real-time clock battery warning. On some inverters, a backup battery voltage that is too low shows as warning W012 Batt. Low, with a flashing yellow LED. To confirm it, check that the date and time are set correctly. Then switch the inverter fully off on both the AC and DC sides, wait a few minutes and restart it. If the date and time have reset to 01/01/2000, the battery is no longer keeping the clock. If the clock does not hold, replace the battery with the inverter isolated on both the AC and DC sides, and keep the battery polarity correct.

<!-- review notes
- sentence 5: support check: partial - The procedure is stated, but the conclusion that a reset to 01/01/2000 means the battery no longer keeps the clock is only implied, since the passage says to replace the battery in that case.
-->
