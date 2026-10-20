---
id: meas:tracker-angle-mismatch
type: Measurement
name: Tracker angle mismatch
---
Tracker angle mismatch means the angle a tracker row actually holds does not agree with the angle it should hold. One example is a gap between a calculated ideal tilt angle and the setpoints and positions the tracker device reports. This kind of mismatch can point to a mechanical or configuration problem, and it lowers energy harvest. To find tracker twist, compare the commanded angle with angles measured at the row ends. Use drone imagery, inclinometer checks, SCADA angle telemetry and string output normalized to plane-of-array irradiance. In a twisted row, one end or one section sits at a different tilt from the rest of the row, even though the row may still respond to commands. Do not confuse twist with a tracker designed to follow the terrain. Treat it as a defect when measured row sections disagree by more than the site tolerance under the same command. On undulating terrain, tracker angles can be nonuniform even when rows follow their commands. A row that tracks its commanded angle is therefore not proof that the geometry is right.

<!-- review notes
- sentence 5: support check: partial - The passages say to separate twist from terrain-following design and to treat twist as a defect when sections disagree beyond site tolerance under the same command state. 'More than the site tolerance' is stated, but nothing in them says to treat twist as a defect only in that case, so the statement is slightly stronger.
-->
