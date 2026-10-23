---
id: comp:backup-power-outlet
type: Component
name: Backup power outlet
aliases:
- SPS power outlet
- Backup Secure outlet
- Backup Socket (SPS)
- EPS (Backup) Port
- Backup Port
---
The backup power outlet is an external socket that is wired to the inverter together with a switch. When the grid fails, it lets the inverter power a selected load from the PV system. Once the outlet is switched on, the inverter disconnects from the utility grid and stops feeding in. The power it delivers to the outlet follows the solar irradiation, so the output can fluctuate strongly or drop to nothing. On Sunny Boy Smart Energy units this feature is called SMA Backup Secure. You start it by hand with the switch, it can supply loads from the battery or the PV array, and it needs SMA Backup Start installed. The outlet and switch connect to the terminals marked SPS inside the inverter. With Backup Secure, the cable bridge that grounds the N conductor must be in place. Overload, underload or low irradiance can briefly cut power to the outlet. The inverter tries again automatically after 20 seconds, which can start the connected load unexpectedly. Event 9203 reports a short circuit at the outlet. Check the socket wiring and the connected load. Event 9202 reports AC overvoltage in backup operation and needs the Service team. Because of a parameter setting, SBSE backup sockets have been found putting out 240 V instead of the selected 120 V, which can damage the connected devices. Make sure the Backup Voltage parameter is set to 120V. When the outlet is live, the green LED flashes and the display shows SPS-mode active. If the LED does not flash, either irradiation is too low or the load needs more power than is available.
