---
id: meas:parameter-setting-failed-event
type: Measurement
name: Parameter setting failed event
aliases:
- Param. setting failed
---
The inverter writes an event to its log saying a parameter could not be set, and the displayed parameter keeps its previous value. Events 10101 and 10103 mean the requested value was rejected; check that the value is within the parameter's allowed thresholds, then enter the change again. Event 10121 means the device has to be stopped before the parameter can be changed. Event 10122 means the installation assistant must be started before the setting can be applied. Event 7105 is logged when parameters could not be loaded from the memory card; for grid-relevant parameters, make sure the SMA Grid Guard code is available. A successful change is logged as event 27103, which confirms the new value was adopted, so use it to check that a retry worked.

<!-- review notes
- sentence 1: support check: partial - Passages state the setting failed and the displayed parameter was not changed, but do not say the inverter writes it to an event log (though event numbers imply it).
- sentence 6: support check: partial - 27103 states the parameter change has been adopted, but the passages do not say it is the logged success event for use in verifying a retry (an inference).
-->
