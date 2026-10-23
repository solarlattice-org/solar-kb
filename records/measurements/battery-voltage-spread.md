---
id: meas:battery-voltage-spread
type: Measurement
name: Battery voltage spread
---
This signature shows up when the battery voltage measured by a Sunny Island on one line conductor falls outside its permissible measurement range. The reading can be too high or too low. In a cluster, each device reports on its own: the master at L1, slave 1 at L2 and slave 2 at L3. Comparing these readings shows which unit sees the deviating battery voltage. The display lists one event for the master and separate warnings for slaves 1, 2 and 3, each stating that the measuring range of battery voltage was exceeded. The current battery voltage can be read on the compact meter as BatVtg, next to the charging voltage setpoint BatChrgVtg. A low reading can mean the usable battery capacity is too small, for example because the battery has aged. A high-power load can also make the battery voltage collapse. A low reading at a slave unit calls for checking that all battery cells work. If single cells fail over years of operation, the nominal voltage can be set lower and a few cells can be removed. A high reading points to DC sources that are connected or configured incorrectly, or to a battery voltage above the target charge voltage.

<!-- review notes
- sentence 2: support check: partial - Master at L1, slave 1 at L2, slave 2 at L3 are stated, but nothing says comparing the readings identifies which unit sees the deviation.
- sentence 6: support check: partial - Checking cells is stated and cell failure allows lower nominal voltage (42–48 V) and removing up to three cells, but the passages don't link this to a slave's low reading and the stated range/limit are omitted.
-->
