---
id: meas:overvoltage-trip-reconnect-cycle
type: Measurement
name: Repeated trip-reconnect cycling
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero and recovers again and again during high production
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC voltage falls at each disconnect and climbs back after each reconnect
---
