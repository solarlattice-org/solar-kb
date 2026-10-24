---
id: stressor:load-inrush-current
type: Stressor
name: Load inrush current
aliases:
- switch-on currents
- high start-up current demand
- motor starting current
- initial current
- peak inrush current
- starting impact power
---
Load inrush current is the short surge of current a load draws when it is switched on. Motors and other appliances with a high start-up demand are the usual source. On battery or backup inverters, too much load power or start-up demand trips the inverter's AC current limitation on a line conductor. If a motor is driven directly, its starting surge must stay inside the power and time limits of the inverter's overload curve. For RLC loads, the peak inrush current when a load is switched in should stay within twice the inverter's rated current, and the total load should not exceed the inverter's rated power. To reduce exposure, lower the total load or stagger when loads are switched on, and choose appliances with a lower initial current. Start three-phase motors with a star-delta or electronic starter, or connect very large loads directly to the grid supply rather than through the inverter. Inverter datasheets list the inverter's own inrush current. Some models rate it as negligible, and others give a small value over a few milliseconds.

<!-- review notes
- sentence 1: support check: partial - Passages mention peak inrush at load switching and high start-up demand loads (engines), but none define inrush as a short surge drawn on switch-on.
- sentence 2: support check: partial - The AcCurLimSlv2 row says load power too high for slave 2 causes AC current limitation on L3 and mentions high start-up demand, but doesn't say it 'trips' nor specifically battery/backup inverters generally.
- sentence 6: support check: partial - Evidence supports star-delta/electronic start for high-startup three-phase loads and connecting very high power loads directly, but the passage is truncated and doesn't say 'to the grid supply'.
- sentence 1: review: partial - The passages mention peak inrush current at load switching and loads with high start-up demand (engines, motor starting impact), but they never define inrush as a short surge or call motors the usual source.
-->
