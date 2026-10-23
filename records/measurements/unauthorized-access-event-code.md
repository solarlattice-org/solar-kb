---
id: meas:unauthorized-access-event-code
type: Measurement
name: Unauthorized access event code
aliases:
- Unauthorized Network Access
- Unauthorized Network Access Fault
- WARN-30
---
This signature is an inverter event entry, number 30, which reports that someone tried to access the inverter network without authorization. In the Modbus register map it appears as warning code WARN-30 and is reported on bit 29. The map also lists it in the high frequency 2 (HF2) group, where it is called the Unauthorized Network Access Fault. When this code appears, check whether there have been malicious attempts to access the inverter network.

<!-- review notes
- sentence 3: support check: partial - The row is garbled but pairs WARN-30, bit 29 with 'High Frequency 2 (HF2): Unauthorized Network Access Fault'; the HF2 grouping is only loosely implied by a malformed row.
-->
