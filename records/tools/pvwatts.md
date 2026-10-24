---
id: tool:pvwatts
type: Tool
name: PVWatts
aliases:
- PVWatts calculator
- NREL PV Watts
- PVWATTS v.1
- PVWATTS v.2
- PVWatts Version 5 Calculator
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:nrel
  note: Produced by the National Renewable Energy Laboratory.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=h118
    h: 4e99aaab8d1f
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h40
    h: bcf4e91cdb34
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
PVWatts is an online software model from NREL that estimates the energy production of grid-connected PV systems. The user picks a site location and enters or accepts defaults for array size, array type and mounting, efficiency or derating factors, tilt, azimuth and electricity cost. It runs an hour-by-hour simulation using typical meteorological year weather data, applies losses including DC to AC conversion, and sums the hourly AC energy into monthly and annual production and energy value. It can also output hourly performance data for the chosen location. Running several scenarios helps compare design changes such as system size, tilt and orientation, and helps match PV output to seasonal loads. PVWatts is the simulation engine inside the System Advisor Model, but the calculator itself has a more basic interface and gives only energy predictions. It is described as a simple-to-use PV system energy model, and it has been used in studies of PV performance loss rates.

<!-- review notes
- sentence 7: support check: partial - The title supports 'simple-to-use PV system energy model', but the 'YOY: YoY2' snippet does not clearly state it was used in studies of PV performance loss rates.
- sentence 7: review: partial - The table title supports 'simple-to-use PV system energy model', but the bare 'PVWatts; YOY: YoY2' row does not clearly show it was used in studies of performance loss rates.
-->
