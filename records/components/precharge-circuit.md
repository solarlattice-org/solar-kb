---
id: comp:precharge-circuit
type: Component
name: DC link precharge circuit
aliases:
- Precharging circuit
- Pre charging circuit
---
The DC link precharge circuit is a part of the inverter that pre-charges the DC link before the inverter starts operating. In SMA Sunny Central CP XT inverters, error 6456 reports that this circuit is defective (precharge circuit failure). For this event the manual lists the inverter behavior as a warning and tells the operator to contact the SMA Service Line. When the fault is present, the data log can show an AC voltage metering frequency that does not match the grid AC voltage. Before calling service, check whether the inverter has the Q at night function and whether its parameter is enabled. Also check the precharge input fuses and the precharge feedback signal at terminals X14-8 and X14-9 on the SC20CONT board, and contact SMA service if they are fine.

<!-- review notes
- sentence 1: support check: partial - The passage says only that the DC link pre-charging circuit is defective; it doesn't say the circuit pre-charges the DC link before the inverter starts operating.
- sentence 5: support check: partial - The article does ask about the Q at night function and whether its parameter is enabled, but the flow is conditional, with a 'contact SMA Service' branch. It doesn't plainly say to check this before calling service.
-->
