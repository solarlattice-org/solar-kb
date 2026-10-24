---
id: state:constant-voltage-operation
type: OperatingState
name: Constant voltage operation
aliases:
- CV mode
- fixed voltage mode
- Cnst. Voltage Mode
- VolDCConst
- constant voltage mode
category: Inverters
---
In constant voltage operation the inverter holds its DC input voltage at a fixed value instead of tracking the maximum power point, so no MPP tracking takes place. On SMA inverters this is chosen with the DC voltage control type parameter Operation.CtrlType, which offers MPP or constant voltage (VolDCConst). While the SMA inverter is in its Run operating status, the Run substatus reads VolDCConst when constant voltage control is active, rather than Mpp. On Solis and CSI inverters the function sits in the Cnst. Voltage Mode menu: RUN enables a fixed input voltage, STOP disables it, and STOP is the factory default. With the mode enabled, the inverter does not operate if the input voltage is below the set voltage. One manual limits this function to maintenance personnel and warns that wrong use stops the inverter from reaching maximum power. If yield is low while constant voltage mode is active, measure the open-circuit voltage and check that it is not lower than the set constant voltage.
