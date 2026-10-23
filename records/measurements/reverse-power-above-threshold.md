---
id: meas:reverse-power-above-threshold
type: Measurement
name: Reverse power above threshold
aliases:
- Generator Reverse Power Protection
- GnRevPwrProt
- Reverse power prot. (generator)
- Event 1408
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC active power flows back toward the grid or generator and stays above the reverse-power threshold
    for longer than the set trip time
---
This signature means power is flowing back into a running generator. The battery inverter flags it when the reverse power stays above its set threshold for longer than the set trip time. It happens when other AC sources in the system, such as PV, wind, water or CHP plants, feed energy into the active generator and drive it. When it trips, the inverter disconnects the generator. Reconnection is then blocked for at least the configured lockout time, which protects the generator from damage. On Sunny Island systems it appears as warning W401 or event 1408. Check for a reverse power protection entry in the Events menu, then acknowledge the generator error. A frequent cause is a reverse power threshold or trip time set too low. The factory defaults are 100 W and 30 seconds, so compare them with what the generator can tolerate and adjust them only with the generator manufacturer's agreement. An unstable external source can also cause the inverter to push current toward that source, so check the source's stability as well. On some older Sunny Island firmware, the transfer relay wrongly stays closed after this warning, and a firmware update is required.

<!-- review notes
- sentence 3: support check: partial - u4 states disconnection and connection blocked for at least ExtLkTm, but the 'protects the generator' is only loosely tied to lockout, and u4 is generic rather than Sunny Island-specific.
- sentence 5: support check: partial - Too-low threshold/time cause and defaults 100 W/30 s and manufacturer agreement are stated, but 'frequent cause' is not stated (only 'can occur') and 'factory defaults' is just 'default'.
-->
