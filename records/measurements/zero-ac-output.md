---
id: meas:zero-ac-output
type: Measurement
name: Zero inverter AC output
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power stays at zero
- point: model_103.WH
  unit: unit:W-HR
  pattern: energy counter stops increasing
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: normal plane-of-array irradiance while the inverter output is zero
- point: model_103.A
  unit: unit:A
  pattern: AC current stays at zero during the event
- point: model_103.DCA
  unit: unit:A
  pattern: DC input current falls to zero because power conversion stops
---
The inverter stops feeding power into the grid, so the AC output power reading drops to zero. With the ON/OFF switch set to OFF, the display's Pac value should read 0.0. An inverter in a failure state produces no power. A complete inverter failure, where the unit is not operating, is a listed failure mode for this component. When the inverter detects a DC arc fault while running, it disconnects from the AC grid. It stays off until someone clears the arc fault or resets the operation inhibition by hand. Pressing the emergency stop button trips the DC load switches and the AC circuit breakers right away, which disconnects the inverter from the grid. An internal inverter fault can also cause an emergency stop status. On some hybrid units, the rapid shutdown or emergency power off switch stops all AC output, to both the grid and the backup loads. If the DC input does not supply enough power, for example because of snow on the modules or low irradiation, the inverter stops feeding in and cannot reconnect to the grid. If no power is fed into the grid for more than 10 minutes, some inverters disconnect, shut down and turn their LEDs off. The communication interfaces stay powered. Before working on the unit, confirm that no voltage is present. Use a measuring device rated for the inverter's maximum AC and DC voltage.

<!-- review notes
- sentence 1: support check: partial - Passage says Pac should be 0.0 since the inverter is OFF, but doesn't state that the inverter stops feeding the grid in general; mostly matches the display note.
- sentence 6: support check: partial - Passage says it can no longer connect to the grid, but the stated 'not enough DC power' cause is given; 'cannot reconnect' is fine, though the statement is essentially supported with only minor wording differences.
- sentence 7: support check: partial - Passage states the 10-minute disconnect/shutdown and powered interfaces under 'Off grid (LEDs off)', which is consistent, but 'some inverters' and LEDs turning off are only implied by the heading.
-->
