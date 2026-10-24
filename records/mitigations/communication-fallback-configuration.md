---
id: mit:communication-fallback-configuration
type: Mitigation
name: Communication-loss fallback configuration
aliases:
- fallback behavior
- Fallback setting
- fallback value
- Operating mode for absent system control
- waiting time until fallback
- Fallback active power
- communication failure between controller and energy meter
- Operating mode fallback
- Fallback
- system fallback
- Fallback set-point
---
Fallback is a preset operating mode that fixes how inverters feed in when the control link or external setpoints are lost, so plant behaviour stays defined during communication problems. It applies when an external setpoint is missing or invalid, when communication between a plant controller and its inverters fails, or when the link between an inverter manager and a SCADA system or power plant controller drops. In export limitation schemes it covers loss of the energy meter signal and similar export limitation control faults; it should be enabled and properly set up as part of a fail-safe design. To set it up, switch fallback on, enter the timeout after which it takes effect, and enter the fallback active power, reactive power or cos Phi value; for each setpoint you can choose to keep the last received values or apply the fallback values instead. Once triggered, the inverter leaves fallback only after a re-entry waiting time in which every trigger condition has stayed inactive the whole time. On Sunny Island systems, losing the energy meter link stops the unit and the PV inverters after an adjustable detection time of 1 to 30 seconds, with a default of 2 seconds. Changing the settings needs an SMA Grid Guard code and must be agreed with the grid operator. Fallback for Speedwire communication loss cannot be configured on inverters fitted with the Speedwire Webconnect Piggy-Back.

<!-- review notes
- sentence 3: support check: partial - Fallback activation on export limit failure/incorrect behavior and the fail-safe enable/configure requirement are stated, but energy meter signal loss is only implied via re-entry time text and 'similar faults' is loosely supported.
-->
