---
id: meas:dc-bus-voltage-low
type: Measurement
name: Low intermediate circuit voltage
aliases:
- PV POWER LOW
- LOW PV POWER
- Power low
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: DC voltage low or falling, typically at dawn and dusk
- point: model_103.DCW
  unit: unit:W
  pattern: DC input power too low to sustain feed-in
---
The inverter reports that its intermediate circuit (DC link) voltage is too low to keep feeding power into the grid, or has fallen below the allowed threshold for feed-in. On Fronius inverters this shows up as status code 306, where the inverter briefly stops feeding the grid and goes back to the startup phase. Code 306 clears by itself and appears every morning and evening because irradiance is low; at those times it does not indicate a fault. Check whether the code keeps coming back while there is plenty of sunlight; if it does, call the system installer. Fronius code 443 is a related reading: the intermediate circuit voltage is too low or unsymmetrical, and the inverter stops feeding current into the grid. If code 443 persists, contact a Fronius-trained service technician.
