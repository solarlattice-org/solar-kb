---
id: meas:row-shadow-line-offset
type: Measurement
name: Row shadow line offset
---
In a drone orthomosaic or oblique image, the shadow line at the end of a tracker row does not line up with the shadow lines of the rows beside it. The main failure mode behind it is tracker twist. A twisted section can rise or fall outside the expected backtracking geometry and shade the next row. To confirm, command the row to several fixed positions and measure its angle at the drive end, the center and the free end. Check the commanded tracker angle against the row-end angles you measured from drone imagery, inclinometer checks and SCADA angle telemetry. Do not mistake intentional terrain-following installation for a defect. Treat it as twist only when sections of the same row, under the same command, disagree by more than the site tolerance. Undulating terrain can also cause uneven tracker angles, uneven apparent row spacing and heavy local shading, so check grade changes and motor block boundaries too. Rows with this offset may show lower normalized current than the rows next to them. The loss is usually easiest to see at low sun angles, during backtracking transitions and in windy periods.

<!-- review notes
- sentence 2: support check: partial - The passages say twist can cause row-to-row shading when a section rises or falls outside the backtracking geometry, but they don't say twist is the main failure mode behind misaligned shadow lines.
- sentence 6: support check: partial - Terrain undulation causing uneven apparent spacing, nonuniform angles, local shading and clustering at motor block boundaries and grade breaks is stated, but the passage doesn't say 'heavy' shading or give an instruction to check these as a twist diagnostic.
-->
