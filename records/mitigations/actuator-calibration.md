---
id: mit:actuator-calibration
type: Mitigation
name: Actuator calibration
---
Twist causes cosine loss, shading between rows and mismatch between strings, and it can lower output across a whole tracker block. Calibration is done together with correcting torque tube alignment, repairing bent or loose mechanical members and checking the backtracking settings. This means recalibrating the actuator may not recover the loss if the real cause is mechanical damage or ground movement. Treat a row as twisted only when measured sections disagree by more than the site tolerance under the same command. Intentional terrain-following installs are not a defect. After the work, retest row angle and normalized power in both morning and afternoon sweep windows. Confirm with a repeat angle survey and compare against unaffected rows under stable irradiance.

<!-- review notes
- sentence 3: support check: partial - Notes say not to attribute loss solely to controls since mechanical causes give similar signatures, but don't explicitly say recalibration may fail to recover the loss.
- sentence 4: support check: partial - Defect when sections disagree beyond site tolerance under same command and terrain-following is distinct, but 'only when' is slightly stronger than the passage.
-->
