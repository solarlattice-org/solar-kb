---
id: meas:inverter-grid-voltage-deviation
type: Measurement
name: Inverter vs grid voltage deviation
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: reported AC phase voltage departs from an independent meter reading taken at the inverter terminals
    beyond the allowed window
---
This signature is a clear gap between the AC voltage the inverter shows on its display or web server and the voltage a meter reads directly at the inverter's AC connectors. In one documented case the inverter showed 150 V AC while the grid voltage actually present was 230 V. Because the inverter believes the grid voltage is too low, it may refuse to connect to the grid. A low-resistance ground fault on a connected PV string can distort the inverter's AC measurement. The grid check runs before the insulation resistance test at startup, so the low insulation resistance may not be shown. For an under-voltage alarm, open the DC switch and measure AC at the inverter test points, then compare that to the LCD reading. If the grid is normal but the display is low, the measurement circuit may be faulty and the inverter may need replacing. For grid-voltage events, read out the voltage and limit values stored in the inverter and compare them with a meter reading at the inverter terminals. If the event only happens at certain times, take the measurement at those times. Grid voltage at the inverter drops as soon as feed-in stops, so the peak that caused the trip usually cannot be measured afterwards.

<!-- review notes
- sentence 5: support check: partial - The passage lists DC switch OFF, checking AC at test points, checking the LCD reading for a possible bad measurement circuit, and replacing the inverter, but it doesn't explicitly state the 'grid normal but display low' condition or order, and it mentions a lower-limit adjustment and grid standard check not captured.
-->
