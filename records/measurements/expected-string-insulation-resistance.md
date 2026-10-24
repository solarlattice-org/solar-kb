---
id: meas:expected-string-insulation-resistance
type: Measurement
name: Expected string insulation resistance
aliases:
- calculated insulation resistance
- expected total resistance of the PV system
- Riso per module
- insulation resistance per PV module
- expected insulation resistance
- Riso
- expected total resistance
---
This is a calculated reference value: the insulation resistance you should expect for the whole PV system or for a single string, worked out with a formula from the inverter documentation. Calculate it for each string before you measure, then compare it with the measured insulation resistance. Get the exact insulation resistance of each PV module from the module manufacturer or the datasheet. If that is not available, use an average value per module: about 40 MOhm for thin-film modules and about 50 MOhm for polycrystalline or monocrystalline modules. The comparison is part of checking a PV system for ground faults, and it is used when a voltage measurement alone does not clearly show a ground fault. The measurement needs an insulation resistance tester and a suitable device to safely disconnect and short-circuit the PV array. Without such a device the measurement must not be carried out.

<!-- review notes
- sentence 2: support check: partial - Passages say to calculate expected insulation resistance per string as the first procedure step, but none state comparing it with the measured value.
- sentence 5: support check: partial - Passages say insulation resistance measurement is used when voltage measurement is insufficient for ground fault evidence and link to ground fault checking, but the comparison itself isn't explicitly stated.
-->
