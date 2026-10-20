---
id: meas:post-rain-production-recovery
type: Measurement
name: Production recovery after rain
signals:
- point: model_307.Rain
  unit: unit:MilliM
  pattern: meaningful or heavy rainfall event recorded
- point: model_103.W
  unit: unit:W
  pattern: irradiance-normalized output declines gradually over dry period, then steps up after rain
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used to normalize output; no matching irradiance change explains the step
---
The signature is a slow drop in irradiance-normalized production during dry weather, then a partial or full rebound after significant rain or a wash. The plant stays online during the decline because the loss comes from less light reaching the cells, not from an equipment outage. Granular dust soiling is the failure mode that typically produces this pattern. The loss is often broad across a zone, but roads, exposed soil, farming, construction, wind and row edges can make it uneven. Before assigning the decline to soiling, rule out availability losses, clipping, curtailment and irradiance sensor problems. Then compare the trend with rainfall, soiling station data, cleaning logs and nearby reference blocks. Tracking how efficiency falls during rain-free periods or between cleanings gives an approximate soiling effect and helps time washes. Check whether the soiling model reproduces the observed recovery after rain or cleaning. If it does not, adjust the local accumulation and wash-off assumptions. If output does not recover after rain but improves after manual cleaning, that points to fungal or biological soiling rather than ordinary dust.

<!-- review notes
- sentence 4: support check: partial - Passage lists ruling out availability, clipping, curtailment, irradiance sensor issues and comparing with rainfall, soiling stations, cleaning logs, reference blocks, but 'when available' qualifier is dropped and ordering/'before assigning' is implied rather than stated.
-->
