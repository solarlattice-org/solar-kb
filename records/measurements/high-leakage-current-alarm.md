---
id: meas:high-leakage-current-alarm
type: Measurement
name: High leakage current alarm
aliases:
- GFCIErr
- GFCI.Err
- leakage current high
- Dynamic leakage current high
- Fault0090
signals:
- point: model_103.W
  unit: unit:W
  pattern: inverter output drops to zero when the leakage protection trips
---
The inverter raises this alarm when it measures too much leakage current from the system to ground. Some inverters log it as a protection event, GFCIErr. A separate fault code covers high dynamic leakage current. The leakage current limit is a protection parameter that can be set in the inverter. To find the source, disconnect the inverter from the grid and open the fuse holders so each PV string is isolated. Then test the strings. Reconnect one string at a time and restart the inverter until the alarm returns. Then trace that string to find where current leaks to earth ground. Front delamination or bubbles can weaken module insulation, especially if water gets in. The inverter may then shut down because of leakage current. Potential induced degradation is linked to leakage current. In some cases, excessive leakage current comes with corrosion and delamination of the module.
