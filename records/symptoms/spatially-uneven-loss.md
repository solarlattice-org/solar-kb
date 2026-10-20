---
id: symptom:spatially-uneven-loss
type: Symptom
name: Spatially uneven loss
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grade-break-aligned-loss
  note: Terrain undulation losses can cluster at grade breaks, swales and rolling sections that differ
    from the modeled representative slope; strongest at low sun angles.
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
  note: Recoverable energy losses concentrated in specific tracker motor blocks or clustered at motor
    block boundaries.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:inverter-normalized-yield-spread
  note: Uneven power reduction across a large plant; compare normalized row or inverter production across
    zones and across morning and afternoon windows.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  - src: src:iea-pvps-t13-21-2022
    loc: tbl=4
    h: 29ce7be13dc7
  review: drafted
  review_note: 'support check: partial - Passages say to compare normalized row/inverter production across
    zones and morning/afternoon and cite a figure of uneven power reduction, but do not state irradiance
    is uniform or POA normalization.'
- claim_id: c4
  rel: observed_as
  target: meas:string-current-below-average
  note: Nonuniform dust deposition gives strings or substrings different effective irradiance, causing
    mismatch.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h5
    h: 43575746a7d7
  review: drafted
  review_note: 'support check: partial - Nonuniform deposition causing mismatch between strings/substrings
    is stated, but not that some string currents are lower on the same inverter where dust is heavier
    (though module current falls with deposition).'
---
Spatially uneven loss means some zones, rows or strings of a plant lose more energy than others under the same irradiance. With granular dust soiling the loss is usually spread over a zone, but roads, exposed soil, farming, construction, prevailing wind and row edges can make some areas much dirtier than others. Uneven dust gives strings or substrings different effective irradiance, so look for mismatch in string currents and check whether the loss slowly builds in dry weather and then recovers after rain or washing. With terrain undulation yield losses the loss repeats with sun position, is worst at low sun angles, and clusters at motor block boundaries, grade breaks, swales and rolling ground. A tracker that follows its commanded angle can still lose energy on undulating ground, because the command itself may come from a terrain model or block layout that is too coarse. First map the underperformance against block IDs, row locations and time of day, and compare it with topographic survey data and as-builts. Then separate out curtailment, clipping, outages and inverter limits, and use drone imagery, row-end angle surveys, tracker command logs and normalized string or inverter output to see whether the loss follows terrain or points to equipment failure. Do not measure dust soiling from one dirty irradiance sensor alone, because drift, poor cleaning or a local obstruction can look like soiling.

<!-- review notes
- sentence 1: support check: partial - Passages show spatially uneven loss across zones and a figure on uneven power reduction, but do not define it as rows/strings losing more under the same irradiance.
- sentence 2: support check: partial - Broad across zone with listed causes making it uneven is stated, but 'much dirtier' overstates what the passage says.
- sentence 3: support check: partial - Mismatch from different effective irradiance and dry-period buildup with recovery after rain/washing are stated, but looking for mismatch in string currents specifically is not stated as guidance.
-->
