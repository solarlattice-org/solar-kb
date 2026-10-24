---
id: method:pv-to-ground-voltage-test
type: DetectionMethod
name: PV-to-ground voltage test
aliases:
- Voltage between PV+ and earth, PV- and earth
- Test by measuring the voltage
- PV+ to earth voltage
- voltage measurement +/- to ground
- PV+ to PE / PV- to PE measurement
- ground fault location via voltage ratio
- PV- to earth voltage
- DC voltage between +/- and PE
- Voltage to ground
claims:
- claim_id: c1
  rel: produces
  target: meas:pv-ground-voltage-sum-equals-string-voltage
  note: A ground fault is indicated when all three readings are stable and the PV+ to PE and PV- to PE
    voltages together roughly equal the PV+ to PV- voltage.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h216
    h: 61d9a9ee5491
  - src: src:kb-sma-stptl-10-us-checking-the-pv-system-for-ground-faults
    loc: sec=h8
    h: 2477637201c1
  - src: src:kb-sma-sbx1spus40-checking-the-pv-system-for-ground-faults
    loc: sec=h8
    h: bfb63d797b92
  - src: src:kb-sma-stpxx-us-41-checking-the-pv-system-for-ground-faults
    loc: sec=h8
    h: d1392ef36f4c
  - src: src:kb-sma-sbx1xpus41-checking-the-pv-system-for-ground-faults
    loc: sec=h8
    h: d1392ef36f4c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
This test checks each PV string for a ground fault by measuring DC voltages against the protective earth (PE). Disconnect the inverter from all voltage sources first, because the voltages involved can kill. Take three readings on each string: positive to PE, negative to PE, and positive to negative. If all three readings are stable and the two voltages to PE add up to roughly the positive-to-negative voltage, the string has a ground fault. The ratio of the two voltages to PE shows where along the string the fault sits, for example between the second and third module. With rapid shutdown module switches installed, the switches put out a standby voltage once the inverter is disconnected, so use that standby voltage instead of the module voltage when you work out the fault location. If this test gives no clear result and the fault message stays on, do an insulation resistance measurement, which gives more exact results. On systems grounded through a resistor, a voltage-to-ground test done to the module maker's procedure confirms that the resistor value is correct and keeps the DC system within acceptable voltage or leakage current limits.
