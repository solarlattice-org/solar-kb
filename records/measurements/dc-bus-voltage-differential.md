---
id: meas:dc-bus-voltage-differential
type: Measurement
name: DC bus half-voltage difference
aliases:
- Bus imbalance
- Bus Voltage Difference High
- Bus Volt Diff High
- Voltage imbalance at neutral point
---
This signature is a mismatch between the positive and negative halves of the inverter's internal DC bus. Some inverters report each half separately, for example as BUS+ and BUS- registers sampled by the PID board. The inverter trips on this condition when the difference between the two half-bus voltages exceeds a protection value that can be configured over Modbus. In monitoring data it shows up as a status bit labelled 'bus voltage difference high', which maps to codes such as Protect0070 or Protect0020 depending on the model. Manuals list the related bus imbalance codes as Protect0070 and Fault0110. They attribute these codes to differences in impedance and voltage between grid phases during transient conditions. The suggested first step is to raise the DC current limit so the inverter has more room to adjust. If the alarm still comes back, replace the inverter. Some inverters report the same condition as a voltage imbalance at the neutral point. These clear on their own once the deviation returns to the permitted range. For the Bus Volt Diff High code, watch the inverter for 5 minutes to see whether the alarm clears by itself. Contact service if it does not.

<!-- review notes
- sentence 2: support check: partial - A writable half-bus differential protection difference value register exists (RW, 1000-6000), but the passage doesn't say the inverter trips when the difference exceeds it.
- sentence 4: support check: partial - Protect0070 and Fault0110 are listed as bus imbalance with the impedance/voltage between grid phases in transient conditions text, but 'attribute to differences' is only implied by the remedy wording.
- sentence 6: support check: partial - Event 024 is voltage imbalance at neutral point with automatic recovery when deviation falls within range, but the passages don't say it is the same condition as the bus difference.
-->
