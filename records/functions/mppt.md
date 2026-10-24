---
id: func:mppt
type: Function
name: Maximum power point tracking
aliases:
- MPPT
- MPP tracking
- OptiTrac
- SMA OptiTrac
category: Control
function_kind: control
---
Maximum power point tracking is the technique an inverter uses to draw the most power it can from the PV array. It sets the operating point on the array's nonlinear I-V curve, which shifts with irradiance and temperature. SMA's tracking algorithm, OptiTrac, keeps the inverter at the array's MPP. Its successor, OptiTrac Global Peak, can also find several power maxima on partially shaded strings and is switched on through the operating parameters. The number of trackers depends on the inverter. The CPS SCA25KTL-DO-R/US-480 and the CSI 23/28KTL-CT/US-480 each have 2, while the CPS SCH200K-T-US-480 and SCH250K-T-US-600 each have 1. Some datasheets give limits for each tracker. The CPS SCH350KTL-DO/US-800 caps PV input current at 40 A per MPPT, and the CPS SCA25KTL-DO-R/US-480 lists 22kW of PV power per MPPT. You can check tracking effectiveness during I-V testing. Under steady conditions, record the operating voltage and power, then disconnect the array right away and trace its I-V curve. The operating power divided by the true maximum power is the MPPT efficiency.

<!-- review notes
- sentence 2: support check: partial - Global Peak details and activation via operating parameters are stated, but the passage doesn't describe OptiTrac itself keeping the inverter at MPP beyond implying it as the predecessor; 'tracking algorithm' is implied only.
-->
