---
id: meas:grid-voltage-rise-with-power
type: Measurement
name: Grid voltage rise with power
status: proposed
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage climbs as exported power rises, approaching the overvoltage limit at high
    output
- point: model_103.W
  unit: unit:W
  pattern: High AC power coincides with the highest grid voltage, followed by a sudden trip to zero
---
