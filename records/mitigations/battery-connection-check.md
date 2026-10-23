---
id: mit:battery-connection-check
type: Mitigation
name: Battery connection check
---
A battery connection check confirms that the battery is switched on and that the power and communication cables between the battery and the inverter are fitted correctly. On SMA hybrid and storage inverters it is the corrective action for event 9308, a communication error in the battery system, and for event 9350, where a requested change of battery status did not happen in time. Make sure the battery is on and has no faults. Then check that the communication cable is properly made up and connected, that the CAN bus wiring is correct, and that the Enable and GND lines are on the right terminals. The communication cable must be twisted pair, at least Cat 5e, and must not exceed the maximum length given in the manual. Strip the wire ends far enough, and use bootlace ferrules on stranded wire. Check the power cable and the data cable to the battery pack, including their plug contacts for damage. Also check the grounding of both the inverter and the battery system, and follow the wiring plan for the approved battery. Next, run a communication test from the user interface. If the fault remains, check the battery using the battery maker's documentation and contact them. If the inverter detects the battery and reads its state of charge but the event keeps coming back, the Enable wire may be the only bad connection. This check has limits. On some older models, the inverter has to be replaced if the message persists after the cables are checked.

<!-- review notes
- sentence 2: support check: partial - The corrective actions for 9308 and 9350 are stated, but the passages do not say they are the same single action, or that it applies across SMA hybrid and storage inverters.
- sentence 3: support check: partial - Battery on, fault-free, cable and CAN wiring checks are stated, but 'Enable and GND on right terminals' is only 'correct connection of Enable and GND lines', and the fault-free check is from event 9350, not 9308.
- sentence 5: support check: partial - Power/data cable connection and plug contact damage (SB3600SE), grounding and wiring plan are stated, but across different articles and the grounding check is not for the same device context; this merges them.
-->
