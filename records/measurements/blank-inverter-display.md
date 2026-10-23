---
id: meas:blank-inverter-display
type: Measurement
name: Blank inverter display
aliases:
- Blank Screen
- No Information
- Total Failure of the Display
- HMI Corrupted
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power stays at normal levels, because feed-in continues while the display is blank
---
The inverter front display shows nothing at all, and the screen stays dark even though the unit should be running. If the screen is still dark long after sunrise, measure the AC voltage at the inverter connections and confirm it is inside the grid range given in the manual. One manufacturer lists three causes for a blank screen: low or missing PV input voltage, reversed polarity and a damaged main board. Check the PV wiring and polarity, and measure the DC voltage with the DC switch both off and on. If the DC voltage reads zero, the inverter should be replaced. Before calling it a fault, check the display illumination setting. Some inverters let you switch the backlight permanently off, or turn it off automatically when no key has been pressed for a while. Some inverter models are built without a display, and their model code marks this. A blank display can come with an inverter that has stopped working completely. The monitoring data log can help find the cause, and visual inspection or infrared thermography can show burned parts.

<!-- review notes
- sentence 7: support check: partial - Complete failure, data log and visual/IRT inspection of burned parts are supported, but the passages don't link a blank display to complete failure.
- sentence 7: review: partial - The IEA row supports complete inverter failure, the monitoring data log, and visual/IRT inspection for burned parts, but it never links a blank display to complete failure (it only says to check the display for fault codes).
-->
