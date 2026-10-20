---
id: meas:dc-input-overcurrent-event
type: Measurement
name: DC input overcurrent event
aliases:
- Overcurrent at the DC input
- DC overcurrent
signals:
- point: model_160.DCA
  unit: unit:A
  pattern: input current on the affected PV input reaches the inverter's overcurrent limit just before
    the event
- point: model_103.W
  unit: unit:W
  pattern: AC output briefly drops to zero while feed-in is interrupted, then resumes
---
This signature is an inverter event that reports overcurrent on the DC input side, coming from the PV array. If the message comes up often, check that the PV array is rated and wired correctly. The related events 3801 and 3802 report DC overcurrent too. For these, check the PV array and look for ground faults in the PV system. During inspection, check the DC overcurrent protection: string or array protective devices must be fitted and correctly specified, and string cables must be sized for the combined fault current from parallel strings.

<!-- review notes
- sentence 4: support check: partial - The passage supports fitted and correctly specified string or array protective devices, and string cables sized for combined fault current. However, it requires cable sizing only for systems without string overcurrent protection, and the statement presents it as general.
-->
