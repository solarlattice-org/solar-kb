---
id: mit:arc-board-replacement
type: Mitigation
name: Arc board replacement
---
Arc board replacement means swapping out the arc detection board, or the wiring box that holds it, when the board has failed. It applies to arc detection board failure. It applies when the inverter shows an Arcboard Err or ARC Protect alarm. Possible causes of Arcboard Err are a poor contact on the arc board or a damaged board. Before replacing anything, make sure the logic connector to the arc board is firmly seated. Then run the Arc Fault Test from the Settings menu. If the alarm comes back, contact the manufacturer's service team to have the arc board or wiring box replaced. The arc board checks the line for arcing and sends a protection signal to the DSP on the control board, which then takes the inverter off the grid. While the arc board has failed, the inverter will not connect to the grid until the board works again. This is why replacement restores production. A real arc fault shown on the display can only be cleared by hand, using the ARCFaultClear command.

<!-- review notes
- sentence 6: support check: partial - The passages say the inverter won't connect to the grid until the arc board is OK, but they don't state that replacement restores production, which is an inference.
- sentence 7: support check: partial - Passages say an arc fault can only be cleared manually and that ARCFaultClear clears it, but they don't explicitly say that command is the only manual method.
-->
