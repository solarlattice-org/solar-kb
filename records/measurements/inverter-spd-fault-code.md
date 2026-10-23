---
id: meas:inverter-spd-fault-code
type: Measurement
name: Inverter SPD fault code
aliases:
- DC SPD fault
- AC SPD fault
- DC-SPD flt
- AC SPD flt
- SPD DC Err
- SPD AC Err
- DC-side SPD alarm
- AC-side SPD alarm
- Warn0040 (DC SPD)
- Warn0100 (AC SPD)
---
The inverter logs an SPD fault or alarm code, raised separately for the surge protection device on the DC side and on the AC side. Examples include W018 SPD DC Err and W019 SPD AC Err on FIMER units, where the alarm LED flashes; these codes appear only on models with a monitored SPD. Sungrow string inverters report code 072 for the DC-side SPD and 071 for the AC-side SPD, and Yaskawa units report Warn0040 and Warn0100. To confirm the code, check the SPD status window: if it has turned from green to red, the SPD is damaged, possibly from a local thunderstorm, and the cartridge must be replaced. If the window still shows green, the code may come from poor contact between the SPD and its holder, so reseat the module in its socket. Before replacing the SPD, measure the AC and DC voltages, including the voltage from each pole to ground, and check that they are normal. For an AC SPD fault, also check whether the micro circuit breaker wired in series with the SPD has tripped. On some large inverters this fault is rated major, meaning the inverter shuts down and stops feeding power to the grid.

<!-- review notes
- sentence 4: support check: partial - Green-to-red meaning damage, thunderstorm cause and replacement are stated, but passages add measuring voltages first; 'cartridge' appears only in the FIMER text, so the combined statement is slightly simplified.
- sentence 6: support check: partial - Passages say to measure AC/DC parameters including pole-to-ground voltages and replace when normal, but the 'before replacing' ordering is somewhat implied and the u6 wording says replace when parameters recover to normal.
-->
