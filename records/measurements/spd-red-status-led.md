---
id: meas:spd-red-status-led
type: Measurement
name: SPD red status LED
aliases:
- Red Alarm LED
- Red Service LED
- N-G Red LED
- NG Red Led Status
- neu/gnd red LED
- Phase C Red LED
---
Eaton SPD display panels have a green and a red LED for each phase. Units with a neutral have an extra pair for neutral-to-ground protection. Green means the mode is fully protected and red means protection has been lost. When an LED turns red, units with an audible alarm sound it. If someone pressed the silence button, the red LED stays on but the alarm is off. The alarm comes back after a power cycle if the fault is still there. A single red phase LED means that phase's protection is compromised or lost, usually after a significant surge or an extended temporary overvoltage. The surge protector is exhausted and must be replaced. If every phase LED is red, all protection may be gone, the SPD may be rated below the system voltage, or there may be a sustained temporary overvoltage. Check the system for overvoltage sources and fit an SPD with the correct voltage rating. A red neutral-to-ground LED with the alarm on means neutral-to-ground protection is compromised or lost, or a significant surge occurred. Replace the SPD. The red LED states can also be read remotely. Modbus status registers report 0 for off and 1 for on, and a BACnet binary object shows the neutral-to-ground red LED as ON or OFF.

<!-- review notes
- sentence 3: support check: partial - Passages give compromised/lost protection, significant surge or extended TOV, and replace SPD, but for TOV the solution is to check for TOV sources and correct, not simply that the SPD is exhausted; 'exhausted' is not stated.
- sentence 6: support check: partial - Modbus 0/1 for N-G red LED and phase red LED and BACnet NG red LED ON/OFF are stated, but 'status registers' generally and 'binary object' being BV rather than a read-only status are fine; the claim about all red LED states is only shown for N-G and phase A.
-->
