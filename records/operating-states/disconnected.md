---
id: state:disconnected
type: OperatingState
name: Disconnected from grid
aliases:
- grid disconnected
- off-line
- disconnected
- Disconnection from the grid
- Missing Grid
- Grid fault
- Grid incident
category: Inverters
---
In this state the inverter is not connected to the utility grid. On FIMER and ABB string inverters it means no grid voltage is present, so the inverter cannot connect, and the display reads "Missing Grid". On KACO blueplanet inverters, you can disconnect the inverter from the grid on purpose, either after logging in to the web interface or with the function button on the housing. Message 226 then appears. To reconnect, hold the function button for more than 5 seconds or switch the grid connection back on in the web interface. LEDs also show this state. On the Solectria PVI the GRID LED flashes during a grid fault and stays lit when the grid is normal. On the Sunny Island the grid LED is off when there is no voltage from the generator or the utility grid. On UNO-DM inverters set to Production mode, the output relay switches while the inverter is connected to the grid. It returns to its resting position whenever the inverter disconnects, whatever the reason. When a CPS inverter reports that it cannot detect the grid, first watch it for about 10 minutes to see whether the alarm clears by itself. If it does not, check the grid voltage and frequency and the inverter's grid cable, then contact the service center. On Fronius Symo inverters, automatic reconnection stops after five grid disconnections caused by excessive leakage current. Someone must acknowledge State Code 607 on the display before the inverter will reconnect.

<!-- review notes
- sentence 3: support check: partial - Solectria GRID LED flash on fault and on when normal, and Sunny Island grid LED off with no voltage, are stated; but the brand attribution to Solectria PVI and Sunny Island isn't in the passages' text (LED entries unattributed), and 'stays lit' fine.
- sentence 4: support check: partial - Relay behavior is stated, but the passage doesn't mention UNO-DM specifically as the product, though Production mode is described.
- sentence 6: support check: partial - Passages state the five-disconnection leakage current rule and State Code 607 acknowledgement, but don't name Fronius Symo.
-->
