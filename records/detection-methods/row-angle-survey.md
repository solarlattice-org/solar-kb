---
id: method:row-angle-survey
type: DetectionMethod
name: Tracker row angle survey
aliases:
- row-end angle surveys
- inclinometer checks
- field angle measurements
- repeat angle survey
claims:
- claim_id: c1
  rel: produces
  target: meas:tracker-angle-mismatch
  note: Measured row-end or section angles disagree with the commanded angle, or with each other under
    the same command state, beyond the site tolerance. A mismatch between actual and ideal angles can
    point to a mechanical or configuration problem.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  - src: src:alsoenergy-kb-tracker-config-ideal-tracker-angle-calculation
    loc: sec=front
    h: d9cac50a694b
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:row-shadow-line-offset
  note: Row-end shadow lines in drone orthomosaic or oblique imagery are compared with neighbouring rows
    to flag twisted rows, which are then confirmed with field angle measurements.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:motor-block-aligned-loss
  note: Used with drone imagery, command logs and normalized output, row-end angle surveys help show whether
    losses follow grade breaks or motor block boundaries rather than equipment failure.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: drafted
---
A tracker row angle survey measures the real tilt of single-axis tracker rows and compares it with the angle the controller commanded. Take angle measurements with an inclinometer at the drive end, the center and the free end while the row is held at several fixed commanded positions. Before going to the field, compare row-end shadow lines in drone imagery against neighbouring rows to find suspect rows, and check SCADA angle telemetry. Treat it as tracker twist when sections of the same row disagree beyond the site tolerance under the same command. Grade changes from normal terrain-following design are not a defect on their own. On undulating terrain, row-end angle surveys help show whether losses follow grade breaks or motor block boundaries rather than an equipment fault. Controller offsets, failed calibration, bent torque tubes, foundation settlement and loose clamps can produce similar losses, so verify the mechanical geometry before blaming the controls. After a repair, repeat the angle survey and compare normalized power against unaffected rows under stable irradiance.

<!-- review notes
- sentence 2: support check: partial - Field angle measurements at drive end, center, free end at several fixed commanded positions are stated, and inclinometer checks are mentioned, but not explicitly tied together as the tool for those measurements.
- sentence 3: support check: partial - Drone shadow-line comparison and SCADA data are mentioned, but the passages do not explicitly say to do this before going to the field; SCADA angle telemetry is listed as a detection method, and the workflow starts with SCADA, consistent in order.
- sentence 5: support check: partial - The passage supports surveys showing whether losses align with grade breaks or motor blocks, but doesn't specifically mention undulating terrain, though it refers to topographic and grade-related terrain.
-->
