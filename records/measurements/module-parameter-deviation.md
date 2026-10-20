---
id: meas:module-parameter-deviation
type: Measurement
name: Module parameter deviation
aliases:
- material parameter differences
---
This signature is a mismatch between the module parameters in the PAN file used for design or financing and the module's actual behavior, as shown by independent test data or by a different version of the file. To find it, compare the manufacturer's PAN file with third-party files and check the parameters against independent test data. In the field it shows up as a lasting gap between expected and measured performance. The gap remains after weather, availability, clipping, curtailment, soiling, degradation and instrumentation have all been checked. The plant itself may be running normally, because the error is in the modeled baseline and not in the hardware. This is the failure mode called flawed PAN file yield losses. Module data entered incorrectly into a model is also listed as a modelling cause of differences between measured and predicted IV curves. Lab IV measurements also carry uncertainty: most laboratories find it hard to certify module IV characteristics more accurately than about 3%. Keep this in mind before calling a small difference a real parameter deviation. Treat the PAN file's source and version as a controlled input. If different teams use different module representations, design comparisons and operational diagnoses can disagree with each other.

<!-- review notes
- sentence 5: support check: partial - Passages list 'PV module data incorrectly entered' under modelling causes, but don't show the context of differences between measured and predicted IV curves nor the 'also' framing.
- sentence 6: support check: partial - The passage says better than 3% certified accuracy is commonly difficult for most laboratories; the advice not to call small differences real deviations is not stated.
-->
