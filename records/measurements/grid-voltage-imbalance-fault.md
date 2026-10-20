---
id: meas:grid-voltage-imbalance-fault
type: Measurement
name: Grid voltage imbalance fault
aliases:
- Grid voltage unbalance
- GridV.Unbal
---
The inverter raises this fault when it sees that the three grid phase voltages are unbalanced. The inverter compares the imbalance to a threshold parameter that can be changed in its settings. In most cases the inverter reconnects to the grid on its own after the grid returns to normal. If the fault keeps coming back, measure the actual grid voltage on each phase. If the phases differ greatly, ask the power company to fix it. If the difference between phases is within the range the local utility allows, adjust the imbalance parameter through the app or the LCD. If the fault still persists, contact the manufacturer. Power quality meters report negative-sequence and zero-sequence voltage imbalance as a percentage. They can also log voltage imbalance averaged over 10-minute and 2-hour intervals, which helps confirm what the inverter reported. On CPS inverters, differences in impedance and voltage between grid phases can also lead to a bus imbalance fault. The suggested fix is to raise the IDCmax limit, and to replace the inverter if the alarm continues.

<!-- review notes
- sentence 2: support check: partial - Passages show a configurable grid voltage imbalance threshold parameter, but don't explicitly say the inverter compares the imbalance to it (implied only).
- sentence 4: support check: partial - Passages say to measure actual grid voltage and contact the power company if phases differ greatly, but don't say 'on each phase' or ask them to 'fix it' explicitly; essentially paraphrase.
- sentence 6: support check: partial - Passages show negative- and zero-sequence voltage imbalance in % and 10-minute/2-hour aggregated voltage imbalance, but nothing about confirming inverter reports or 'power quality meters' being used that way.
- sentence 7: support check: partial - Fault0110 bus imbalance fix (raise IDCmax, replace inverter) is stated, but the passages don't say CPS inverters or that grid phase differences cause the fault beyond the instruction to cope with them.
-->
