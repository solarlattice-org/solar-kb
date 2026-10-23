---
id: comp:grid-relay
type: Component
name: Grid tie relay
aliases:
- Grid relay
- Line tie relay
- Inverter relay
- Inv Relay
---
The grid tie relay is the switch inside the inverter that connects its output to the utility grid and disconnects it again. Some grid operators require a signal as soon as the inverter connects to the grid. On SMA inverters the multifunction relay can be set to report the grid relay's switching status for this purpose. The main failure mode is relay failure: the relay contacts weld shut or stay open. CPS inverters report grid relay problems as Fault0100 (grid relay fault) or Protect0020 (grid relay error). Some models also use Protect0120, Protect0130 or PFault0030 for grid or inverter relay faults. The recommended first step is to switch both the AC and DC switches off, wait for stored energy to discharge, and then switch both back on. The manuals give a wait of 1 minute or 5 minutes depending on the model. If the fault does not clear after the restart, CPS manuals say to replace the inverter or, on some models, to contact after-sales service.

<!-- review notes
- sentence 1: support check: partial - Passages mention a line tie relay with welded/open contacts and a grid relay switching status signal, but none define the grid tie relay as the internal switch connecting/disconnecting the inverter output to the grid.
- sentence 3: support check: partial - The alarm describes contacts welded or open, but nothing says this is the main failure mode.
-->
