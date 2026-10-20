---
id: mit:reload-parameter-file
type: Mitigation
name: Parameter file reload
---
Reloading the parameter file is the corrective action for SMA STP inverter event 7102. That event means the parameter file was not found or is defective, so loading it failed. The inverter keeps feeding in while this event is active, so the problem does not stop production. To fix it, copy the parameter file into the correct folder again. Event 10118 confirms the fix worked: it reports that the parameter upload is complete and the configuration file loaded. Event 7105 is a related case where parameters could not be set from the memory card. For that one, check that the parameters are set correctly and that you have an SMA Grid Guard code. The operating manual has a separate procedure for adopting a configuration from a file.

<!-- review notes
- sentence 4: support check: partial - 10118 reports parameter upload complete and configuration file loaded, but the passages do not say it confirms the 7102 fix or link the two events.
- sentence 6: support check: partial - Only a section heading 'Adopting a Configuration from a File' is shown; it suggests a section exists but the passage doesn't show it is a procedure or which manual.
-->
