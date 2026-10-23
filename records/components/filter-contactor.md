---
id: comp:filter-contactor
type: Component
name: Filter contactor
---
When the inverter shows the Contactor Fail event, the manual says the filter contactor did not close. Over Modbus, the inverter can report a fault called Filter Contactor Open. The related Filter Cont. Err event means the LC filter is not working, although the inverter keeps producing AC power. For both events, first switch off DC and AC, then restart the inverter. If the problem does not clear, an authorized service provider may need to inspect and service the inverter.
