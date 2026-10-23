---
id: meas:setpoint-feedback-mismatch
type: Measurement
name: Setpoint feedback mismatch
---
Some plant controllers expose feedback points that report back the real and reactive power setpoints the device is applying. You can compare these with the setpoints the dispatcher sent. The real power feedback points are reported per unit of rated power (Wpu), and the reactive power feedback points per unit of rated reactive power (Varpu). Check that the commanded values use the same per-unit scaling before you call it a mismatch. A mismatch can be expected behaviour. A controller treats a setpoint as invalid if no configuration exists for it or if it falls outside the configured value range. It then applies fallback setpoints instead of the commanded value. If no setpoint arrives within a configurable time, the controller keeps the last valid value for a limited time and then switches to the configured fallback values. It returns to the current setpoint once a valid one is received again. On some central inverters, invalid content in the power setpoint information shows up as the ComInvalid display message. The fix is to check the power specification settings. Event logs that record when the setpoint specification was activated or deactivated help show which setpoint source was active when the mismatch occurred.

<!-- review notes
- sentence 1: support check: partial - Feedback points for real and reactive power setpoints exist, but the passages say nothing about comparing them with dispatcher setpoints or about which controllers expose them.
- sentence 2: support check: partial - Units Wpu and Varpu are listed for the points, but 'per unit of rated power' and the advice to check commanded scaling are not stated.
- sentence 3: support check: partial - Invalid-setpoint criteria and fallback are stated, but the passage doesn't say a mismatch can be expected behaviour, and the fallback applies only if activated and configured.
- sentence 4: support check: partial - The retain-then-fallback-then-resume sequence is stated, but the retention time is described as configurable and the fallback only applies if activated and configured.
- sentence 5: support check: partial - ComInvalid with invalid power setpoint content and checking the power specification settings is stated, but only when mode WCtlCom is selected, and 'some central inverters' isn't stated.
- sentence 6: support check: partial - Events 8706 and 8707 for setpoint spec activated and deactivated exist, but the passages don't say they help identify the active setpoint source during a mismatch.
-->
