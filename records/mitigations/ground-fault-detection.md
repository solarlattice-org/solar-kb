---
id: mit:ground-fault-detection
type: Mitigation
name: Continuous ground fault detection
aliases:
- GFCI
- residual current detection
- Ground fault monitoring
- Ground Fault Detector
- GFD
- GFDI
---
Continuous ground fault detection means the inverter or another device checks for ground faults at all times. It is recommended as a corrective action for backsheet chalking, together with regular inspections that track how the failure progresses. For backsheet cracking it is listed as a preventive action, along with checking that the IEC 61215 certification and bill of materials are valid and inspecting modules visually before installation. It matters because an ageing backsheet can crack and lose its insulating properties, which is a serious safety hazard. Inverters do this with residual current detection, as UL 1741 requires: when a ground fault in the array causes leakage current, the inverter raises an alarm and stops operating. The trip limit depends on the model: one inverter shuts down above 500 mA of leakage current, while another lists a GFDI trip limit of 300 mA. Detection only reports an insulation fault after it happens. Chalking does not reliably predict cracking or insulation loss, so modules with a direct safety risk, or that fail insulation or wet-leakage tests, still need to be replaced.

<!-- review notes
- sentence 3: support check: partial - Backsheet cracking entries list ground fault detection together with IEC 61215/BOM check and visual inspection before installation, but they don't label these as 'preventive'; the grouping is stated though.
- sentence 6: support check: partial - The passages give 500 mA for PVI 36TL and 300 mA for PVI 3800-7600TL, but they don't say the limit depends on the model in general.
- sentence 7: support check: partial - Passages say chalking can't be reliably predicted as a precursor and that modules with direct safety risk or failed insulation/wet-leakage tests should be replaced, but nothing says detection only reports an insulation fault after it happens.
-->
