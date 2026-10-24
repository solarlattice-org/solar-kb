---
id: state:backup-operation
type: OperatingState
name: Backup operation
aliases:
- backup mode
- EPS mode
- battery-backup operation
- Emergency Power Supply
- automatic backup operation
- Battery backup
category: Storage
---
Backup operation means the inverter feeds the backup loads from solar power and the battery while the utility grid is down, using its backup output (called the EPS output on Solis inverters). In SMA automatic backup operation, the transfer switch moves to backup automatically once the grid has failed for a set minimum time, which is 5 s by default and can be set from 0 s to 600 s. The system returns to parallel grid operation only after the grid has been back for a set time, which is 300 s by default. During that changeover the backup loads go without power for a short gap, 5 s by default. You will hear the transfer switch click when it goes into backup operation and again when it switches back to the grid. On Solis inverters with EPS mode for Italy, the backup port stays off while the grid is present and turns on only during an outage, after a switching delay that can be set from 10 to 99,990 ms. Battery charge set aside for backup operation cannot be used during normal grid operation. On Solis, the EPS depth-of-discharge setting gives the minimum charge kept for backup use. To test backup operation, switch off the pre-meter breaker to simulate a grid failure, check that the backup loads get power, then switch the breaker back on and check that the system returns to the grid.
