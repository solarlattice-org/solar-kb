---
id: symptom:filter-malfunction
type: Symptom
name: Output filter malfunction
aliases:
- Filter Cont. Err
- Filter Contactor Open
- LC Filter not working
---
The message means the LC output filter is not working, but the inverter keeps producing AC power, so you may not see a drop in the power data. In Modbus monitoring, the same condition shows as the Filter Contactor Open fault bit, with value 8192 (hex 2000). First, turn off both the DC and AC sides and restart the inverter. If the error returns after the restart, an authorized service provider may need to inspect and service the inverter.

<!-- review notes
- sentence 2: support check: partial - Passage gives hex 2000, decimal 8192, fault Filter Contactor Open, but doesn't state it's the same condition as the UI message Filter Cont. Err or that it's a Modbus bit (linkage implied only).
-->
