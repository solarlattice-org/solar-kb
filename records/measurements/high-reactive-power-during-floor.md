---
id: meas:high-reactive-power-during-floor
type: Measurement
name: Elevated reactive power dispatch
signals:
- point: model_103.VAr
  unit: unit:V-A_Reactive
  pattern: High reactive power output at the same timestamps as DC voltage floor events
- point: model_103.PF
  unit: unit:UNITLESS
  pattern: Power factor away from unity during suspected voltage-floor intervals
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC voltage level or hysteresis behavior coinciding with DC voltage pinned at the minimum
---
Reactive power is reported in var. The plant controller caps how much reactive power the combined elements may be dispatched, with one limit for injection and one for absorption. Injection is the overexcited, positive direction and is allowed only if the maximum limit is set above zero. Absorption is negative and is allowed only if the minimum limit is set below zero. The maximum injection limit can be set from zero up to the nominal reactive power, or up to the site nominal reactive power in the site-level table. Under proportional voltage control, reactive power injection starts only once the voltage rises above the reference voltage by more than the upper deadband. On CPS string inverters, reactive power follows a reactive power versus grid voltage curve. The curve's settings include voltage points, reactive power points, a reference voltage and response times. A revenue meter can log three-phase instantaneous reactive power in VAR, which lets you check the reactive dispatch that was actually delivered. The controller reports the reactive limit maximum and minimum back as feedback points, so the limits in force can be compared with the reactive power logged in monitoring data.

<!-- review notes
- sentence 4: support check: partial - Passage says upper deadband is the minimum voltage difference above reference for regulation to start injecting; 'only once... more than' is close, but it's a minimum difference, not strictly 'more than'.
- sentence 5: support check: partial - Curve parameters (voltage points, Q points, Vref, response times) appear, but the passages never mention CPS string inverters by name or say reactive power follows the curve.
- sentence 6: support check: partial - Q3P is three-phase instantaneous reactive power in VAR, but the passage doesn't mention a revenue meter logging it or checking dispatch delivered.
- sentence 7: support check: partial - Maximum and minimum feedback points exist, but the passages don't state comparison with logged monitoring reactive power or that the controller is what reports them.
-->
