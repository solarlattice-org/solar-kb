---
id: symptom:sun-position-repeatable-loss
type: Symptom
name: Time-of-day repeatable loss
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grade-break-aligned-loss
  note: Terrain undulation losses cluster at grade breaks, swales and rolling sections, and are strongest
    at low sun angles.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:motor-block-aligned-loss
  note: Large motor blocks spanning several terrain conditions force one command angle across rows, raising
    shading or cosine loss.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
  review_note: 'support check: partial - Motor block clustering, sun-position repeatability and large
    blocks forcing one angle (shading/cosine loss) are stated, but ''mainly during backtracking'' is not
    explicitly tied to motor-block loss.'
- claim_id: c3
  rel: observed_as
  target: meas:low-normalized-row-current
  note: Twisted rows can show lower normalized current than neighbors while modules, inverters and irradiance
    sensors look healthy; may look acceptable at one sun position and fail at another.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:tracker-angle-mismatch
  note: Measured row-end angles differ from the commanded angle or from other sections of the same row
    under the same command state.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:row-shadow-line-offset
  note: Drone orthomosaic or oblique imagery shows row-end shadow lines that differ from neighboring rows.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
This symptom is a production loss that comes back each day at the same sun positions. It is usually worst at low sun angles and during backtracking. Shading at a specific site is a typical cause of losses that cut power at fixed times of day. Compare irradiance-normalized row, string or inverter output across the morning, solar-noon and afternoon windows. First remove intervals affected by clipping, curtailment, outages and inverter limits. With terrain undulation, the losses cluster at grade breaks, swales, rolling ground and motor block boundaries, even while the trackers follow their commands correctly. With tracker twist, one end or section of a row sits at a different tilt from the rest. That row shows lower normalized current than its neighbors, and the effect can also show up in windy intervals. To tell them apart, check angles at the drive end, center and free end with the row commanded to several fixed positions. Twist means sections of one row disagree beyond the site tolerance under the same command. A terrain-following design can be intentional and still hold a common plane. Drone imagery of row-end shadow lines, tracker command logs and topographic survey comparisons help locate the cause. Also check for controller offsets, bent torque tubes, foundation settlement or loose clamps.
