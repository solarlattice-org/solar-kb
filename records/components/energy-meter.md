---
id: comp:energy-meter
type: Component
name: Energy meter
aliases:
- production meter
- solar meter
- net meter
---
An energy meter measures power and energy flow at one point of a site, such as PV production, building consumption, the utility interconnect or an AC-coupled battery. Where the meter's current transformers and voltage taps go depends on the meter type. A production meter only sees energy flowing out of the generation source. A grid or net meter can see flow in both directions: a positive value means power is coming from the grid and a negative value means power is going to the grid. Typical meter readings include three-phase real and reactive power, average line-to-line RMS voltage, frequency, and lifetime counters for imported and exported energy in Wh. A plant controller may mark a meter as invalid if its readings are out of bounds, it has lost communication, or it has detected a PT or CT failure. O&M guidance lists meter accreditation and calibration, and meter installation and connection, as staff skills. IEC 61724-1 is the standard for PV system performance monitoring.

<!-- review notes
- sentence 4: support check: partial - The points and units are listed, but the import/export counters are defined as energy charged/discharged by the battery, not generic imported and exported energy.
- sentence 5: support check: partial - The Meter Invalid point matches the conditions, but the passages don't mention a plant controller doing the marking, and PT/CT failure is only assessed if detection is used.
-->
