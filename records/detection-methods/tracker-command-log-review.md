---
id: method:tracker-command-log-review
type: DetectionMethod
name: Tracker command log review
aliases:
- tracker command logs
- tracker controller logs
- tracker stow telemetry
- SCADA angle telemetry
claims:
- claim_id: c1
  rel: produces
  target: meas:stow-event-output-dip
  note: Timestamped stow commands and return-to-track events from the controller log are lined up with
    SCADA production and irradiance. Stow loss then shows up as dips in output while irradiance would
    support production, so it can be separated from clipping, curtailment, outages and sensor faults.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  review: drafted
  review_note: 'support check: partial - Passages support aligning stow commands with production/irradiance
    and separating from clipping etc., but the specific signals (model_103.W, model_302.POAI, model_307.WndSpd,
    gusts at or above threshold) are only loosely supported.'
- claim_id: c2
  rel: produces
  target: meas:motor-block-aligned-loss
  note: Tracker command logs, combined with angle surveys and normalized output, show whether losses line
    up with grade breaks or motor block boundaries rather than with equipment failure. These losses tend
    to be strongest at low sun angles.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
  review_note: 'support check: partial - Command logs/angle surveys/normalized output showing alignment
    with motor block boundaries and strongest losses at low sun are stated, but the specific string-current
    signal during morning/afternoon backtracking windows is not explicitly stated.'
---
Tracker command log review means pulling the tracker controller's logged commands and events and comparing them with production and weather data. This separates stow loss from clipping, grid curtailment, outages and sensor faults; high-frequency gust data explains tracker behaviour better than hourly averages. For tracker twist, the commanded angle is checked against measured row-end angles from drone imagery, inclinometers or SCADA angle telemetry, together with irradiance-normalized string output. For terrain undulation, command logs plus angle surveys and normalized output show whether losses line up with grade breaks or motor block boundaries. A tracker that follows its command is not proof of good performance, because on undulating terrain the command itself can cause the loss. Before you blame the controls, verify the mechanical geometry, since bent torque tubes, loose clamps or foundation settlement can produce the same production signatures. Do not lower stow thresholds to recover energy unless the tracker supplier and a structural engineer confirm the change stays within the design envelope.
