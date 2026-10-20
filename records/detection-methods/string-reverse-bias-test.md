---
id: method:string-reverse-bias-test
type: DetectionMethod
name: Night string reverse-bias test
aliases:
- string wise BPD test
- BPD test
claims:
- claim_id: c1
  rel: produces
  target: meas:high-string-reverse-voltage
  note: At night, a small reverse current of 3% to 5% of rated Isc is fed into each string. A string that
    reaches an unusually high reverse voltage points to modules with an open bypass diode or an unconnected
    substring (failure mode A).
  quote: If a string with extraordinarily high reverse voltage is found
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:ir-warm-substring
  note: While reverse current is applied, a night IR inspection of the flagged string shows substrings
    warmed by a few kelvin. This locates the modules with unconnected bypass diodes or mode A failure.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  - src: src:iea-pvps-t13-30-2025
    loc: fig=46
    h: e4272b24daa9
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h5
    h: f6f94e604618
  review: drafted
---
The night string reverse-bias test feeds a small reverse current into each module string in the dark. The current is about 3% to 5% of the rated short-circuit current, and the reverse voltage the string reaches is measured. A string with an unusually high reverse voltage likely has modules with an open or unconnected bypass diode, or an unconnected substring in the junction box. To find the faulty modules, inspect the flagged string with an infrared camera at night while the reverse current is applied. Look for substrings that have warmed up slightly. The test targets junction box failure from cold solder joints (failure mode A) and bypass diode failure. Mode A cannot be seen in a normal daytime infrared inspection and goes unnoticed until the module is shaded. Resistive heating at a bad joint in mode A normally shows only under shading. Seeing it during this test is safer for the inspector, because a shaded module with this defect can heat within seconds and may char or burn. The test cannot tell a failed diode from an unconnected substring. That takes destructive analysis of the junction box. Use thermal inspection for the other connection failure modes (B and C). Because of the high fire risk, test all modules once a single failure is found.

<!-- review notes
- sentence 4: support check: partial - Mode A not detectable by IRT and unnoticed without shade is stated, but 'normal daytime' inspection is not specified and test targeting is only implied.
- sentence 6: support check: partial - Failing BPD cannot be differentiated from mode A without destructive analysis, and thermal inspection is recommended for B and C, but the claim that 'the test' cannot tell them apart is an inference.
-->
