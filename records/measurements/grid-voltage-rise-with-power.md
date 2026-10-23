---
id: meas:grid-voltage-rise-with-power
type: Measurement
name: Grid voltage rise with power
aliases:
- VRise
- AC line voltage rise
- rise-in-voltage
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage climbs as exported power rises, approaching the overvoltage limit at high
    output
- point: model_103.W
  unit: unit:W
  pattern: High AC power coincides with the highest grid voltage, followed by a sudden trip to zero
---
When a PV system feeds net power into the grid, the voltage at its connection point goes up in proportion to the power injected. The pattern is hard to see on a small system. It becomes visible when the system is large compared with feeder demand, or when many systems in an area share one feeder. Plotting relative voltage rise against system yield gives a virtual grid impedance. A steep slope means the feeder has high resistance or already carries a lot of PV, and the method assumes unity power factor with no reactive power supplied. Some of the rise can come from the site's own wiring between the inverter and the grid connection, mainly because of a long run to the point of common coupling or undersized conductors. If the voltage passes the inverter's overvoltage setting, the inverter disconnects and the voltage drops. After the reconnection time the inverter restarts and the voltage climbs again, and it can take seconds, minutes or longer before the next trip. Some inverters log a grid incident and disconnect when the grid voltage or grid impedance at their connection point is too high. This links the signature to high grid impedance. Some inverters can limit voltage rise by supplying reactive power and cutting active power once the output voltage passes a set level. This can avoid a disconnection.

<!-- review notes
- sentence 3: support check: partial - Passage gives z as the virtual grid impedance in the voltage rise vs yield relation, high z meaning high resistance or much PV, and unity power factor; it does not mention plotting or a slope explicitly.
- sentence 7: support check: partial - Passages state SUN2000 voltage rise suppression delivers reactive power and decreases active power above a voltage level, and another inverter derates to prevent disconnection; the claim that this avoids disconnection is only stated for derating, not reactive power.
-->
