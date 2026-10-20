---
id: meas:arc-fault-alarm
type: Measurement
name: Arc fault alarm
aliases:
- ARC Protect
- Electric arc detected
- Arc-fault
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power falls to zero when the inverter shuts down on arc detection
- point: model_103.DCA
  unit: unit:A
  pattern: DC input current stops at the moment of the arc fault shutdown
---
An arc fault alarm is an inverter protection event that is raised when the arc fault detector senses an arc on the DC side. The detector looks for the electrical noise that usually comes with a DC series arc, and the inverter shuts down when it finds a series arc. Some inverters show this as an ARC Protect message. Others log it as an electric arc detected event. If the arc-fault circuit interrupter was triggered through operation inhibition, someone has to reset that inhibition by hand before the inverter runs again. Before treating it as a real arc, check that the logic connector to the arc board is secure. Then run the arc fault test from the settings menu. If the alarm comes back, the arc board or the wiring box may need replacing by the manufacturer's service, so a faulty detector can also cause it. A separate self-test error saying the interference level is too high points to a fault in the arc-fault circuit interrupter itself. Its cause has to be found by service.

<!-- review notes
- sentence 1: support check: partial - Passages say an arc is detected (and DC series arc detection), but don't explicitly define an alarm raised when the detector senses an arc on the DC side; 'Arc-fault' definition is bare.
- sentence 4: support check: partial - Passage says the operation inhibition must be reset manually, but doesn't explicitly say the inverter doesn't run until then.
- sentence 5: support check: partial - Steps to check connector and run the arc fault test are listed, but the passage doesn't frame them as a check before treating it as a real arc.
- sentence 6: support check: partial - Passages say contact CPS Service to replace arc board or wiring box if alarm recurs, but don't state explicitly that a faulty detector can cause the alarm ('may need' is inferential).
- sentence 7: support check: partial - Passage says an error occurred during the arc-fault interrupter self-test and service must determine the cause, but doesn't say it points to a fault in the interrupter itself.
-->
