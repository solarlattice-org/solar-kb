---
id: symptom:invalid-external-signal
type: Symptom
name: Invalid external input signal
aliases:
- Incorrect input signal
- invalid input status
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Fronius Symo, State 568 appears on the display when the multifunctional power interface gets
    an incorrect input signal, the signal input function is set to Ext. signal and the trigger type is
    Warning. With trigger type Ext. Stop the inverter switches off and shows State 668 instead.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r15
    h: 90247f520522
  - src: src:fronius-fronius-symo-advanced-ul-operating-instructions-42-0410-0192
    loc: sec=h168
    h: 178ceafb49d2
  - src: src:fronius-fronius-symo-advanced-ul-operating-instructions-42-0410-0192
    loc: sec=h367
    h: 2f567690fb43
  review: drafted
---
On a Fronius Symo this symptom shows up as State 568 on the inverter display, which means the multifunctional power interface has received an incorrect input signal. The code only appears when the signal input function is set to Ext. signal and the trigger type is set to Warning. In that case the inverter keeps running and only shows the warning. If the trigger type is set to Ext. Stop instead, the same input condition switches the inverter off and the display shows State 668. The input can be set up as normally closed or normally open. Check that this setting matches how the external contact is actually wired. To clear it, acknowledge the state code and then check the devices connected to the multifunctional power interface. On SMA devices, a failure tolerance time parameter sets how long an invalid input status can last before it is recorded as a fault.

<!-- review notes
- sentence 4: support check: partial - The N/C or N/O connection type setting is stated, but nothing in the passages says to check that it matches the external wiring.
- sentence 6: support check: partial - Passages say failure tolerance time indicates the time as of which an invalid input status is recorded as a fault, but do not mention SMA devices or explicitly a duration it may last.
-->
