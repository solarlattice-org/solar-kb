---
id: state:battery-discharging
type: OperatingState
name: Battery discharging
aliases:
- discharging
- Discharging the battery
category: Storage
---
Battery discharging means the system is currently drawing power out of the battery to supply the household loads. The battery discharges when the loads need more energy than the PV system is producing at that moment. On a Sunny Island with no generator or utility grid connected, the battery supplies the loads and the measured battery current reads positive. Discharging ends at a set limit: in Solis time-of-use discharge periods, at the settable discharging cut-off voltage; on Tesla off-grid sites, at the Minimum Off-Grid SOE, where generators are started. The LED pattern for this state depends on the brand: an Enphase IQ Battery flashes blue slowly, a Solis hybrid's battery light flashes blue every 3 s, and a Generac PWRcell flashes green rapidly at 0.5 s intervals. This is a normal operating state, so no action is needed. Discharge timing and rate can be adjusted in the time-of-use settings if the owner wants.

<!-- review notes
- sentence 6: support check: partial - Time-of-use adjustment of timing/rate is supported, but nothing states that discharging is a normal state requiring no action.
-->
