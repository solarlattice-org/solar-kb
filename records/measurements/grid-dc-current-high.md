---
id: meas:grid-dc-current-high
type: Measurement
name: Excess DC in grid current
aliases:
- output DC component
---
This signature means the inverter has measured too large a direct-current share in the current it feeds to the grid. The inverter detects it itself and logs it as a grid incident or grid fault event. Several inverter models offer a protection setting for the output DC component, and its threshold is set in the same menu as the leakage current threshold. The sources here do not give a numeric limit or say which failure modes cause this signature.

<!-- review notes
- sentence 3: support check: partial - The passages show the OtherProtect menu sets thresholds for both leakage current and output DC component protection, but they don't say that several inverter models offer it; the evidence appears to come from CPS manuals.
-->
