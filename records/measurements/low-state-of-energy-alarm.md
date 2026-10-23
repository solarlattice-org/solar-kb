---
id: meas:low-state-of-energy-alarm
type: Measurement
name: Low state of energy alarm
---
This signature is a Low State of Energy alert raised by a Megapack battery system when its stored energy has fallen to a very low level. When the alert is active, at least one battery module has already switched into its protective battery off state. The alert is also published as a DNP3 status point in the controls and communications point list, so SCADA or plant monitoring can read it remotely. The alert has priority P1 and is handled on a critical path, because leaving the system at low state of energy can permanently damage the cells. The customer's first step is to try sending a charge command to the system and, if that does not work, to contact Tesla Industrial Storage Support. The alert also raises a Tesla alarm for remote review, and a field service ticket is opened if the problem cannot be fixed remotely.

<!-- review notes
- sentence 3: support check: partial - A DNP3 point with this label and index is listed, but the passages don't say it's a status point in a controls/communications list or mention SCADA monitoring.
- sentence 4: review: partial - P1 priority, the Critical path and possible permanent cell damage are all stated, but the passage does not say the priority or path is assigned because of the cell damage.
-->
