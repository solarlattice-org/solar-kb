---
id: meas:battery-module-red-led-flashing
type: Measurement
name: Battery module red LED flashing
aliases:
- Red, rapid blinking
- Red LED is flashing quickly
---
A flashing red LED on a battery module means the battery has gone into a fault state. The blink pattern differs by manufacturer, so read it against that battery's LED table. On SMA Home Storage, a fast red flash of about 0.25 s on and 0.25 s off comes with the battery cell undervoltage fault event. For that undervoltage fault, SMA says to close the battery DC switch, restart the battery and inverter, and check that emergency charging starts by itself. If the error stays, contact service. On Enphase IQ Batteries, red flashes in a sequence of two mean an error state that may need an on-site inspection. On Generac PWRcell batteries, rapid red blinking at a 0.5 s interval means an error, while a slow red strobe at an 8 s interval only means the battery is sleeping. Do not confuse a flashing red LED with a steady red battery LED on SMA systems. A steady red light only means the state of charge is below 20 percent.

<!-- review notes
- sentence 1: support check: partial - Passages show flashing red LEDs indicate error states for Enphase, SMA, and Generac with differing patterns, but they don't state the general rule or that you should read it against the battery's LED table.
- sentence 3: support check: partial - The steps match, but the article says 'emerging charging' rather than 'emergency charging', and it also says to contact the installer.
- sentence 5: support check: partial - Rapid red blinking at 0.5 s is an error and a red strobe at 8 s is sleeping, but the passages don't name Generac PWRcell and 'only' is an added qualifier.
- sentence 6: support check: partial - A steady red battery LED means state of charge below 20%, but the passages don't mention flashing red or say 'only'.
- sentence 1: review: partial - The Enphase, SMA and Generac passages each tie a flashing red LED to an error or fault state with different patterns, but the general rule for all battery modules and the advice to read the pattern against that battery's LED…
-->
