---
id: func:dc-arc-fault-protection
type: Function
name: DC arc-fault protection
aliases:
- AFCI
- arc-fault circuit interrupter
- arc fault detection
- AFD
- ArcFix
- Arc Guard
- SMA ArcFix
- DC series arc fault detection
- DC arc-fault circuit protection
- Arc Fault Circuit Protection
category: Protection
function_kind: protection
---
DC arc-fault protection watches the DC side of the inverter for electrical noise that points to a series arc, then stops the inverter when it finds one. Fronius Arc Guard uses an electronic circuit to check the DC current and voltage for contact errors and shuts the circuit down. This lowers the risk of overheating and fire at poor contact points. The function is required by NEC Article 690.11. Fronius also cites CSA C22.1 Art. 64-216. The CPS and Solectria inverters state compliance with UL 1699B. On the CSI 23/28KTL-CT, an arc trip shows ARC Protect on the LCD and must be cleared by hand. You can run an AFCI Test from the System Setting OtherCmd menu, which ends with TestFinish or AFCI Fault. The ABB UNO-DM inverters self-test the arc detection circuit at every power-up. After an arc trip they stay off the grid until someone presses the reset button on the DC wiring box. Check the DC cables and panels first to find the source of the arc. For the CPS ARC Protect or Arcboard Err alarms, check that the logic connector to the arc board is secure and run the Arc Fault Test. If the alarm comes back, call CPS Service to replace the arc board or the wiring box.

<!-- review notes
- sentence 3: support check: partial - NEC 690.11, CSA 64-216 and UL 1699B compliance are stated, but the passages don't name Solectria, and CPS isn't named either; 'required by NEC' is stated only for the NFPA 70 case, and Fronius brand isn't explicit.
- sentence 5: support check: partial - Self-test at power-up, manual reset, and checking DC cables/panels first are stated, but the passage says the reset button is on the left side and doesn't name ABB UNO-DM (the statement mentions only the DC wiring box, fine); the model name isn't in the passage.
-->
