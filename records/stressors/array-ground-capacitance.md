---
id: stressor:array-ground-capacitance
type: Stressor
name: High PV array capacitance to ground
aliases:
- leading leakage currents
- capacitive leakage current
- leading leakage current
- capacity of the PV modules to ground
- parasitic capacitance
- Riso varies with humidity/dew
- PV generator leakage capacitance
- High PV array leakage capacitance
- stray capacitance
- PV capacitance to ground
---
Every PV array has some capacitance to ground. The module surface faces a grounded frame or roof, so together they act like a capacitor. Large, high-power arrays have more of it. Inverters pass part of the grid AC voltage onto the array. This keeps recharging that capacitance and drives a capacitive leakage current to ground. Single-phase transformerless inverters cause much more of this current than three-phase units. The leakage current can trip the inverter's residual current monitoring, which causes a short disconnection followed by automatic restart. It can also trip the feed-in line's RCD, which has to be reset by hand. The capacitance does not damage module insulation itself. It shows up as leakage current faults and production interruptions. Capacitance rises when the array is wet. It is highest in heavy rain and on mornings with condensation, and very low in full sun. Water films on the glass, grounded frames and roof area all add to it. The risk is highest with large module areas, modules mounted close to a grounded surface, glass-glass modules or modules with metal rear panels, and modules laid flat across galvanized steel roofs. If leakage alarms only come in rain or on damp mornings and evenings and clear by themselves, they are usually normal. If they happen often, check cables, cable routing and grounding, then adjust the leakage threshold to suit the site. Exposure is reduced at the planning stage. Calculate the array's capacitance to ground and keep it below the capacitance limit given in the inverter manual.

<!-- review notes
- sentence 6: support check: partial - Large area, small distance to ground, laminate/metal rear panel high capacitance and carpet installation on galvanized steel roofs are supported, but glass-glass modules are described only as reaching peak values in heavy rain, not as higher risk.
- sentence 7: support check: partial - Normal if morning/evening/rain with automatic recovery and adjust thresholds if frequent are stated, but checking cables, routing and grounding is listed only as system-factor troubleshooting, not as the explicit step when alarms are frequent.
-->
