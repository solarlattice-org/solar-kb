---
id: mit:impedance-matching
type: Mitigation
name: Grid impedance matching
---
Grid impedance matching is one of the corrective steps Solis lists for the GRID-INTF alarm. That alarm means the inverter has detected an unstable grid or a high internal fault current. Before trying it, measure the AC voltage and test the AC line for harmonic distortion (THD) with the DC switch off. Then repeat the THD test with the DC switch on. Where several inverters share the connection, also try turning one of them off. The fix itself is either an impedance matching adjustment or an added impedance matching box at the grid connection. Grid impedance matters because a grid voltage or grid impedance that is too high at the inverter's connection point can make the inverter disconnect from the utility grid. Monitoring data can show whether impedance is the problem. Plot grid voltage against PV output: the slope of the regression line gives the equivalent grid impedance. Extending that line shows whether voltage will reach the trip threshold, such as 1.1 p.u., at high yield. The sources give no detailed procedure for the adjustment and no measure of how well it works. Internal inverter damage or a wire that came loose in shipping can raise the same alarm, so rule these out first.

<!-- review notes
- sentence 3: support check: partial - Impedance matching adjustment or box is listed, but the passage does not call it 'the fix itself' or say the box is added at the grid connection.
- sentence 6: support check: partial - Internal damage and a wire loose in shipping are listed as causes, but the passages do not say to rule them out first, and the claim that the sources give no procedure or effectiveness measure is not something the passages state.
-->
