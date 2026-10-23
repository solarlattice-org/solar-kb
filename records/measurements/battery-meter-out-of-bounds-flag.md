---
id: meas:battery-meter-out-of-bounds-flag
type: Measurement
name: Battery meter out-of-bounds flag
aliases:
- Battery Meter Out of Bounds
---
This signature is a read-only boolean status point from the battery meter. It is set when the meter's voltage or frequency readings fall outside their bounds. In the utility manual, the flag is set only after the meter voltage and frequency have stayed outside acceptable bounds for a given duration. Read it from Modbus register 32017 for an individual meter or from register 31013 for the aggregate meter location. The aggregate version is set when at least one of the aggregated meters has been out of bounds. An out-of-bounds condition sets the Meter Invalid point. That point can also come from lost meter communication or a detected PT/CT failure, so check those flags as well. A separate Unreasonable flag reports voltage or frequency readings that differ greatly from the reference minimum and maximum values. Read it together with this flag to tell the two conditions apart.

<!-- review notes
- sentence 6: support check: partial - The Unreasonable flag definition is stated, but the advice to read it together to tell the conditions apart is not in the passages.
-->
