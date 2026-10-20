---
id: stressor:high-dc-ac-ratio
type: Stressor
name: High DC/AC ratio
---
A high DC/AC ratio means the PV array can deliver more DC power than the inverter is rated to export as AC power. When the DC input exceeds the inverter's AC capacity, the inverter holds its output at that limit, and the energy above the limit is lost. This is called inverter clipping. Clipping losses happen mostly during peak sun hours and on the sunnier days of the year. Clipping is not always a fault. Designers often oversize the array on purpose to get more energy in the morning and evening, accepting some lost output at midday. Inverter makers set a maximum allowed DC/AC ratio and a short-circuit current limit. Going past either limit can damage the inverter, and that damage may not be covered by the warranty. Monitoring software can estimate clipping losses by modelling the DC array size against the inverter's AC limit, so expected output is capped wherever the AC capacity limits it. Do not mix up clipping with voltage-floor losses. Clipping is a cap on power, while voltage flooring comes from the inverter's DC voltage window, and the two need different fixes.

<!-- review notes
- sentence 1: support check: partial - Passages describe DC exceeding inverter AC capacity causing clipping, but never define 'high DC/AC ratio' explicitly; it's implied only.
- sentence 4: support check: partial - Passage says not all clipping is a fault and is sometimes designed for morning/evening yield, but 'designers often' overstates 'at times'.
- sentence 5: support check: partial - Passages give max DC/AC ratios and say failing to stay within DC/AC and Isc limits may cause damage not covered by warranty, but 'inverter makers set' and the damage-to-inverter detail are mostly implied.
-->
