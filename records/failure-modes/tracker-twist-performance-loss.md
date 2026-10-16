---
id: fm:tracker-twist-performance-loss
type: FailureMode
name: Performance Loss from Tracker Twist
claims:
- claim_id: c1
  rel: affects
  target: comp:single-axis-tracker
  note: Torque tube, slew drive, bearings, dampers or linked segments stop holding a common plane.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  rel: caused_by
  target: stressor:mounting-structure-defect
  note: Bent, loose, slipping or deformed tracker hardware such as couplers, bearings, torque tube joints,
    dampers and actuator mounts.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passages mention loose/deformed/slipping hardware (couplers,
    bearings, joints, dampers, actuator mounts) as things to inspect and bent/loose members to repair,
    but don''t explicitly state twist is caused by a mounting structure defect; they also list controller
    offsets as alternative causes.'
- claim_id: c3
  rel: presents_as
  target: symptom:nonuniform-tracker-angles
  note: One end or section of a row sits at a different tilt from the rest under the same command.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: presents_as
  target: symptom:sun-position-repeatable-loss
  note: Most visible at low sun angles, during backtracking transitions and in windy periods; a row may
    look fine at one position and fail at another.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: presents_as
  target: symptom:string-current-low
  note: Affected rows show lower normalized current than neighboring rows while modules, inverters and
    sensors look healthy.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: presents_as
  target: symptom:inter-row-shading
  note: A twisted section can rise or drop outside the expected backtracking geometry.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: presents_as
  target: symptom:uneven-string-current
  note: On long rows, parallel strings on the same tracker get unequal irradiance, which causes electrical
    mismatch.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: detected_by
  target: method:performance-monitoring
  note: Use SCADA and controller data to find rows that underperform after normalizing for irradiance
    and clipping; compare morning, noon and afternoon windows.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c9
  rel: detected_by
  target: method:tracker-command-log-review
  note: Compare the commanded angle with the measured row-end angles and the SCADA angle telemetry.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c10
  rel: detected_by
  target: method:drone-inspection
  note: Use an orthomosaic or oblique images to compare row-end shadow lines with neighboring rows.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c11
  rel: detected_by
  target: method:row-angle-survey
  note: Take inclinometer readings at the drive end, center and free end with the row commanded to several
    fixed positions.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c12
  rel: mitigated_by
  target: mit:tracker-geometry-correction
  note: Correct the torque tube alignment.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c13
  rel: mitigated_by
  target: mit:actuator-calibration
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c14
  rel: mitigated_by
  target: mit:structural-hardware-repair
  note: Repair bent or loose mechanical members.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: mitigated_by
  target: mit:backtracking-tuning
  note: Verify the backtracking settings.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c16
  rel: mitigated_by
  target: mit:root-cause-investigation
  note: Verify the mechanical geometry before blaming tracker controls. Controller offsets, failed calibration,
    bent tubes, terrain movement, foundation settlement and loose clamps can all look similar.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h7
    h: 497a3230089b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c17
  rel: mitigated_by
  target: mit:post-repair-verification
  note: After repair, repeat the angle survey and compare normalized power with unaffected rows under
    stable irradiance, through morning and afternoon sweeps.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h7
    h: 497a3230089b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c18
  rel: distinguished_from
  target: fm:terrain-undulation-yield-losses
  by: method:row-angle-survey
  note: A terrain-following tracker can follow grade changes and still hold its commanded rotation. Treat
    it as twist only when measured row sections disagree beyond site tolerance under the same command.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - u7 supports the terrain-following vs twist distinction and tolerance
    criterion, but doesn''t name terrain undulation yield losses or explicitly say a row angle survey
    is the discriminating method (measured sections are mentioned).'
---
It costs energy through cosine loss and row-to-row shading, and on long rows it causes mismatch between parallel strings. Look for rows with lower normalized current than their neighbors, mostly at low sun angles, during backtracking transitions and in wind, while modules and inverters look healthy. Screen with SCADA and controller data across morning, noon and afternoon windows, then compare row-end shadow lines in drone images. Confirm with angle readings at the drive end, center and free end at several commanded positions, and inspect couplers, bearings, joints, dampers and actuator mounts for slip or damage. Do not blame the controls until the mechanical geometry is checked, and do not mistake intended terrain-following grade changes for twist. Fix it by correcting actuator calibration and torque tube alignment, repairing bent or loose parts and checking backtracking settings. Then repeat the angle survey and compare normalized power with healthy rows.
