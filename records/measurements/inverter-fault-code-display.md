---
id: meas:inverter-fault-code-display
type: Measurement
name: Inverter fault code display
aliases:
- Code on display
- Fault Indication Interface
- LCD Display
- Display Message
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: inverter AC phase voltage disagrees with the grid-side voltage measurement while a warning
    code is active
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero for a short time, then comes back after the inverter restarts
- point: model_103.A
  unit: unit:A
  pattern: AC current falls to zero during the short feed-in stop
---
When the inverter cannot run normally, its FAULT light comes on and a fault menu opens. The current faults the inverter has recorded can then be read on the LCD screen. A fault entry pairs a code with a short error message and an LED signal, for example a W018 or W019 code together with an alarm LED. Some faults have a message but no code. For example, Missing Grid or Vac absent appears when the inverter sees no output voltage on the AC side, and the fix is to check grid voltage at the AC terminal block. Surge arrester alarms are shown as SPD AC Err or SPD DC Err on models with monitored SPDs. A red inspection window on an arrester means its cartridge is damaged and must be replaced. Critical event messages can name an arc fault in the PV array, an AC contactor failure, an internal communication failure or a failed parameter download. The code shown on the LCD can also be read from Modbus fault registers, where each bit is mapped to a display code such as a relay fault or a GFCI fault. A grounding fault code should be checked together with the GFDI LED. If that LED is lit, the fuse should be replaced. A dark display does not mean the inverter is off, because a dark display can come from a failed internal component. Always confirm that the AC and DC disconnects are open.

<!-- review notes
- sentence 6: support check: partial - Modbus register table maps bits to LCD codes like relay fault (Fault0100) and GFCI fault, but passages don't state the LCD code is 'also read' from registers generally; the mapping is shown, though one bit has no code.
- sentence 7: support check: partial - Passage says for GFDIErr check whether GFDI LED is lit and if so replace fuse, but doesn't say to check it together with any grounding fault code generally; essentially supported for GFDIErr.
-->
