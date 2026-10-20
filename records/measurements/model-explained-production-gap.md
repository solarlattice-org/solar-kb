---
id: meas:model-explained-production-gap
type: Measurement
name: Model-explained production gap
signals:
- point: model_103.W
  unit: unit:W
  pattern: Measured AC power stays persistently below the modeled baseline; the shortfall shrinks or disappears
    when the module file parameters are varied in sensitivity cases
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: Plane-of-array irradiance used as model input for the sensitivity cases; no irradiance anomaly
    explains the gap
---
This signature is a lasting gap between expected and measured plant output that is still there after weather, availability, clipping, curtailment, soiling, degradation and instrument problems have been checked. The plant itself may be running normally. The gap comes from a wrong baseline expectation, not from a physical fault. A typical cause is Flawed PAN File Yield Losses: the module parameter file used in PVsyst or a similar energy model does not match how the modules actually behave. To confirm it, identify the exact PAN file used, including its source, version and any manual edits. Then compare it with datasheets, independent lab measurements, third-party PAN files and measured site behavior. Run sensitivity cases to check whether the model parameters plausibly explain the gap. Keep this analysis separate from real operational losses so that a baseline error is not treated as a field defect that can be repaired. The shading model can also shift the expected value. Monitoring platforms count shade as a percentage loss of irradiance and do not model how partially shaded modules interact electrically, so the expected value is only approximate. Derate settings and modeled loss steps also move the expected production up or down. Check them before you treat a gap as underperformance. Different snow loss models run on the same weather data can give very different results, so a gap may reflect the model chosen rather than how the plant performs.

<!-- review notes
- sentence 6: support check: partial - The passage supports shade being modeled as a percentage irradiance loss and ignoring the electrical interaction of partially shaded modules, but it does not say monitoring platforms in general do this, and 'shift the expected value' is only implied.
- sentence 7: support check: partial - The passage says derates and loss factors shift the expected production up or down, but it doesn't say to check them before treating a gap as underperformance.
-->
