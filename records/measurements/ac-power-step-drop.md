---
id: meas:ac-power-step-drop
type: Measurement
name: Sudden AC power drop
signals:
- point: model_103.W
  unit: unit:W
  pattern: sudden step decrease equal to the power of one string, with irradiance unchanged
- point: model_103.A
  unit: unit:A
  pattern: AC current drops to zero when the AC side disconnects
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: plane-of-array irradiance stays at a usable level while power is low
- point: model_103.DCA
  unit: unit:A
  pattern: DC input current falls to zero when the inverter shuts down
---
A sudden AC power drop shows up in inverter monitoring data as an abrupt fall in AC output. When a string is disconnected, the drop equals the power that string was supplying. The same signature can be a real fault in full sun but normal behaviour under clouds, so compare it with past performance under similar weather before calling it a fault. A rapid shutdown trigger produces this signature because the inverter disconnects its AC side. Grid incidents also cause it. The inverter leaves the grid when the ten-minute average grid voltage is out of range, when grid voltage or impedance at the connection point is too high, when grid frequency is out of range, or when it detects a stand-alone grid. The inverter also shuts down automatically when PV voltage and power fall below the set value, when the AC grid fails, or when ambient temperature goes beyond the normal range. String inverters and micro-inverters shut down automatically when they lose the AC connection, as IEEE 1547 requires. The size of the step depends on the inverter layout. When a central inverter goes down, all of its production is lost, while one failed string inverter affects fewer arrays.

<!-- review notes
- sentence 3: support check: partial - The event row says the AC side was disconnected on Rapid Shutdown, but it does not mention any monitoring signature such as a power drop.
- sentence 7: support check: partial - The passage says a central inverter outage loses all its associated production and that fewer arrays are affected by one string inverter failure, but it does not mention the size of a step in the data.
-->
