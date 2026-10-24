---
id: mit:frequency-shift-power-control
type: Mitigation
name: Frequency-shift power control
aliases:
- P(f)
- FSPC
- Frequency Shift Power Control
- frequency-shift-power-control scheme
- power control via frequency
- Output Power Limitation of PV Inverter
- country data set for stand-alone mode
- Permanently derated
- power adjustment via frequency
- Frequency Shifting
- Freq-Watt
---
Frequency-shift power control lets a battery or hybrid inverter curtail AC-coupled PV inverters by changing the AC frequency it creates. No communication link between the units is needed. It is used in off-grid or backup systems. When the battery is full and PV power exceeds the load, it keeps the excess energy from overcharging the battery. The battery inverter raises the frequency. Once the frequency passes the start threshold, the PV inverter reduces its output, and at the limit threshold its output reaches zero. On SMA PV inverters, set the country data set to an island or off-grid mode. By default the inverter then begins curtailing at 61Hz and ramps linearly down to zero active power at 62Hz. The start and end points can be adjusted to match the battery inverter. PV inverters that do not support a frequency-watt response do not curtail smoothly. They shut off as the frequency shifts and come back on after the frequency is corrected. If the frequency goes outside the allowed band, the PV inverters disconnect. When a generator is running, the generator sets the frequency, so the PV inverters usually keep delivering full power. A PV inverter connected directly to the utility grid must keep the utility-required settings. Change frequency control parameters only when the grid operator asks for it.

<!-- review notes
- sentence 5: support check: partial - The shut-off and return after the frequency is corrected are stated, but the passage does not say that these inverters 'do not curtail smoothly'.
-->
