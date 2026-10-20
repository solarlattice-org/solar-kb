---
id: meas:iv-curve-step
type: Measurement
name: IV curve step
aliases:
- Steps or notches
- notch in the curve
- inflex points
---
An IV curve step is a step or notch in the current-voltage curve of a module or string, where the current drops in stages instead of following one smooth curve. It points to a mismatch between parts of the module or array: a bypass diode switches on and carries current around a cell string that cannot pass the same current as the others. A step can only show up when the module has several cell strings, each protected by a working bypass diode. Typical causes are partial shading, partial soiling or snow cover, damaged cells or modules, a short-circuited or defective bypass diode, and heavy cell mismatch. Even one partly shaded cell can turn on its bypass diode and make a notch, so rule out shading and soiling before blaming hardware. Heterogeneous loss of transparency in the module can also produce inflection points in the curve. Record the curve with a portable IV curve tracer on an isolated string or module, or from an inverter that offers IV curve monitoring per MPP tracker. Then compare it with the expected curve, the datasheet values or an earlier measurement.

<!-- review notes
- sentence 3: support check: partial - The table footnote says inflection points are 'only possible with several strings of cells protected by working bypass diodes', but the u20 fragment doesn't show the footnote and 'only' is applied to a column entry; mostly supported yet the evidence is a fragmentary table.
- sentence 5: support check: partial - The note that one shaded cell can turn on the bypass diode and cause a notch is stated, but the advice to rule out shading and soiling before blaming hardware is not in the passages.
- sentence 7: support check: partial - Portable tracer, isolating the string, inverter I-V curve per MPP tracker, and comparing with expected, datasheet or previous curves are all supported, but the passages don't explicitly say to use a module, and the combined procedure is assembled from separate passages.
-->
