---
id: meas:iv-sloped-isc-region
type: Measurement
name: Sloped IV curve near Isc
---
On a healthy module, the horizontal leg of the IV curve slopes down only slightly. This signature is a clearly steeper downward slope in the current near short-circuit current. The slope at short-circuit current is read from an IV curve. A tracer records it by sweeping the voltage from zero up to open-circuit voltage under a known irradiance level. A steeper slope near Isc means the shunt resistance has dropped because of shunt paths in the cells, the interconnections, or both. Slight cell mismatch or slightly uneven yellowing of the encapsulant can also produce this slope. Uneven (heterogeneous) loss of transparency, uneven glass corrosion and uneven delamination are listed as failures that change the slope at Isc. They usually also lower Isc and can add inflection points to the curve. This signature lowers the fill factor and therefore the module's maximum power output. Before you blame a failure, rule out measurement errors, instrument setup problems and wrongly entered module or string data. Shading and soiling can also change the curve shape. Fault detection systems may compare the slope between Isc and the maximum power point with an expected value. They flag a fault when the slope deviates by a significant amount.

<!-- review notes
- sentence 1: support check: partial - The horizontal leg slightly sloping down on a normal curve is stated, but the passages describe a sloped curve near Isc as shunt-resistance decrease, with no specific 'clearly steeper' signature wording; the statement is also self-contradictory in framing.
- sentence 2: support check: partial - The tracer sweep from 0 V to Voc under known irradiance is stated, and Rsc is defined as the slope at Isc, but reading the slope from the curve is only implied.
- sentence 5: support check: partial - The table rows mark heterogeneous transparency loss, glass corrosion and delamination as affecting Isc, Rsc and inflection points, but 'usually' lowering Isc is not stated, and inflection points carry an asterisk condition (only with several cell strings protected by working bypass diodes) that is omitted.
-->
