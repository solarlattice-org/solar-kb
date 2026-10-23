---
id: mit:backup-load-reduction
type: Mitigation
name: Backup load reduction
---
Backup load reduction means lowering or removing the loads on an inverter's backup output so that the available power can carry what remains connected. On SMA inverters it is one of the corrective steps when input power is too low for backup operation, meaning the battery and PV together cannot supply the secure power supply load. In that case, also make sure enough PV power is available and the battery is charged correctly before you reduce the load. When a short circuit occurs at the SMA socket for manual secure power supply, check the socket wiring and the connected load. Then unplug the load and switch secure power supply operation back on. On Solis hybrid inverters, a backup overload alarm calls for checking whether the backup port load is above the rated output. If it is, reduce that load and restart the inverter. Large inductive loads can draw a high startup power that overloads the backup side, so it may help to take them off the backup circuit. As a design measure, a critical load panel can limit backup to essential circuits when battery capacity is limited or long backup duration is the priority.

<!-- review notes
- sentence 3: support check: partial - The measures are listed, but the passage does not say to do them before reducing the load; it gives no order.
- sentence 4: support check: partial - The measures are present, but the passage says to check that the load works correctly, not to check the 'connected load' for a fault; the order and the 'then' sequencing are also implied rather than stated.
- sentence 5: support check: partial - The Solis alarm solution is stated, but the passages do not say the alarm applies to hybrid inverters specifically, and the 'if it is' condition is only loosely implied.
-->
