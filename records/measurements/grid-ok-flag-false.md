---
id: meas:grid-ok-flag-false
type: Measurement
name: Grid OK flag false
aliases:
- Grid OK
signals:
- point: model_103.Hz
  unit: unit:HZ
  pattern: Grid frequency moves outside the reconnect window, or reads zero when the grid is gone
- point: model_103.PhVphA
  unit: unit:V
  pattern: Grid voltage is outside the reconnect window or missing
---
Grid OK is a boolean output of the islanding controller. It is read-only and can be read over Modbus starting at register 29026. The flag shows whether grid voltage and frequency are inside the reconnect thresholds set in the islanding controller. A false value means the grid is not inside those reconnect limits. Check it together with the Breaker Closed point at register 29025. A value of 0 there means the islanding breaker is open and the system is off-grid. To find out which grid value is out of range, read the grid-side voltage and frequency that the islanding controller measures, starting at registers 29015 and 29017. Do not mix this flag up with OK to Island. That is a separate readiness point based on battery capacity and state of energy. When OK to Island is false, the islanding breaker cannot trip and the system cannot go off-grid.

<!-- review notes
- sentence 3: support check: partial - Breaker Closed at 29025 with 0 meaning open/off-grid is stated, but the passages don't say to check it together with Grid OK.
- sentence 4: support check: partial - Grid voltage (29015) and frequency (29017) measured by the islanding controller are listed, but the passages don't say to use them to diagnose which value is out of range.
- sentence 5: support check: partial - OK to Island false blocks breaker trip and off-grid transition, and it is based on battery capacity and SOE; the passages don't say it is distinct from Grid OK, though that is implied by the separate definitions.
-->
