---
id: comp:pv-disconnect-switch
type: Component
name: PV array disconnect switch
aliases:
- DC switch disconnector
- array switch disconnector
- PV module switch
---
A PV array disconnect switch separates the PV array from the inverter. It is installed either inside the array or between the array and the inverter. Together with the inverter and a rapid shutdown initiation device, these switches make up a complete PV Rapid Shutdown System under the NEC. SunSpec-compliant switches receive a permission-to-operate signal from the inverter over the DC input conductors. When that signal stops, the switches must lower the line voltages in the array. If any module connected to the inverter lacks a SunSpec-compliant switch, the inverter cannot start feeding in. On SMA inverters, the SunSpec Shutdown operating mode selects this type of switch. The switches must disconnect the array within 15 seconds of rapid shutdown initiation. The combined standby voltage of all switches in one string must stay below 30 V. SMA event 9037 means the switches did not connect the PV generator. Event 9034 can mean the array was not disconnected correctly or the string's total switch standby voltage is above 30 V.
