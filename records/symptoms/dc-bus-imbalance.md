---
id: symptom:dc-bus-imbalance
type: Symptom
name: DC bus voltage imbalance
aliases:
- Bus imbalance
- DC bus unbalanced voltage
- UNB-BUS
- Bus voltage difference is high
---
The inverter reports that the voltages on its internal DC bus are out of balance. Yaskawa Solectria and CPS string inverters show this as Protect0070 or Fault0110 (Bus imbalance), and Solis hybrid inverters show it as UNB-BUS. The manuals put the alarm down to transient conditions in which the inverter cannot cope with differences in impedance and voltage between the grid phases. The first fix the manuals give is to raise the IDCmax or DCImax limit, for example to 400 mA, so the inverter has more room to adjust during transients. If the alarm still comes back after this change, the manuals say to replace the inverter. On Solis units, first restart the system and check whether the fault is still there.

<!-- review notes
- sentence 1: support check: partial - Passages show Protect0070/Fault0110 (Bus imbalance) and Solis UNB-BUS 'DC bus unbalanced voltage', but they don't name Yaskawa Solectria or CPS, and 'internal' bus isn't stated.
- sentence 2: support check: partial - The passages only imply the cause through the fix wording (more room to adjust in transients to cope with phase impedance/voltage imbalance); they don't explicitly attribute the alarm to it.
- sentence 1: review: partial - Protect0070/Fault0110 (Bus imbalance) and Solis UNB-BUS 'DC bus unbalanced voltage' are stated, but the passages do not name Yaskawa Solectria, CPS or Solis hybrid models, and they do not call the bus 'internal'.
-->
