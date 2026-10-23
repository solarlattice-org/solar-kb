---
id: stressor:flash-bad-sectors
type: Stressor
name: Flash memory bad sectors
aliases:
- bad blocks
---
Bad sectors are faulty areas in the flash memory of an inverter's monitoring unit. They are a listed cause of flash memory failure, which Huawei inverters report as alarm 61440. Flash memory is non-volatile storage that keeps data such as firmware when the power is off. The manufacturer rates this flash alarm as minor severity. The same alarm can also come from the flash memory running out of space, so a bad sector is only one possible cause. First, turn off the AC output switch and the DC input switch, wait 15 minutes, then turn both back on. If the fault is still there, replace the monitoring board or contact Huawei technical support. Other manuals say to replace the monitoring board. If the board is built into the monitoring device, replace the whole monitoring device.

<!-- review notes
- sentence 1: support check: partial - Passages list bad sectors as a cause of alarm 61440 (Flash Fault), but they don't define bad sectors as faulty areas of the monitoring unit's flash memory beyond that wording.
-->
