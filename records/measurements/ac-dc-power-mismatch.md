---
id: meas:ac-dc-power-mismatch
type: Measurement
name: AC vs DC power mismatch
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC output power differs from DC input power by more than the inverter allows
- point: model_103.DCW
  unit: unit:W
  pattern: DC input power does not match the measured AC output power
---
To see an AC vs DC power mismatch, the monitoring system has to log power on both sides of the inverter. Inverter models differ in which parameters they report. Some inverters report only DC voltage on the input side. These units do not give a direct DC power value to compare with AC power. Other inverters report DC power, DC current and DC voltage for each MPPT input, along with AC power for each phase. With these values the DC side can be compared directly with the AC side. Monitoring guidelines list both AC active power at the plant injection point and power from the DC field as production data to record. The same guidelines record expected and real production as performance data. This gives a reference for judging a deviation. One inverter manual includes a chart of AC output power against DC input voltage. Use this kind of curve to check what conversion behaviour is normal before calling a gap a fault.

<!-- review notes
- sentence 1: support check: partial - Table shows inverter models differ in reported parameters, but the passage does not state that monitoring must log power on both sides to see an AC/DC mismatch.
- sentence 2: support check: partial - Inverter #1 lists only DC voltage on the DC side with no DC power, but the table doesn't state it gives no direct DC power for comparison; Inverter #2 also shows only DC voltage.
- sentence 3: support check: partial - Inverter #3 lists DC power, current and voltage per MPPT plus AC power per phase, but the passage doesn't state a direct DC-to-AC comparison is possible.
- sentence 5: support check: partial - Row 14 lists Expected vs Real under performance data, but the passage does not say it serves as a reference for judging deviation.
- sentence 6: support check: partial - The passage only shows a figure heading for AC output power versus DC input voltage; it doesn't say it's from one manual's chart usage or advise using it to judge faults.
-->
