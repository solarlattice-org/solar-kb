---
id: meas:overvoltage-trip-reconnect-cycle
type: Measurement
name: Repeated trip-reconnect cycling
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero and recovers again and again during high production
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC voltage falls at each disconnect and climbs back after each reconnect
---
Inverters and battery systems can be set to stop operating when meter readings show grid voltage above one of several overvoltage trip levels, each with its own threshold and timeout. Some inverters also trip on a moving average of grid voltage, with a separate trip time for that filtered value. The high voltage trip threshold is set as a percentage of nominal voltage. After a trip, the unit reconnects only when grid voltage drops below a maximum reconnect or recovery voltage setting. A reconnect or recovery timer must also run out after the grid comes back inside the allowed voltage and frequency windows. Only then does the unit start producing again.

<!-- review notes
- sentence 4: support check: partial - Reconnect Max Voltage and recovery thresholds for max grid voltage are stated, but the passages don't say the unit reconnects 'only' when voltage drops below it or describe the post-trip reconnection logic explicitly.
-->
