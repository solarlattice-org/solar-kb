---
id: comp:control-board
type: Component
name: Control board
aliases:
- dominating control board
---
A separate arcing check board watches the DC line for arcing and passes an arc protection signal to the DSP on the control board. When the control board gets that signal, it takes the inverter off the grid for safety. If the arc detection board fails, the display shows 'arc board err' and the inverter will not reconnect to the grid until that board works again. An arc fault can only be cleared manually, for example with the ARCFaultClear menu. In metering equipment such as the SEL-735, the main board and microprocessor run self-tests on settings and code RAM, ROM, nonvolatile memory and program execution. A failed test disables the meter and latches the alarm output.
