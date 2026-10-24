---
id: comp:rapid-shutdown-transmitter
type: Component
name: Rapid shutdown signal transmitter
aliases:
- PLC transmitter
- RSS Transmitter
- Transmitter-PLC
- PLC signal transmitter
- SunSpec RSD transmitter
- Sunspec powerline communication transmitter
- Built-in MLRSD Sunspec Transmitter
- Integrated SunSpec-certified Transmitter
- RSD transmitter
- integrated MLRS transmitter
---
The rapid shutdown signal transmitter is the inverter-side half of a module-level rapid shutdown system. It talks to receivers mounted at each PV module by sending a power line communication signal over the PV DC conductors. It can be built into the DC side of the inverter or its wire box at the factory. It can also be mounted near the inverter in its own enclosure, with its own small power supply and current transducers. The transmitter draws power from the AC side. While powered, it sends a keep-alive or heartbeat signal. If the grid is lost, or the AC disconnect or breaker is opened, the signal stops and the module receivers drop into shutdown mode. Transmitters are brand-specific: a Tigo RSS Transmitter works with Tigo TS4-F receivers, while an APsmart Transmitter-PLC works with RSD-S-PLC and RSD-D receivers. Order the transmitter that matches the receivers on site. Known failure modes include crosstalk when several PLC transmitters share one roof, which weakens receiver operation, and loss of the keep-alive signal. If string voltages stay at the low shutdown level, confirm the inverter has AC power, the rapid shutdown switch is released, and any external DC switch is on so the signal can reach the receivers. One manufacturer states its transmitter can signal receivers up to 500 feet away. The systems are built to meet NEC 690.12 and CSA C22.2 No. 330, and certified as a PV Rapid Shutdown System (PVRSS).

<!-- review notes
- sentence 2: support check: partial - Integrated on DC side and external enclosure with small power supply and current transducers are stated (u1), and wirebox integration (u10), but 'wire box' factory build is only loosely supported and the passages don't say 'its wire box at the factory' exactly.
- sentence 4: support check: partial - Tigo RSS with TS4-F and APsmart Transmitter-PLC with RSD-S-PLC/RSD-D are stated, and ordering matching wire box is advised, but 'brand-specific' is only implied (u21 says RSS only compatible with Tigo; SunSpec transmitters compatible with all SunSpec receivers).
- sentence 5: support check: partial - Crosstalk from multiple transmitters is stated (u2) and loss of keep-alive causes shutdown, but loss of keep-alive is described as normal function, not a 'known failure mode'.
-->
