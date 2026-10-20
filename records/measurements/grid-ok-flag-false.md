---
id: meas:grid-ok-flag-false
type: Measurement
name: Grid OK flag false
status: proposed
signals:
- point: model_103.Hz
  unit: unit:HZ
  pattern: Grid frequency moves outside the reconnect window, or reads zero when the grid is gone
- point: model_103.PhVphA
  unit: unit:V
  pattern: Grid voltage is outside the reconnect window or missing
---
