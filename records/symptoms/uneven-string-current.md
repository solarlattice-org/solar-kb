---
id: symptom:uneven-string-current
type: Symptom
name: Uneven string current
aliases:
- electrical mismatch
- partial-string mismatch
claims:
- claim_id: c1
  rel: observed_as
  target: meas:string-current-below-average
  note: Monitoring alerts compare normalized string DC current with the best-performing string on the
    same component. By default an alert opens below a ratio of 0.8 held for 2 hours of daylight; this
    is an alert setting.
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h2
    h: 4ec2fde2d167
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:low-normalized-row-current
  note: With tracker twist, the affected rows show lower irradiance-normalized current than neighbouring
    rows, even when the modules, inverters and sensors look healthy.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h5
    h: 38a22f4e3727
  review: drafted
  review_note: 'support check: partial - Tracker twist lower normalized current than adjacent rows at
    low sun/backtracking is stated, but POA normalization and irradiance appearing normal are only loosely
    supported (irradiance sensors appear healthy).'
---
Uneven string current means strings that should match, on the same inverter or tracker, carry noticeably different currents. You can see it in string-level monitoring or in inverter string-failure detection, which compares each input with the mean or with the best string. Snow is one cause: when it only partly clears during melt or slide-off, clear cells and covered cells run at different currents. That loss lines up with snowfall and recovery periods and shows up on site cameras. Tracker twist is another cause: parallel strings on a twisted row no longer get the same irradiance. That loss depends on time of day and is worst at low sun angles, during backtracking and in wind. To confirm twist, compare the commanded tracker angle with angles measured along the row, and check row-end shadow lines in drone imagery. First, make sure the strings really are comparable. Normalize for different string sizes, and group inputs that share shading, alignment and module type. Then check the number of modules in the string, shading and module orientation. Do the current comparison under stable irradiance, or use a reference string or an IV curve test.

<!-- review notes
- sentence 3: support check: partial - Partial clearing mismatch and snowfall/recovery timing are stated, and camera observations appear only in the detection method, but not explicitly as the loss showing up on cameras; still largely supported.
-->
