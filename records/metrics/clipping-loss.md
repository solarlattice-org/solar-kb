---
id: metric:clipping-loss
type: Metric
name: Clipping loss
aliases:
- inverter clipping loss
category: Performance
claims:
- claim_id: c1
  rel: part_of
  target: concept:energy-loss-waterfall
  note: Clipping is one loss category in the performance waterfall. The waterfall infers DC size, AC capacity
    and effective orientation from historical data, then calculates clipping wherever the AC capacity
    limits output.
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h12
    h: 66cfaabb55b0
  review: drafted
---
Clipping loss is the energy lost when inverter output fails to rise as it should while irradiance increases. In one waterfall analysis, clipping counts as the loss that happens when the inverter's DC input is more than its AC capacity. The analysis estimates DC size, AC capacity and effective tilt and azimuth from historical data. In the PowerTrack loss table, clipping loss is the sum of two parts: the loss from reaching maximum inverter output (called Inverter Limit) and clipping below that limit from other causes. The PV model loss definitions separate the two by a threshold. Flat power below 96 percent of the inverter's rated output while irradiance rises counts as Clipping Loss. Flat power at or above 96 percent counts as Inverter Limit Loss. Inverter Limit Loss gets its own category because inverters are expected to clip at rated output when available DC power is more than they can handle. The losses are calculated from PV model parameters using measured irradiance and module temperature. Accurate results need a well-tuned model and good sensor data. Clipping power is one of the terms subtracted when residual loss is calculated. A performance alert flags clipping loss above 1 percent as a loss that may need intervention. With a DC-coupled battery, energy that would be clipped can charge the battery instead.
