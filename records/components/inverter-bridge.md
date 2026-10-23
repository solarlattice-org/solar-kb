---
id: comp:inverter-bridge
type: Component
name: Inverter bridge
aliases:
- power module
---
The inverter bridge is the power-electronics stage inside an inverter, and SMA inverters report a disturbance in it with the SD-WR-Bruecke or SD-inv-bridge message. In transformerless inverters the bridge can be damaged by sporadic ground faults and insulation errors in the PV array, so a power stage fault often points back to the DC installation. When this fault occurs the inverter disconnects from the grid and then tries to reconnect, the yellow LED flashes code 5, and the error can be sporadic or continuous. To find the cause, measure the insulation resistance of all strings with an insulation tester, because a simple DC-to-ground voltage check only detects acute, severe ground faults. If the bridge message persists and becomes permanent after any insulation faults are fixed, the inverter has to be replaced. Overheating of the power module causes short interruptions of grid feed-in, and the inverter goes back to its startup phase until the temperature has dropped. For overheating, clean the cooling air openings and cooling elements, using compressed air if needed, and contact the installer if the code keeps returning. Some inverters also limit output power because of the power module, which shows up as derated production rather than a full stop.

<!-- review notes
- sentence 1: support check: partial - The passage says the message indicates a disturbance in the power electronics, but it never defines the inverter bridge as the power-electronics stage.
- sentence 2: support check: partial - The passage says the bridge in transformerless inverters can be damaged by sporadic ground faults and that the error can be caused by DC installation faults, but it does not say this is 'often' the cause.
-->
