---
id: meas:stow-event-output-dip
type: Measurement
name: Output dip during stow
signals:
- point: model_103.W
  unit: unit:W
  pattern: intermittent drop during logged stow intervals while irradiance remains supportive
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance stays high during the same logged stow intervals
- point: model_307.WndSpd
  unit: unit:M-PER-SEC
  pattern: gusts at or above the active controller wind threshold coincide with logged stow commands
---
This signature shows up as output dips while irradiance would otherwise support normal production. It happens when single-axis trackers move to a high-tilt protective stow angle because measured wind has gone over the controller threshold. The dip is intermittent and follows the weather. It is most visible on gusty days, when rows go into stow again and again, and it lasts until the rows return to normal tracking. The failure mode behind it is tracker wind stow production loss: gust-triggered stow moves the trackers away from the best tracking angle. To confirm it, line up the timestamped stow and return-to-track events in the tracker controller log with SCADA production, irradiance and inverter status. This separates stow loss from clipping, grid curtailment, outages and sensor faults. Use high-frequency wind data, such as three-second gusts, one-minute averages or met mast data, rather than hourly averages. Losses can be bigger than hourly weather data suggests. Monthly reviews can miss these dips if they are grouped under generic availability, curtailment or weather variance, so track them as a defined tracker operating mode. Do not lower the stow thresholds to win back energy unless the tracker supplier and a structural engineer confirm that the change stays within the design envelope.
