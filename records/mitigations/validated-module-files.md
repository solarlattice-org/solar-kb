---
id: mit:validated-module-files
type: Mitigation
name: Validated module model files
---
Using validated module files means basing the energy model on a module performance (PAN) file that has been checked against independent data. Simply trusting the file that came with the module is not enough. It addresses Flawed PAN File Yield Losses. In this failure mode, a wrong or unrepresentative module file biases simulated performance, so expected yield differs from what the plant really does even when nothing is physically wrong. The PAN file describes the module's electrical behaviour, temperature response, low-light performance and incidence angle assumptions. If these parameters are optimistic or do not match the delivered modules, the model can overstate energy. Find the exact file used for the energy estimate, including its source, version and any manual edits. Then compare it with datasheets, independent lab measurements, third-party PAN files and measured site behaviour. Record which PAN source and version was chosen, run sensitivity cases, and update forecasts when independent testing shows important parameter differences. Treat the module file as a controlled modelling input. Using different module files across teams makes design comparisons and operational diagnosis inconsistent. Module data entered incorrectly in the model is a recognised modelling cause of performance gaps. This action fixes the model baseline, not the plant. Keep it separate from real operating losses so that a model error is not mistaken for a field defect that needs repair.

<!-- review notes
- sentence 1: support check: partial - Passages say to use validated module files and validate parameters against independent test data, but do not explicitly say that simply trusting the manufacturer-supplied file is insufficient.
- sentence 6: support check: partial - Engineering notes support treating PAN provenance as a controlled input and the risk of inconsistent representations across teams, but they speak of provenance and not explicitly of 'different module files' making comparisons inconsistent.
-->
