---
id: symptom:dc-link-fault
type: Symptom
name: DC link fault
aliases:
- Bus imbalance
- Bus over total voltage
- Bus over volt Hardware
- Bus Hardware overcurrent fault
- BUS over voltage (firmware)
---
A DC link fault shows up on the inverter display as one of several bus-related codes, covering bus overvoltage (hardware, firmware or total), bus hardware overcurrent, and bus imbalance. For bus overvoltage or bus overcurrent codes, first restart the inverter: switch both the AC and DC switches off, wait for the stored energy to discharge, then switch both back on. The manual gives a 5 minute wait for the hardware bus overvoltage and total bus overvoltage faults, and a 1 minute wait for the bus hardware overcurrent fault and the firmware bus overvoltage protection. If the inverter cannot clear one of these bus overvoltage or overcurrent codes after a restart, the manual says to replace the inverter. A bus imbalance code is handled differently. It is linked to unequal impedance and voltage between the grid phases during transients, so the first step is to raise the IDCmax limit, for example to 400mA. If the bus imbalance alarm still occurs after this adjustment, replace the inverter.
