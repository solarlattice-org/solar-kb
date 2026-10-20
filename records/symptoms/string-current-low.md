---
id: symptom:string-current-low
type: Symptom
name: Reduced string current
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-string-isc
  note: Measured during commissioning or a fault test and compared with expected value and with identical
    strings under stable irradiance.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.5.2.1
    h: d4e5d5d644a3
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passage supports measuring string Isc and comparing with expected
    value and identical strings under stable irradiance (within ~5%), but doesn''t state that low Isc
    is the observed signature of reduced string current beyond comparison.'
- claim_id: c2
  rel: observed_as
  target: meas:low-normalized-row-current
  note: For tracker twist, rows show lower POA-normalized current than adjacent rows, mostly at low sun
    angles, during backtracking transitions and in wind.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  review: drafted
---
Reduced string current means one string carries less DC current than identical strings, or less than expected, at the same irradiance. It is found with string-level monitoring or clip-on ammeter checks. Monitoring platforms flag a string when its normalized current stays below the best string of the same component for a set period. Under stable irradiance, identical strings should normally agree within 5 % of the average. String current monitoring at a resolution of 15 minutes or finer gives more precise troubleshooting than inverter-level data. A low string can be caused by a cable defect, a module hotspot from cell damage, or glass breakage. A badly broken module can lower current and power in the whole string. Granular dust soiling lowers current gradually during dry periods and recovers after rain or washing. The loss usually covers a whole zone, so many strings drop together. With tracker twist, the loss depends on time of day: affected rows show lower normalized current than neighboring rows, mostly at low sun angles and during backtracking, while modules and inverters look healthy. To check, first normalize the string by irradiance and compare it with its neighbors. Then use an IR scan, an IV curve and a visual inspection of the affected modules and cables. Check the current again after any repair.

<!-- review notes
- sentence 2: support check: partial - Alert relative to highest-performing string over a time threshold and the 5% agreement are supported, but the 'normalized current' flagging is a specific platform's feature, generalized to 'monitoring platforms'; also threshold is 80% ratio, not stated—minor.
- sentence 3: support check: partial - Passages say string-level monitoring is more precise than inverter level and recommend 15-minute resolution (up to/at least 15 min), but not that 'finer' resolution gives more precision.
- sentence 7: support check: partial - IR scan, IV curve, visual inspection and retesting current after repair are supported, but the first step of irradiance-normalizing and comparing with neighbors is only supported for trackers, not for this general string workflow.
-->
