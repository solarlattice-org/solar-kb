---
id: state:battery-charging
type: OperatingState
name: Battery charging
aliases:
- charging
- BatChrgOp
- Grid to Battery
category: Storage
---
Battery charging means energy from the PV system, or from the grid, is going into the battery; SMA monitoring shows this as the battery charging power. On the Sunny Island US display, a charging symbol at position D shows that charging is active (BatChrgOp). Event codes E203 to E207 record when the battery management switches between the float, boost, full and equalization charge methods. When the Sunny Island reaches the constant voltage phase, its battery management picks a boost, full or equalization charge. The Sunny Island adjusts the charging voltage for temperature. It lowers the voltage above 20°C and raises it below 20°C so the battery is not overcharged or undercharged. On Solis three-phase hybrids, a Time of Use charge period charges the battery at the set current until it reaches the charging cut-off voltage, which can be adjusted. During an SMA charging period, the battery charges at the set power and takes energy from the grid at night, or when there is not enough PV. Discharging is blocked during that period.

<!-- review notes
- sentence 1: support check: partial - Passages say power is charged from the system into the battery and list 'Grid to Battery (Charging)', but don't explicitly say PV or grid energy or that SMA monitoring shows it as battery charging power.
- sentence 2: support check: partial - Position D = active charging (BatChrgOp) is stated and E203, E204, E205, E207 are state changes for float, boost, full, equalization, but E206 (silent mode) is within the E203–E207 range and is not a charge method, and no 'charging symbol' is mentioned.
-->
